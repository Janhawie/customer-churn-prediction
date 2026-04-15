# 📊 Power BI Dashboard & DAX Reference
This dashboard transforms the static model into a dynamic business tool.

### 1. The Interaction Logic (Cross-Filtering)
- **Clicking the Donut Plot (Segments):** The entire dashboard filters to show *only* that group (e.g., VIP).
- **Clicking the Scatter Plot (Tenure vs Charges):** Allows you to see if a specific high-paying customer who churned was a VIP or an At-Risk customer.

### 2. Key Visuals
- **KPI Card:** Annual Revenue Lost (The most important number for executives).
- **Stacked Bar Chart:** Churn Rate by Contract Type (Proves that longer contracts reduce churn).
- **Matrix:** Churn Rate by Internet Service and Contract (Finds "Problem Hotspots").

### 3. DAX Formula Reference
These are the formulas used for our calculations:

**Revenue Lost:**
```dax
Revenue Lost = CALCULATE(SUMX(telco_rfm, telco_rfm[MonthlyCharges] * 12), telco_rfm[Churn] = 1)
```

**Churn Rate:**
```dax
Churn Rate = DIVIDE(COUNTROWS(FILTER(telco_rfm, telco_rfm[Churn] = 1)), COUNTROWS(telco_rfm), 0)
```

### 4. Technical Tip: "Don't Summarize"
We had to set the X and Y axes of the scatter plot to **"Don't Summarize"** to force Power BI to show individual dots (individual people) instead of adding them all up into one big dot.
