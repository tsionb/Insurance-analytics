# Task 4 – Predictive Modeling Summary

This report summarizes the predictive modeling work carried out to estimate insurance risk and support data-driven pricing and underwriting decisions. Two complementary models were developed: a claim frequency model and a claim severity model.


## 1. Objective

The main objectives of Task 4 are:

- To predict the probability that a policy will result in a claim (frequency modeling)
- To estimate the expected claim size for policies with claims (severity modeling)
- To demonstrate how predictive modeling can support risk-based pricing and portfolio optimization

## 2. Data Preparation and Feature Engineering

### 2.1 Target Variables

Two separate targets were defined:

- **Claim Frequency**
  - Target: `HasClaim` (binary)
  - Definition: 1 if `TotalClaims > 0`, else 0

- **Claim Severity**
  - Target: `TotalClaims`
  - Applied transformation: `log1p(TotalClaims)` to reduce skewness

### 2.2 Feature Selection

The following features were used:

**Numerical Features**
- VehicleAge
- LogSumInsured
- CalculatedPremiumPerTerm

**Categorical Features**
- Province
- Gender
- VehicleType

High-cardinality variables (e.g., PostalCode, Model) were excluded to avoid sparsity and overfitting.


### 2.3 Preprocessing Pipeline

A unified preprocessing pipeline was built using `scikit-learn`:

- Numerical variables:
  - Median imputation
  - Standard scaling

- Categorical variables:
  - Missing value imputation ("MISSING")
  - One-hot encoding with unseen-category handling

This ensured consistent preprocessing during training and inference.

## 3. Model Development

### 3.1 Claim Frequency Model

**Model type:** Binary Classification  
**Algorithms tested:**
- Logistic Regression (baseline)
- XGBoost Classifier (final model)

**Evaluation Metrics:**
- ROC-AUC
- Precision / Recall
- Confusion Matrix

**Outcome:**
- XGBoost outperformed Logistic Regression
- The model successfully differentiated high-risk and low-risk policies

### 3.2 Claim Severity Model

**Model type:** Regression (claims > 0 only)  
**Algorithm used:** XGBoost Regressor  

**Target Handling:**
- Log-transformed target to reduce extreme skew
- Predictions back-transformed using `expm1`

**Evaluation Metrics:**
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

**Outcome:**
- RMSE and MAE showed reasonable error magnitudes given claim variability
- Low R² was expected due to the stochastic nature of insurance losses

## 4. Model Interpretation

- Province and VehicleType were among the most influential features in both models
- Premium-related variables contributed strongly to severity prediction
- Results aligned with findings from Task 3 hypothesis testing

## 5. Business Implications

- Claim frequency predictions can be used for:
  - Risk-based pricing
  - Underwriting rules
  - Customer segmentation

- Claim severity predictions support:
  - Expected loss estimation
  - Reinsurance planning
  - Capital allocation

Together, the two models form a foundational **pricing and risk engine**.

## 6. Limitations

- No temporal validation was applied
- High-cardinality features were excluded
- External risk factors (e.g., weather, traffic density) were not included

These can be addressed in future iterations.

## 7. Conclusion

Task 4 successfully demonstrates the end-to-end development of predictive insurance models. The results provide strong evidence that data-driven methods can significantly enhance risk assessment and pricing strategies at AlphaCare Insurance Solutions.

