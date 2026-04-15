# 📓 Technical Notebooks Guide
This project consists of 6 dedicated Jupyter notebooks, each handling a specific stage of the data pipeline.

### 01_data_exploration.ipynb
- **Purpose:** EDA (Exploratory Data Analysis).
- **Key Step:** Identified 11 missing values in `TotalCharges`.
- **Solution:** Realized these were new customers (Tenure = 0). Imputed missing values with 0 instead of deleting them.
- **Visuals:** Used Seaborn to visualize churn across gender, contracts, and internet services.

### 02_rfm_segmentation.ipynb
- **Purpose:** Feature Engineering using marketing behavioral analysis.
- **RFM Logic:**
    - **Recency:** Using `tenure` (how long they've been with us).
    - **Frequency:** Count of additional services (OnlineSecurity, Backup, etc.).
    - **Monetary:** `MonthlyCharges`.
- **Outcome:** Created the `Segment` column (**VIP**, **Loyal**, **At-Risk**).

### 03_sql_analysis.ipynb
- **Purpose:** Cross-validation using SQL.
- **Database:** SQLite.
- **Key Query:** Calculation of churn rate grouped by contract type.
- **Why?** Proves that findings in Pandas are consistent and ready for enterprise SQL databases.

### 04_machine_learning.ipynb
- **Purpose:** Predictive modeling.
- **Models Used:** 
    1. Logistic Regression (Baseline).
    2. Random Forest.
    3. Gradient Boosting (Final Model).
- **Evaluation:** Achieved **0.84 ROC-AUC** after hyperparameter tuning via GridSearchCV.
- **Persistence:** Saved the final model as `best_model.pkl`.

### 05_web_app_setup.ipynb
- **Purpose:** Model Deployment.
- **Tech:** FastAPI / Uvicorn.
- **Outcome:** Setup a REST API endpoint that accepts customer data and returns a churn risk score (0-100%).

### 06_excel_report.ipynb
- **Purpose:** Automated reporting for non-technical stakeholders.
- **Tech:** `pd.ExcelWriter`.
- **Output:** Generated a multi-sheet Excel file (`reports/churn_full_report.xlsx`) containing raw data and summary statistics.
