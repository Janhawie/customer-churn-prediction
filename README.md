# 🔄 Customer Churn Prediction & Lifetime Value Analysis
This repository contains a full end-to-end data science project focused on predicting customer churn and analyzing its impact on business revenue.

## 📂 Project Structure
- **/notebooks:** 6 단계별 Jupyter notebooks (Exploration to Excel Reporting).
- **/data:** Raw and processed datasets.
- **/models:** Pickled machine learning models and scalers.
- **/app:** FastAPI web application for real-time predictions.
- **/reports:** Automatically generated Excel and PNG reports.
- **/documentation:** Full project knowledge base and interview guide.

## 📙 Project Documentation Hub
For a detailed breakdown of every phase, check out the files in the `documentation/` folder:
1. [Business Context](documentation/01_Project_Overview_and_Business_Context.md)
2. [Technical Notebook Guide](documentation/02_Technical_Notebooks_Guide.md)
3. [ML & Math Deep Dive](documentation/03_Machine_Learning_and_Math_Deep_Dive.md)
4. [Power BI & DAX Reference](documentation/04_PowerBI_Dashboard_and_DAX_Reference.md)
5. [Interview Prep Guide](documentation/05_Interview_Prep_Master_Guide.md)

## 🚀 How to Run the App
1. Install dependencies: `pip install -r requirements.txt`
2. Launch the API: `uvicorn app.main:app --reload`
3. Visit: `http://localhost:8000`

## 📊 Results Summary
- **Model:** Gradient Boosting.
- **Metric:** 0.84 ROC-AUC.
- **Insight:** $1.6M projected annual revenue loss identified.
