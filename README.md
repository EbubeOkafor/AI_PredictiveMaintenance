# Predictive Maintenance using Machine Learning

This project demonstrates how machine learning can be applied to predict equipment failure before it occurs.

## Project Overview

The goal is to build a classification model that can identify whether a machine is likely to fail (`1`) or not (`0`) based on feature values.

## Dataset

Since this is a practice project, the dataset is a synthetic dataset of just 100 rows. Features include Temperature, pressure, RPm etc

## Approach

* **EDA:** Visualized feature correlations and identified class imbalance.
* **Modeling:** Trained a **Random Forest Classifier** with class balancing using SMOTE.
* **Evaluation:** Used metrics like Accuracy, Precision, Recall, F1-Score, PR AUC, and visualized the PR Curve.

## Key Findings

* **SMOTE** improved class balance.
* The model achieved satisfactory performance.
* **Feature importance** helped identify key factors influencing equipment failure.

## Deployment

Streamlit was used to build a simple web interface that allows users to input data and receive predictions.

## Future Work

* Use more detailed and realistic Dataset
* Integrate time-based features
* Explore anomaly detection techniques
