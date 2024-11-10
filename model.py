import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class SalaryPredictor:
    def __init__(self):
        self.model = LGBMRegressor(random_state=42, n_jobs=-1, n_estimators=1000)
        self.label_encoders = {}

    def load_data(self, filepath):
        self.data = pd.read_csv(filepath, index_col=0)
        print(self.data.columns)

    def preprocess_data(self):
        categorical_cols = ['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size']
        for col in categorical_cols:
            le = LabelEncoder()
            self.data[col] = le.fit_transform(self.data[col])
            self.label_encoders[col] = le

        self.X = self.data.drop('salary_in_usd', axis=1)
        self.y = self.data['salary_in_usd']

    def train(self):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def encode_features(self, features):
        for col in ['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size']:
            if col in features.columns:
                features[col] = self.label_encoders[col].transform(features[col])
        return features

    def predict(self, features):
        features = self.encode_features(features)
        return float(self.model.predict(features)[0])
