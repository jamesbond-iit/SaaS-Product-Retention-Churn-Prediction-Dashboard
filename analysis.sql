-- 01_retention_overview.sql
SELECT plan_tier, COUNT(*) users, ROUND(100.0*AVG(churned),2) churn_rate, ROUND(AVG(monthly_logins),2) avg_logins, ROUND(AVG(features_used),2) avg_features FROM saas_users GROUP BY plan_tier ORDER BY churn_rate;

-- 02_ltv_cac.sql
SELECT plan_tier, ROUND(AVG(estimated_ltv),2) avg_ltv, ROUND(AVG(acquisition_cost),2) avg_cac, ROUND(AVG(estimated_ltv)/NULLIF(AVG(acquisition_cost),0),2) ltv_cac_ratio FROM saas_users GROUP BY plan_tier;

-- 03_power_vs_risk.sql
SELECT CASE WHEN monthly_logins>=20 AND features_used>=7 THEN 'Power User' WHEN monthly_logins<8 OR features_used<4 THEN 'At Risk' ELSE 'Healthy' END user_status, COUNT(*) users, ROUND(100.0*AVG(churned),2) churn_rate FROM saas_users GROUP BY 1 ORDER BY churn_rate DESC;

-- 04_feature_nonadoption.sql
SELECT api_adopted, COUNT(*) users, ROUND(100.0*AVG(churned),2) churn_rate FROM saas_users GROUP BY api_adopted ORDER BY api_adopted;

-- 05_cohort_retention.sql
WITH cohort AS (SELECT user_id, DATE_TRUNC('month',signup_date)::date cohort_month FROM saas_users), activity AS (SELECT DISTINCT user_id, DATE_TRUNC('month',event_date)::date active_month FROM saas_events), joined AS (SELECT c.cohort_month,c.user_id,EXTRACT(month FROM age(a.active_month,c.cohort_month))::int month_number FROM cohort c JOIN activity a USING(user_id) WHERE a.active_month>=c.cohort_month) SELECT cohort_month,month_number,COUNT(DISTINCT user_id) active_users FROM joined GROUP BY 1,2 ORDER BY 1,2;

-- 06_window_functions.sql
SELECT user_id, event_date, event_type, LAG(event_date) OVER(PARTITION BY user_id ORDER BY event_date) previous_event, event_date-LAG(event_date) OVER(PARTITION BY user_id ORDER BY event_date) days_since_previous FROM saas_events;