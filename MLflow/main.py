import mlflow
import mlflow.sklearn
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score


def prepare_data(dataset, encoder):
    df = pd.read_csv(dataset)

    df = pd.get_dummies(df, columns=["sex", "smoker"])
    df["region"] = encoder.fit_transform(df["region"])

    X = df.drop("charges", axis=1)
    y = df["charges"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test


def save_predictions(model_name, y_test, pred):
    """ Save actual and predicted values for offline evaluation """
    with open(f"{model_name}_pred.pkl", "wb") as f:
        pickle.dump((y_test.tolist(), pred.tolist()), f)


def load_predictions(model_name):
    """ Load actual and predicted values for offline evaluation """
    with open(f"{model_name}_pred.pkl", "rb") as f:
        y_test, pred = pickle.load(f)
    return y_test, pred


def train_model(X_train, X_test, y_train, y_test, model_name):
    with mlflow.start_run(run_name=model_name):
        if model_name == "Linear Regression":
            model = LinearRegression()
        elif model_name == "Random Forest":
            model = RandomForestRegressor(n_estimators=300, max_depth=6, random_state=42)
        elif model_name == "Xgb":
            model = XGBRegressor(n_estimators=50, learning_rate=0.1, max_depth=6, random_state=42)
        elif model_name == "Catboost":
            model = CatBoostRegressor(n_estimators=150, learning_rate=0.1, verbose=0, random_state=42)
        else:
            print("Model not found")
            return None

        model.fit(X_train, y_train)
        pred = model.predict(X_test)

        # Evaluate and log metrics
        r2, mse = evaluate_model(pred, y_test)
        mlflow.log_param("model_name", model_name)
        mlflow.log_metric("R2_score", r2)
        mlflow.log_metric("MSE", mse)
        mlflow.sklearn.log_model(model, model_name)

        print(f"Model: {model_name} - R² Score: {r2:.2f} - MSE: {mse:.2f}")

        # Save predictions for offline evaluation
        save_predictions(model_name, y_test, pred)

        return r2, mse


def evaluate_model(pred, y_test):
    """ Compute R² Score and Mean Squared Error """
    r2 = r2_score(y_test, pred)
    mse = mean_squared_error(y_test, pred)
    return r2, mse


def offline_evaluate_model(model_name):
    """ Load predictions and log metrics without retraining """
    with mlflow.start_run(run_name=f"Offline_{model_name}"):
        y_test, pred = load_predictions(model_name)
        r2, mse = evaluate_model(pred, y_test)

        # Log offline evaluation metrics
        mlflow.log_metric("Offline_R2_score", r2)
        mlflow.log_metric("Offline_MSE", mse)

        print(f"[Offline] Model: {model_name} - R² Score: {r2:.2f} - MSE: {mse:.2f}")


if __name__ == "__main__":
    mlflow.set_experiment("InsurancePrediction")

    encoder = LabelEncoder()
    X_train, X_test, y_train, y_test = prepare_data("insurance.csv", encoder)

    models = ["Linear Regression", "Random Forest", "Xgb", "Catboost"]

    # Train and save predictions
    for model in models:
        train_model(X_train, X_test, y_train, y_test, model)

    # Offline evaluation (compare results without retraining)
    print("\nPerforming Offline Evaluation...\n")
    for model in models:
        offline_evaluate_model(model)
