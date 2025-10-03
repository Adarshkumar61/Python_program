import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Father Name': ['Tom', 'Jack', 'Sam', 'Max'],
    'Address': ['Delhi', 'Mumbai', 'Pune', 'Chennai'],
    'Joining Date': ['2021-05-12', '2020-03-10', '2022-01-15', '2019-07-23'],
    'Data': ['A', 'B', 'A', 'C'],
    'Target': [1, 0, 1, 0]  # Your output class
}

df = pd.DataFrame(data)

# Convert 'Joining Date' to datetime
df['Joining Date'] = pd.to_datetime(df['Joining Date'])

# Extract useful date features
df['Join_Year'] = df['Joining Date'].dt.year
df['Join_Month'] = df['Joining Date'].dt.month
df['Join_Day'] = df['Joining Date'].dt.day

# Drop raw date and non-useful name fields (optional if you think they carry no info)
df = df.drop(columns=['Name', 'Father Name', 'Joining Date'])

# Define features and target
X = df.drop('Target', axis=1)
y = df['Target']

# Categorical columns (you can tune based on actual data)
categorical_cols = ['Address', 'Data']

# Column transformer to apply OneHotEncoding to categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'  # Pass the rest of the columns (numerical) unchanged
)

# Pipeline with preprocessing + model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
