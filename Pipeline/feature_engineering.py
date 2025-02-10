from sklearn.preprocessing import LabelEncoder
import pickle
import yaml
from logger import logger


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


# Define function to preprocess data
def preprocess_data(df):
    try:
        logger.info(f"Data Preprocessing...")
        # Define categorical columns
        categorical_cols = config["categorical_cols"]
        # Initialize encoders dictionary
        label_encoders = {}

        # Encode categorical variables
        for col in categorical_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

        # Split features and target
        X = df.drop('salary_in_usd', axis=1)
        y = df['salary_in_usd']

        # Save encoders
        with open("models/encoders.pkl", "wb") as f:
            pickle.dump(label_encoders, f)

        return X, y

    except Exception as e:
        logger.error(f"Failed to preprocess the data: {e}")
        raise



