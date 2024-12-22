import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import logging

# Setup logging
logging.basicConfig(
    filename="logs/preparation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def preprocess_data():
    try:
        logging.info("Starting data preparation...")
        train_data = pd.read_csv("data/raw/train.csv")
        train_data.fillna(method='ffill', inplace=True)

        # Encode categorical variables
        label_encoder = LabelEncoder()
        train_data['Sex'] = label_encoder.fit_transform(train_data['Sex'])
        joblib.dump(label_encoder, "models/encoder.pkl")
        logging.info("Categorical variables encoded.")

        # Standardize numerical variables
        scaler = StandardScaler()
        train_data[['Age', 'Fare']] = scaler.fit_transform(train_data[['Age', 'Fare']])
        joblib.dump(scaler, "models/scaler.pkl")
        logging.info("Numerical variables standardized.")

        train_data.to_csv("data/processed/train_processed.csv", index=False)
        logging.info("Processed data saved to 'data/processed/train_processed.csv'.")
    except Exception as e:
        logging.error(f"Error during data preparation: {e}")
        raise

if __name__ == "__main__":
    preprocess_data()
