# Exploratory Data Analysis (EDA) Summary

## Dataset Overview
- Raw data: Insurance dataset (.txt, >500MB, excluded from Git)
- Sample used for EDA: 50,000 records
- Data format: Pipe-separated text file
- Columns: Customer, vehicle, policy, premium, and claim attributes

## Data Cleaning & Quality
- Initial load revealed delimiter parsing issues, resolved by explicitly using `|`
- Date fields contained inconsistent formats and were parsed robustly
- Numeric columns required coercion due to mixed types
- Records with zero or negative premiums were excluded from loss ratio analysis

## Key Metric
- Loss Ratio = TotalClaims / TotalPremium
- Over 75% of policies have zero claims
- Loss ratio distribution is highly right-skewed with extreme outliers

## Key Insights
1. Loss ratios vary noticeably across provinces, indicating geographic risk differences
2. Monthly total claims show temporal trends suggesting seasonality
3. Claim severity differs across customer demographics such as gender

## Visualizations
- Average Loss Ratio by Province
- Monthly Total Claims Trend
- Average Claim Severity by Gender

