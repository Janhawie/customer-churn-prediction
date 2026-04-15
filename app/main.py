
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
import pickle
import io

app = FastAPI(title="Customer Churn Predictor")
templates = Jinja2Templates(directory="app/templates")

with open('models/best_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('models/feature_columns.pkl', 'rb') as f:
    feature_columns = pickle.load(f)

print("✅ Model loaded!")

def preprocess(df):
    # ── Step 1: Fix TotalCharges if it's text ──────────────────────────────
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # ── Step 2: Convert Yes/No service columns to 1/0 ──────────────────────
    # These are the service columns that had Yes/No/No internet service values
    service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport',
                    'StreamingTV', 'StreamingMovies']

    for col in service_cols:
        if col in df.columns:
            df[col] = df[col].map({
                'Yes': 1, 'No': 0,
                'No internet service': 0,
                'No phone service': 0
            }).fillna(0).astype(int)

    # ── Step 3: Calculate Service_Count (sum of all service columns) ────────
    existing_service_cols = [c for c in service_cols if c in df.columns]
    df['Service_Count'] = df[existing_service_cols].sum(axis=1)

    # ── Step 4: Calculate RFM Scores (same logic as notebook) ──────────────
    # R_Score: lower tenure = higher risk score (4 = newest, 1 = oldest)
    df['R_Score'] = pd.qcut(df['tenure'], q=4,
                             labels=[4, 3, 2, 1],
                             duplicates='drop').astype(int)

    # F_Score: more services = higher score
    df['F_Score'] = pd.qcut(df['Service_Count'], q=4,
                             labels=[1, 2, 3, 4],
                             duplicates='drop').astype(int)

    # M_Score: higher charges = higher score
    df['M_Score'] = pd.qcut(df['TotalCharges'], q=4,
                             labels=[1, 2, 3, 4],
                             duplicates='drop').astype(int)

    # Combined RFM Score
    df['RFM_Score'] = df['R_Score'] + df['F_Score'] + df['M_Score']

    # Segment label
    def assign_segment(score):
        if score >= 9:
            return 'VIP'
        elif score >= 6:
            return 'Loyal'
        elif score >= 4:
            return 'At-Risk'
        else:
            return 'About to Churn'

    df['Segment'] = df['RFM_Score'].apply(assign_segment)

    # ── Step 5: One-Hot Encode nominal columns ──────────────────────────────
    nominal_cols = ['gender', 'Partner', 'Dependents',
                    'InternetService', 'Contract',
                    'PaymentMethod', 'PaperlessBilling', 'Segment']

    cols_to_encode = [c for c in nominal_cols if c in df.columns]
    df = pd.get_dummies(df, columns=cols_to_encode, drop_first=True)

    # ── Step 6: Add missing columns with 0, remove extra columns ───────────
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep only the exact columns the model was trained on, in the right order
    df = df[feature_columns]

    return df


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    # Drop columns that won't be needed
    df.drop(columns=['customerID', 'Churn'], errors='ignore', inplace=True)

    # Run full preprocessing
    df_processed = preprocess(df)

    # Scale
    df_scaled = scaler.transform(df_processed)

    # Predict
    predictions = model.predict(df_scaled)
    probabilities = model.predict_proba(df_scaled)[:, 1]

    results = []
    for i in range(len(predictions)):
        prob = round(float(probabilities[i]) * 100, 1)
        if probabilities[i] > 0.7:
            risk = "🔴 HIGH"
        elif probabilities[i] > 0.4:
            risk = "🟡 MEDIUM"
        else:
            risk = "🟢 LOW"

        results.append({
            "customer": i + 1,
            "churn": "⚠️ Will Churn" if predictions[i] == 1 else "✅ Will Stay",
            "probability": f"{prob}%",
            "risk": risk
        })

    return {"predictions": results}
