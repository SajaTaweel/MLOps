
## Overview

This project contains the following key components:

### 1. **ETL Pipeline with PostgreSQL**:
   - Extract, Transform, and Load (ETL) operations to handle data ingestion, cleaning, and processing.
   - Data is stored in a PostgreSQL database for easy access and analysis.

### 2. **FastAPI**:
   - A FastAPI application for serving the trained salary prediction model.
   - The API handles HTTP requests, performs data preprocessing, and returns salary predictions.

### 3. **Docker**:
   - Dockerization of the FastAPI application to ensure easy deployment and scalability.
   - Includes a Dockerfile and instructions to run the FastAPI app within a Docker container.

### 4. **MLflow**:
   - Model tracking with **MLflow** to log experiments, parameters, metrics, and models.
   - MLflow allows you to manage models throughout their lifecycle, from experimentation to deployment.
   - Tracks the performance of different models and hyperparameters.



