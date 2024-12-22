import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import logging

# Setup logging
logging.basicConfig(
    filename="logs/evaluation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def evaluate_model():
    try:
        logging.info("Starting model evaluation...")

        # Load the processed data and model
        data = pd.read_csv("data/processed/train_processed.csv")
        model = joblib.load("models/model.pkl")

        # Split data into features and target
        X = data.drop("Survived", axis=1)
        y = data["Survived"]

        # Make predictions
        y_pred = model.predict(X)

        # Calculate metrics
        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(y, y_pred)
        recall = recall_score(y, y_pred)
        f1 = f1_score(y, y_pred)

        # Log results
        logging.info(f"Accuracy: {accuracy:.2f}")
        logging.info(f"Precision: {precision:.2f}")
        logging.info(f"Recall: {recall:.2f}")
        logging.info(f"F1 Score: {f1:.2f}")
        print("Evaluation completed. Check logs/evaluation.log for details.")
    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        raise

if __name__ == "__main__":
    evaluate_model()
