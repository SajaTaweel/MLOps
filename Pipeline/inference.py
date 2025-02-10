import pickle
import pandas as pd
import yaml

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Load trained model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoders
with open("models/encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# Function to preprocess input data
def preprocess_input(data: dict):
    df = pd.DataFrame([data])

    for col in config["categorical_cols"]:
        if col in df.columns and col in label_encoders:
            df[col] = label_encoders[col].transform([df[col][0]])  # Encode single value

    return df

#  Function to make predictions
def predict_salary(data: dict):
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)[0]  # Get single prediction
    return round(float(prediction), 2)  # Round for readability
