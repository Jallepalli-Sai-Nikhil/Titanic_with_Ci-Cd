import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import logging

# Setup logging
logging.basicConfig(
    filename="logs/modeling.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def train_model():
    try:
        logging.info("Starting model training...")
        data = pd.read_csv("data/processed/train_processed.csv")
        X = data.drop("Survived", axis=1)
        y = data["Survived"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, "models/model.pkl")
        logging.info("Model saved to 'models/model.pkl'.")

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logging.info(f"Model training completed with accuracy: {accuracy:.2f}")
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        raise

if __name__ == "__main__":
    train_model()
