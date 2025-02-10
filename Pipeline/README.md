# FastAPI Salary Prediction Model

This project contains a machine learning pipeline for predicting salaries using a FastAPI app. It includes data extraction, feature engineering, model training, and deployment.


## Overview

This project implements a machine learning pipeline to predict salaries for various job titles using FastAPI. The model is based on the **LightGBM Regressor** and the application uses FastAPI for REST API deployment.

### Main Pipeline Steps:
1. **Data Extraction:** Extract dataset from a specified source (e.g., CSV file).
2. **Feature Engineering:** Preprocess and encode categorical features.
3. **Model Training:** Train the model using LightGBM and save the trained model.
4. **Deployment:** Use FastAPI to deploy the model as an API for salary predictions.

## Features

- **Predict Salaries:** Predict salaries based on job title, experience level, company size, and other features.
- **FastAPI Backend:** Expose a REST API for salary predictions.
- **Docker Deployment:** Containerized app using Docker for easy deployment.

## Setup

### Clone the Repository

To clone the repository:

```bash
git clone https://github.com/SajaTaweel/MLOps/Pipeline.git
cd Pipeline
```

### Install Dependencies

Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

Alternatively, if you're using Docker, skip the installation and go straight to **Docker Deployment**.


## Model Training

The model training is done using **LightGBM Regressor**.

### Steps to Train the Model

1. Load the data using the `extract()` function.
2. Preprocess the data with the `preprocess_data()` function.
3. Train the model using the `train_model()` function, which saves the model to `models/model.pkl`.

## FastAPI Deployment

### Run Locally

To run the FastAPI app locally:

```bash
uvicorn main:app --reload
```

Your FastAPI app will be available at `http://localhost:8000/docs`.

### Docker Deployment

If you want to deploy the app using Docker:

1. **Build the Docker image**:

   ```bash
   docker build -t fastapi-salary-model .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8000:8000 fastapi-salary-model
   ```

The FastAPI app will be available at `http://localhost:8000/docs`.

