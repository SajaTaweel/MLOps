# **Insurance Charges Prediction with MLflow**  

This project aims to predict insurance charges using different regression models while tracking and comparing their performance with **MLflow**. The models used include:  

- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**  
- **CatBoost Regressor**  

## **📌 Features**  
✔ Data preprocessing with one-hot encoding and label encoding  
✔ Model training and evaluation (R² Score & MSE)  
✔ MLflow integration for experiment tracking  
✔ Offline evaluation for comparison  

## **📌 Setup & Installation**  

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
2. Run the MLflow tracking server (Optional):  
   ```bash
   mlflow ui
   ```  
   Open **http://localhost:5000** to visualize results.  

3. Run the model training script:  
   ```bash
   python main.py
   ```  
