import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Sample dataframe (replace this with your CSV file)
# df = pd.read_csv("your_file.csv")
data = {
    'Loan_ID': ['L1', 'L2', 'L3', 'L4'],
    'Gender': ['Male', 'Female', 'Male', 'Male'],
    'Married': ['Yes', 'No', 'Yes', 'No'],
    'Dependents': ['0', '1', '2', '0'],
    'Education': ['Graduate', 'Not Graduate', 'Graduate', 'Graduate'],
    'Self_Employed': ['No', 'Yes', 'No', 'No'],
    'ApplicantIncome': [5000, 3000, 4000, 2500],
    'CoapplicantIncome': [0, 1500, 1000, 1200],
    'LoanAmount': [150, 100, 130, 80],
    'Loan_Amount_Term': [360, 360, 360, 180],
    'Credit_History': [1.0, 0.0, 1.0, 1.0],
    'Property_Area': ['Urban', 'Rural', 'Semiurban', 'Urban']
}
df = pd.DataFrame(data)

# Drop Loan_ID (not useful)
df = df.drop(columns=['Loan_ID'])

# Target and features
X = df.drop('LoanAmount', axis=1)
y = df['LoanAmount']

# Categorical columns
categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

# Preprocessor: OneHotEncode categorical columns, keep the rest
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'  # Leave numeric columns unchanged
)

# Pipeline: preprocessing + RandomForestRegressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("Predictions:", y_pred)
print("Mean Squared Error:", mse)
