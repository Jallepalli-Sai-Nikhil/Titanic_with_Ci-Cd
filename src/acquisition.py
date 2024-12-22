import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    filename="logs/acquisition.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    try:
        logging.info("Starting data acquisition...")
        train_data = pd.read_csv("data/raw/train.csv")
        test_data = pd.read_csv("data/raw/test.csv")
        logging.info("Data successfully loaded.")
        return train_data, test_data
    except Exception as e:
        logging.error(f"Error during data acquisition: {e}")
        raise

if __name__ == "__main__":
    train, test = load_data()
