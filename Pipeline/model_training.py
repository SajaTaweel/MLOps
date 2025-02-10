import pickle
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import yaml
from logger import logger

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# 📌 Train and save model
def train_model(X, y):
    try:
        logger.info(f"Model Training...")

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=config["model_split"]["test_size"], random_state=config["model_split"]["random_state"]
        )

        # Initialize and train the model
        model = LGBMRegressor(
            random_state=config["lightgbm"]["random_state"],
            n_jobs=config["lightgbm"]["jobs"],
            n_estimators=config["lightgbm"]["estimators"]
        )
        model.fit(X_train, y_train)

        # 📌 Make predictions on test set
        y_pred = model.predict(X_test)

        # 📌 Compute accuracy (R² score)
        accuracy = r2_score(y_test, y_pred)

        logger.info(f"Model Training Complete! R² Score: {accuracy:.4f}")

        # 📌 Save trained model
        with open("models/model.pkl", "wb") as f:
            pickle.dump(model, f)

        return model

    except Exception as e:
        logger.error(f"Failed to train the model: {e}")
        raise
