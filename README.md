# Loan

The Loan Prediction model is a machine learning model that uses various techniques to predict the likelihood of loan repayment and is deployed as a web application using the Streamlit framework. It can be used by financial institutions to make informed decisions on loan approvals. However, it should be noted that the model should be trained on a diverse dataset and used as a tool to assist in decision making, not as the sole determining factor.

## Overview
This project aims to predict loan approval decisions using various machine learning algorithms. The objective is to accurately classify loan applications as approved or rejected based on historical data and applicant features. Multiple classification models are evaluated to determine the most effective algorithm for this task.

## Dataset
The dataset contains records of loan applications with various features that influence the approval decision. The target variable indicates whether a loan application was approved.

##Models Evaluated

Logistic Regression (LR)
Training Accuracy: 83.11%
Training F1-Score: 0.890
Testing Accuracy: 81.71%
Testing F1-Score: 0.880

Support Vector Machine (SVM)
Training Accuracy: 83.69%
Training F1-Score: 0.892
Testing Accuracy: 80.52%
Testing F1-Score: 0.871

K-Nearest Neighbors (KNN)
Training Accuracy: 86.67%
Training F1-Score: 0.904
Testing Accuracy: 78.15%
Testing F1-Score: 0.844

Decision Tree Classifier (CART)
Training Accuracy: 100%
Training F1-Score: 1.000
Testing Accuracy: 75.76%
Testing F1-Score: 0.823

Random Forest Classifier (RF)
Training Accuracy: 100%
Training F1-Score: 1.000
Testing Accuracy: 81.24%
Testing F1-Score: 0.872

Gradient Boosting Classifier (GB)
Training Accuracy: 93.40%
Training F1-Score: 0.955
Testing Accuracy: 80.28%
Testing F1-Score: 0.865

Extreme Gradient Boosting (XGBoost)
Training Accuracy: 99.97%
Training F1-Score: 0.999
Testing Accuracy: 81.23%
Testing F1-Score: 0.870

Gaussian Naive Bayes (GNB)
Training Accuracy: 83.85%
Training F1-Score: 0.896
Testing Accuracy: 83.85%
Testing F1-Score: 0.897

AdaBoost Classifier (ABC)
Training Accuracy: 87.99%
Training F1-Score: 0.918
Testing Accuracy: 81.23%
Testing F1-Score: 0.873

## Key Findings
Gaussian Naive Bayes (GNB) achieved the highest testing accuracy (83.85%) and demonstrated a strong performance with a high F1-score.
Logistic Regression and Gradient Boosting also performed well, balancing both accuracy and F1-score.
Decision Tree and Random Forest showed high training accuracy but lower generalizability on the test set, indicating potential overfitting.

Conclusion
The Gaussian Naive Bayes model emerged as the most effective algorithm for predicting loan approvals, offering a balanced performance in terms of accuracy and F1-score. This model can assist financial institutions in making informed loan approval decisions. tuned Gaussian Naive Bayes model achieved 89.68% accuracy.

##A video summarizing what I did in the code : 
https://drive.google.com/file/d/13Juk5yWc3O3WW45h-7TAfDLHhQNT4_So/view
