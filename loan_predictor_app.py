import streamlit as st
import pandas as pd
import joblib  # or use your trained model directly
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Sample data (or load model from file if saved)
def train_model():
    data = {
        'Gender': ['Male', 'Female', 'Male', 'Male'],
        'Married': ['Yes', 'No', 'Yes', 'No'],
        'ApplicantIncome': [5000, 3000, 4000, 2500],
        'Loan_Amount_Term': [360, 360, 360, 180],
        'LoanAmount': [150, 100, 130, 80]
    }
    df = pd.DataFrame(data)
    X = df.drop('LoanAmount', axis=1)
    y = df['LoanAmount']
    categorical_cols = ['Gender', 'Married']
    numerical_cols = ['ApplicantIncome', 'Loan_Amount_Term']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
            ('num', StandardScaler(), numerical_cols)
        ]
    )

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
    model.fit(X, y)
    return model

model = train_model()  # Or load from file

# 🎨 Streamlit UI
st.title("🏦 Loan Amount Predictor")

gender = st.selectbox("Select Gender", ['Male', 'Female'])
married = st.selectbox("Married?", ['Yes', 'No'])
income = st.number_input("Applicant Income", value=4000)
term = st.number_input("Loan Amount Term (in days)", value=360)

if st.button("Predict"):
    input_data = {
        'Gender': gender,
        'Married': married,
        'ApplicantIncome': income,
        'Loan_Amount_Term': term
    }

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.success(f"💰 Predicted Loan Amount: {round(prediction[0], 2)}")
