# 📈 SaaS Product Retention & Churn Prediction Dashboard

## Business-first Product Analytics Project

An end-to-end SaaS product analytics project that uses **cohort retention analysis, LTV/CAC, user health segmentation and logistic regression** to identify churn risk and support weekly product-manager decisions.

## 🎯 Business Problem

SaaS businesses need to understand why users stop engaging, which cohorts retain, whether acquisition economics are sustainable, and which users should receive proactive retention interventions.

This project analyzes **12,000 synthetic SaaS users** and their product events to answer:

- How does retention differ by signup cohort and plan?
- Which users are power users vs at-risk users?
- Is customer acquisition economics healthy through LTV/CAC?
- Which behaviors are associated with churn?
- Can a churn model prioritize users for intervention?

## 🧰 Tech Stack

- PostgreSQL / SQL
- Python, Pandas, NumPy
- Scikit-learn
- Streamlit + Plotly
- Jupyter Notebook
- Power BI-ready outputs

## 📁 Structure

```text
saas-retention-churn-dashboard/
├── data/
│   ├── saas_users_12k.csv
│   └── saas_events.csv
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── notebooks/
│   ├── saas_retention_analysis.ipynb
│   └── analysis.py
├── dashboard/
│   └── app.py
├── docs/
│   └── DASHBOARD_GUIDE.md
├── requirements.txt
└── README.md
```

## 🔍 Analysis

### 1. Cohort Retention

Users are grouped by signup month and tracked by months since signup. This produces retention curves/heatmaps that show whether newer cohorts are improving or deteriorating.

### 2. LTV/CAC

The project compares estimated lifetime value with acquisition cost to understand unit economics by plan.

### 3. Power Users vs At-Risk Users

Power users are defined using high engagement and feature adoption. At-risk users are identified using low login frequency or low feature adoption.

### 4. Churn Prediction

A logistic regression model uses behavioral features including login frequency, feature usage, support tickets, team size, API adoption and derived engagement indicators. ROC-AUC is used for evaluation because the output is a probability ranking problem.

## 💡 Product Recommendations

1. **Improve feature adoption:** users with low feature usage should receive targeted onboarding and education.
2. **Prioritize paid at-risk users:** retention teams should focus first on users with meaningful recurring revenue exposure.
3. **Monitor cohort quality:** compare Day-30/Day-60 retention across acquisition channels and plan tiers.
4. **Use LTV/CAC for growth decisions:** acquisition spend should be evaluated alongside long-term value.
5. **Use risk scores for prioritization, not automatic cancellation decisions:** thresholds should reflect the cost of false positives and false negatives.

## 🚀 Run the Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## 🐘 PostgreSQL

Create a database, run `sql/schema.sql`, import both CSV files, then run `sql/analysis.sql`.

## 📊 Suggested Power BI Dashboard

- KPI cards: Users, Churn Rate, Avg Logins, Avg Features, LTV/CAC
- Cohort retention heatmap
- Churn rate by plan
- LTV/CAC by acquisition channel
- User health segmentation
- Top at-risk user table
- Slicers for plan, region and acquisition channel

## ⚠️ Dataset Disclaimer

The dataset is synthetic and created for educational and portfolio purposes. It contains no real customer information.

## 👤 Author

**K. James Bond**

Aspiring Data Analyst / Business Analyst — IIT Madras

GitHub: https://github.com/jamesbond-iit

## 📌 Skills Demonstrated

SQL • PostgreSQL • Python • Pandas • Logistic Regression • Cohort Analysis • Churn Modeling • LTV/CAC • Product Metrics • Streamlit • Plotly • Business Recommendations
