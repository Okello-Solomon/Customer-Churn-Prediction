# Customer Churn Prediction Using Logistic Regression

Live Application: [Customer Churn Prediction](https://customer-churn-prediction-gejdn7bzopuux4djprncx4.streamlit.app/)

<details> <summary><strong>View Project Details</strong></summary>

## Project Overview

Customer churn, when a customer stops using a service is a critical business challenge for companies. Accurately predicting churn allows companies to proactively retain at-risk customers and reduce revenue loss.

This project develops a machine learning pipeline to predict customer churn, addressing data imbalance and feature redundancy. The final model leverages RFE-selected features and a Bagging Logistic Regression classifier for robust performance.

### The project demonstrates a complete workflow:

Data preprocessing → Feature selection → Model training → Hyperparameter tuning → Evaluation → Model deployment.

### Dataset Summary

- Total records: 594,194 customers

- Target variable: Churn (Yes/No)

- Class distribution:

    No churn: 77.5%

    Yes churn: 22.5%

## Preprocessing

### Encoding categorical variables:

- Binary encoding for gender, Partner, Dependents, PhoneService, PaperlessBilling, and Churn

- One-hot encoding for multi-category features like InternetService, Contract, PaymentMethod, etc.

### Train-test split:

- 80% training, 20% testing

- Stratified on the Churn class to maintain distribution

### Class imbalance handling:

- SMOTE (Synthetic Minority Oversampling Technique) applied in the pipeline

- Logistic Regression weighted by class to further balance the minority class

## Feature Selection (RFE)
- Used Recursive Feature Elimination with Logistic Regression to select the top 14 predictive features.

## Modeling
- Model: Bagging Logistic Regression

- Hyperparameters (optimized via Bayesian Search):

- Pipeline includes: Standard scaling → SMOTE → Bagging Logistic Regression.

## Deployment

The trained Bagging Logistic Regression pipeline is deployed using Streamlit, allowing users to input customer and service details to receive instant churn predictions.

Feature alignment between training and deployment is strictly enforced: the model only accepts the 14 RFE-selected features in the exact same order used during training. This ensures reliable, consistent, and reproducible predictions.

The pipeline integrates scaling, SMOTE oversampling, and the Bagging classifier, making it suitable for interactive real-time predictions.

## Data Source: [Predict Customer Churn](https://www.kaggle.com/competitions/playground-series-s6e3)

</details>
