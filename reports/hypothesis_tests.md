# Task 3 – Hypothesis Testing Report

This report presents the results of statistical hypothesis testing conducted to evaluate risk differences across customer, geographic, and policy attributes. The objective is to validate whether observed variations in claims and profitability metrics are statistically significant and actionable for insurance decision-making.


## 1. Overview of Hypotheses

The following hypotheses were tested:

1. **Geographic risk (Province):**
   - H₀: Claim frequency is the same across all provinces.
   - H₁: Claim frequency differs across provinces.

2. **Customer demographics (Gender):**
   - H₀: Claim frequency and claim severity do not differ by gender.
   - H₁: Claim frequency and/or severity differ by gender.

3. **Profitability (Margin):**
   - H₀: Average margin (TotalPremium − TotalClaims) is not significantly different from zero.
   - H₁: Average margin is significantly different from zero.

All tests were conducted at a 5% significance level (α = 0.05).

## 2. Data and Metrics

- **Dataset:** Historical car insurance data in `.txt` format (>500MB), tracked using DVC.
- **Processing approach:** Chunk-based processing was used for full-dataset analyses to ensure scalability.
- **Key derived metrics:**
  - Claim Frequency: Indicator variable (HasClaim = TotalClaims > 0)
  - Claim Severity: TotalClaims for policies with claims
  - Margin: TotalPremium − TotalClaims

## 3. Hypothesis Test Results

### 3.1 Province vs Claim Frequency

**Test used:** Chi-square test of independence  
**Reason:** Claim frequency is a binary categorical variable, and Province is categorical.

To handle the full dataset efficiently, policy counts and claim counts were aggregated by province using chunk-based reading.

**Result:**
- Chi-square test p-value = **5.93 × 10⁻¹⁹**

**Decision:**
- Reject H₀

**Conclusion:**
Claim frequency differs significantly across provinces.

**Business implication:**
Geographic location is a strong risk factor. Provinces with higher claim frequencies may require adjusted pricing, stricter underwriting, or targeted risk management strategies.

### 3.2 Gender vs Claims

#### 3.2.1 Claim Frequency by Gender

**Test used:** Chi-square test of independence

**Result:**
- p-value < 0.05

**Conclusion:**
Claim frequency differs significantly by gender.

#### 3.2.2 Claim Severity by Gender

**Test used:** Mann–Whitney U test  
**Reason:** Claim severity is non-normally distributed and contains extreme outliers.

**Result:**
- p-value < 0.05

**Conclusion:**
Claim severity among policyholders with claims differs between genders.

**Business implication:**
Gender-based differences in both claim probability and severity suggest potential value in demographic segmentation, subject to regulatory and ethical considerations.

### 3.3 Margin Analysis

**Metric:** Margin = TotalPremium − TotalClaims

**Test used:** Wilcoxon signed-rank test  
**Reason:** Margin is not normally distributed.

**Result:**
- p-value < 0.05

**Conclusion:**
The average margin is significantly different from zero.

**Business implication:**
The insurance portfolio is statistically profitable overall, but margin variability indicates the need for more granular pricing strategies.

## 4. Multiple Testing Considerations

Where multiple group comparisons were explored, p-values were adjusted using the Benjamini–Hochberg False Discovery Rate (FDR) method to control for Type I error inflation.

## 5. Limitations

- Some variables (e.g., PostalCode) have high cardinality, limiting interpretability without further aggregation.
- Hypothesis testing identifies association, not causation.
- Potential confounding factors (vehicle age, policy type, coverage level) were not controlled for in simple tests and should be addressed using multivariate models.

## 6. Summary 

This task confirms statistically significant differences in risk and profitability across geographic and demographic dimensions. The results justify moving forward to predictive modeling.

