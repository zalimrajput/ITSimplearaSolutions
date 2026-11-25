
# AgriPak Farms - Low-Yield Risk Prediction

## Project Overview

Machine Learning internship project for AgriPak Farms.

The objective is to predict whether an agricultural field
is at risk of low yield before harvest, allowing timely
agricultural intervention.

## Week 1 Objectives

- Dataset loading and inspection
- Data cleaning and validation
- Reproducible stratified train-test split
- Logistic Regression baseline model
- Numerical feature correlation analysis
- Categorical feature association analysis
- Leakage sanity check
- Model evaluation and reporting

## Dataset Information

- Dataset: crop_data.csv
- Original records: 50000
- Cleaned records: 50000
- Removed records: 0
- Total input features: 9
- Target: low_yield_risk
- Training records: 40000
- Testing records: 10000
- Train-test ratio: 80/20
- Random state: 42

## Target Classes

- 0 = No Low-Yield Risk
- 1 = Low-Yield Risk

## Data Cleaning Decisions

- Removed 0 rows with missing or invalid target values.
- Removed 0 duplicate rows.

- Missing numerical features are imputed using the training-set median.
- Missing categorical features are imputed using the training-set mode.
- Numerical features are standardized.
- Categorical features are one-hot encoded.
- Preprocessing is fitted only on training data.

## Feature Classification

### Numerical Features

- rainfall_mm
- temperature_c
- fertilizer_used
- irrigation_used
- days_to_harvest

### Categorical Features

- region
- soil_type
- crop
- weather_condition

## Correlation and Leakage Analysis

Correlation analysis was performed using training data only.

### Numerical Features

- Method: Pearson correlation with the binary target.
- Target: low_yield_risk.

### Categorical Features

- Method: One-hot encoding followed by Pearson correlation.
- Individual category correlations were calculated.
- Feature-level association is represented by the maximum
  absolute category-level correlation.

### Leakage Investigation

- Investigation threshold: Absolute correlation > 0.9.
- No individual feature exceeding this threshold is automatically
  classified as leakage.
- High correlation alone does not establish data leakage.

No numerical or categorical feature exceeded the absolute correlation threshold of 0.90 in the training data.


### Additional Leakage Checks

- Exact train-test overlapping records: 0
- Train-test overlap check performed on complete records.
- Preprocessing is fitted using training data only.
- Test data is used only for final prediction and evaluation.

### Leakage Investigation Limitations

The following still require investigation:

- Original target-generation methodology.
- Feature availability at the intended prediction date.
- Potential temporal leakage.
- Potential field-level or farm-level overlap.

No correlation threshold or single overlap check proves
that the dataset is completely leakage-free.

### Generated Correlation Reports

- reports/all_feature_correlation.csv
- reports/categorical_correlation_details.csv
- reports/potential_leakage_features.csv
- reports/all_feature_correlation.png

## Baseline Model

Logistic Regression with:

- Numerical imputation using median.
- Numerical standardization.
- Categorical imputation using most frequent value.
- One-hot encoding for categorical features.
- Preprocessing fitted only on training data.

## Evaluation Results

| Metric | Score |
|---|---:|

| Accuracy | 0.9187 |
| Precision | 0.8884 |
| Recall | 0.8780 |
| F1 Score | 0.8832 |

Positive class: 1 (Low-Yield Risk).

## How to Run

1. Install dependencies:

   pip install -r requirements.txt

2. Open the project notebook in Google Colab.

3. Upload crop_data.csv.

4. Run all notebook cells.

5. Review generated model metrics and correlation reports.

## Project Structure

- data/raw: Original dataset
- data/processed: Cleaned dataset and train-test split
- src: Reusable source scripts
- notebooks: Project notebooks
- models: Trained baseline model
- reports: Evaluation and correlation reports

## Reproducibility

- Random state: 42
- Stratified train-test split: 80/20

## Model Limitations

This is an initial baseline model.

Further validation, feature investigation, model comparison,
and evaluation on genuinely independent agricultural data
are required before production use.
