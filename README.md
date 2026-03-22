Project: Restaurant Rating Prediction

📌 Objective

Predict restaurant ratings using structured features like cost, location, services, and engagement.

📊 Dataset Features
Longitude
Latitude
Cuisines
Average Cost for two
Currency
Has Table booking
Has Online delivery
Is delivering now
Price range
Votes

👉 Target:
Aggregate rating

⚙️ Workflow
Data Cleaning
Removed null values
Dropped irrelevant columns
Feature Engineering
Created meaningful derived features
Reduced multicollinearity
Preprocessing
Encoding categorical variables
Scaling numerical features
Outlier handling

Model Building

Linear Regression
Support Vector Regression
LightGBM
XGBoost
Hyperparameter Tuning
Used Optuna for optimization

Evaluation
R² score
Cross-validation
Ensemble Learning
Stacking Regressor

📈 Results
Model
R² Score
Linear Regression 0.72
SVR 0.88
LightGBM 0.9597
XGBoost 0.9596
Stacking 0.9598
🧠 Key Insight
Boosting models performed best
Stacking gave minimal improvement
Data quality and feature engineering had the biggest impact
