import yaml
from logger import logger
from extract import extract
from pydantic import BaseModel
from fastapi import FastAPI
from feature_engineering import preprocess_data
from model_training import train_model
from inference import predict_salary
import uvicorn

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Define FastAPI app
app = FastAPI(title="Salary Prediction API", version="1.0")

# Define input schema for FastAPI

class SalaryInput(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary_currency: str
    salary_in_usd: int
    employee_residence: str
    remote_ratio: int
    company_location: str
    company_size: str

@app.post("/predict")
def predict(input_data: SalaryInput):
    """API endpoint for salary prediction."""
    input_dict = input_data.dict()
    prediction = predict_salary(input_dict)
    return {"predicted_salary": prediction}

def main():
    try:
        logger.info("Starting pipeline...")

        # Extract data
        df = extract(config["dataset"])
        print(df.info)

        # Preprocess data
        X, y = preprocess_data(df)

        # Train model
        model = train_model(X, y)

        logger.info("Pipeline completed successfully!")

        # Run FastAPI server
        uvicorn.run(app, host="0.0.0.0", port=8000)

    except Exception as e:
        logger.error(f"Failed in the pipeline process: {e}")

if __name__ == "__main__":
    main()
