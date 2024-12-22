import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    filename="logs/inspection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def inspect_data():
    try:
        logging.info("Starting data inspection...")
        train_data = pd.read_csv("data/raw/train.csv")
        logging.info("Train Data Info:")
        logging.info(train_data.info())
        logging.info("Train Data Description:")
        logging.info(train_data.describe())
        logging.info("Data inspection completed.")
    except Exception as e:
        logging.error(f"Error during data inspection: {e}")
        raise

if __name__ == "__main__":
    inspect_data()
