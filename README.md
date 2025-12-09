# Insurance Analytics Week 3 Project

## Project Overview
Analysis of car insurance data for AlphaCare Insurance Solutions (ACIS) to identify low-risk segments and optimize premiums.

## Objectives
1. Perform exploratory data analysis (EDA) on insurance claim data
2. Conduct A/B hypothesis testing on risk factors
3. Build predictive models for claims and premiums
4. Implement data version control with DVC

Task 1: EDA

    Analyzed insurance data
    Created 3 visualizations
    Calculated loss ratios

Task 2: DVC

    DVC installed and initialized
    Local storage configured
    Data files tracked: insurance_data_cleaned.csv
    Tested DVC pull/push functionality

Task 3: A/B Hypothesis Testing

  Tested four key hypotheses using statistical methods

  Findings:

    Rejected H₀: Risk differs significantly across provinces
    Rejected H₀: Risk differs between top postal codes
    Rejected H₀: Margins differ between postal code groups
    Gender: Claim frequency differs, but severity doesn't
    Used chi-square, t-tests, Mann-Whitney U, and logistic regression
    Business insights documented with actionable recommendations

Task 4: Statistical Modeling

    Classification Model: XGBoost for claim prediction (ROC AUC: 0.888)
    Regression Model: XGBoost for claim severity prediction (R²: 0.125)
    Premium Optimization: Built risk-based pricing formula
    Model Interpretability: SHAP analysis for feature importance
    Saved trained models and preprocessing pipelines
    Compared suggested vs actual premiums

