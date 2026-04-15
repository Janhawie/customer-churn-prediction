# 🔄 Customer Churn Prediction & Lifetime Value Analysis
## Project Overview & Business Context

### 🎯 The Business Problem
Customer churn (when customers stop using a service) is one of the most expensive problems for subscription-based businesses like Telecom. Losing a customer doesn't just mean losing their current monthly fee; it means losing all future projected revenue (Lifetime Value).

**Objective:** To build an end-to-end data solution that predicts churn before it happens and visualizes the financial impact to enable proactive retention strategies.

### 🛠️ The Data Universe
We used a dataset containing 7,032 customer records with 21 different attributes, including:
- **Demographics:** Gender, Senior Citizen status, Partners, Dependents.
- **Services Used:** Phone, Internet (DSL/Fiber), Online Security, Backup, Device Protection, Streaming TV/Movies.
- **Account Info:** Tenure, Contract Type (Month-to-month, One year, Two year), Payment Method, Monthly Charges, Total Charges.

### 📝 Key Business Metrics Defined
- **Churn Rate:** The percentage of customers who left out of the total customer base.
- **Monthly Revenue Lost:** The sum of `MonthlyCharges` for customers who churned.
- **Annual Revenue Lost:** `Monthly Revenue Lost * 12`. This is our "North Star" metric for management.
- **RFM Segments:** Grouping customers by Recency (Tenure), Frequency (Services used), and Monetary (Charges) to distinguish between **VIPs**, **Loyal Customers**, and **At-Risk Customers**.

### 💼 Why This Project Matters
By the end of this project, a business doesn't just see a "1" or "0" (Churn vs Stay). They see:
1. **Who is leaving?** (Segments)
2. **Why are they leaving?** (Contract types, Fiber optic instability, etc.)
3. **What is it costing us?** (Projected revenue loss)
4. **How can we stop it?** (Automated predictions via web app)
