import pandas as pd
import logging
from s3_handler import download_file_from_s3
from rds_handler import create_db_engine, create_iris_table, insert_data_to_rds
from config import Config
from utils import setup_logging

# Set up logging
setup_logging(Config.LOG_LEVEL)
logger = logging.getLogger(__name__)

def run_pipeline():
    """Main function to run the data pipeline from S3 to RDS."""
    try:
        # Step 1: Download the file from S3
        download_file_from_s3()

        # Step 2: Load the data into a pandas DataFrame
        df = pd.read_csv(Config.LOCAL_FILE_PATH)
        logger.info("Data loaded successfully into pandas DataFrame.")

        # Step 3: Create a connection to the RDS database
        engine = create_db_engine()

        # Step 4: Create the Iris table in RDS (if not exists)
        create_iris_table(engine)

        # Step 5: Insert the data into the RDS database
        insert_data_to_rds(df, engine)

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()

