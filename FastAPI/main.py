import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model import SalaryPredictor


class Features(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary_currency: str
    employee_residence: str
    remote_ratio: int
    company_location: str
    company_size: str


# Initialize the FastAPI app and the SalaryPredictor
app = FastAPI()
predictor = SalaryPredictor()

# Load data, preprocess, and train the model
predictor.load_data(
    "C:/Users/Laptop/Documents/AI&data science/extra courses/Improved/MLOps/Task2/DataScience_salaries_2024.csv")
predictor.preprocess_data()
predictor.train()


# Define the root endpoint
@app.get("/")
def index():
    return {"message": "Salary Prediction API"}


# Define the prediction endpoint
@app.post("/salary/predict")
def predict_salary(features: Features):
    try:
        # Convert the input features to a DataFrame
        input_data = pd.DataFrame([features.dict()])

        # Ensure correct order of columns, and exclude 'salary' as it's not needed for prediction
        input_data = input_data[['work_year', 'experience_level', 'employment_type',
                                  'job_title', 'salary_currency', 'employee_residence',
                                  'remote_ratio', 'company_location', 'company_size']]

        # Predict the salary using the model
        predicted_salary = predictor.predict(input_data)
        return {"predicted_salary": predicted_salary}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
