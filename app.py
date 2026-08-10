import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SaaS Retention & Churn",layout="wide")
@st.cache_data
def load(): return pd.read_csv("data/saas_users_12k.csv",parse_dates=["signup_date","churn_date"])
df=load()
st.title("SaaS Product Retention & Churn Dashboard")
st.caption("Cohort retention • LTV/CAC • power users • churn risk")
plans=st.sidebar.multiselect("Plan",sorted(df.plan_tier.unique()),default=sorted(df.plan_tier.unique()))
regions=st.sidebar.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
f=df[df.plan_tier.isin(plans)&df.region.isin(regions)]
cols=st.columns(5)
cols[0].metric("Users",f"{len(f):,}")
cols[1].metric("Churn Rate",f"{100*f.churned.mean():.1f}%")
cols[2].metric("Avg Monthly Logins",f"{f.monthly_logins.mean():.1f}")
cols[3].metric("Avg Features Used",f"{f.features_used.mean():.1f}")
cols[4].metric("Avg LTV/CAC",f"{(f.estimated_ltv/f.acquisition_cost).mean():.1f}x")
left,right=st.columns(2)
plan=f.groupby("plan_tier",as_index=False).agg(users=("user_id","count"),churn_rate=("churned","mean"))
plan.churn_rate*=100
left.plotly_chart(px.bar(plan,x="plan_tier",y="churn_rate",title="Churn Rate by Plan",labels={"churn_rate":"Churn (%)"}),use_container_width=True)
seg=f.copy(); seg["status"]="Healthy"; seg.loc[(seg.monthly_logins<8)|(seg.features_used<4),"status"]="At Risk"; seg.loc[(seg.monthly_logins>=20)&(seg.features_used>=7),"status"]="Power User"
status=seg.status.value_counts().reset_index(); status.columns=["status","users"]
right.plotly_chart(px.pie(status,names="status",values="users",title="User Health Segments"),use_container_width=True)
st.subheader("Top At-Risk Users")
seg["risk_score"]=(0.45*(seg.features_used<4)+0.30*(seg.monthly_logins<8)+0.15*(seg.api_adopted==0)+0.10*seg.churned)
st.dataframe(seg.sort_values("risk_score",ascending=False)[["user_id","plan_tier","monthly_logins","features_used","api_adopted","risk_score"]].head(25),use_container_width=True,hide_index=True)
st.subheader("Product Actions")
st.markdown("- Target feature non-adopters with onboarding nudges.\n- Create save-playbooks for high-risk paid users.\n- Monitor Day-30 retention by acquisition channel and plan.\n- Use LTV/CAC to prioritize acquisition spend.\n- Review model thresholds based on the cost of false negatives vs false positives.")
