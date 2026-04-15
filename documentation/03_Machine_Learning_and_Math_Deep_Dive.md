# 🤖 Machine Learning & Mathematics Deep Dive
This document explains the "How" and "Why" of our predictive models.

### 1. The Models: RF vs GB
We compared two main ensemble models:
- **Random Forest (RF):** Builds 100+ decision trees in **parallel**. Each tree sees a random bootstrap sample of data and a random subset of features. The final result is the "average" of all trees.
- **Gradient Boosting (GB):** Builds trees **sequentially**. Each new tree learns specifically from the *residuals* (errors) of the previous tree. 
- **The Winner:** Gradient Boosting achieved higher accuracy (0.84 ROC-AUC) because it is more sensitive to complex, non-linear relationships.

### 2. The Mathematics of Metrics
- **ROC-AUC (Receiver Operating Characteristic - Area Under Curve):** This measures how well the model separates "Churn" from "Stay". An AUC of 0.84 means there is an 84% chance the model will rank a randomly chosen churner higher than a randomly chosen survivor.
- **Recall (Sensitive):** "Catching" the churners. Higher recall means fewer churners slip through the cracks.
- **Precision:** "Being right about predictions." Higher precision means we don't accidentally harass loyal customers with "please stay" emails.

### 3. Hyperparameter Tuning (GridSearchCV)
Instead of guessing, we used a grid search to find:
- **n_estimators:** The optimal number of trees.
- **max_depth:** How deep the "logic branches" of our trees should go.
- **learning_rate:** The speed at which Gradient Boosting corrects itself.

### 4. Categorical Encoding
Machines can't read words like "Month-to-month". We used **One-Hot Encoding** to convert categorical text labels into a series of `0` and `1` columns, allowing the math to perform mathematical distance/split calculations.
