import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, classification_report

df=pd.read_csv("data/saas_users_12k.csv",parse_dates=["signup_date","churn_date"])
df["feature_non_adoption"]=(df.features_used<4).astype(int)
df["low_login_frequency"]=(df.monthly_logins<8).astype(int)
df["ltv_cac_ratio"]=df.estimated_ltv/df.acquisition_cost
print(df.groupby("plan_tier").agg(users=("user_id","count"),churn_rate=("churned","mean"),avg_ltv=("estimated_ltv","mean"),avg_cac=("acquisition_cost","mean"),ltv_cac=("ltv_cac_ratio","mean")))
features=["monthly_logins","features_used","support_tickets","team_size","api_adopted","feature_non_adoption","low_login_frequency"]
X=df[features]; y=df.churned
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model=Pipeline([("scale",StandardScaler()),("logit",LogisticRegression(max_iter=1000))])
model.fit(Xtr,ytr); p=model.predict_proba(Xte)[:,1]
print("AUC:",round(roc_auc_score(yte,p),3))
coef=pd.Series(model.named_steps["logit"].coef_[0],index=features).sort_values(key=abs,ascending=False)
print(coef)
df["churn_risk_score"]=model.predict_proba(X)[:,1]
df[["user_id","churn_risk_score"]].sort_values("churn_risk_score",ascending=False).head(100).to_csv("docs/top_100_at_risk_users.csv",index=False)
