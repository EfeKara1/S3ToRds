from sqlalchemy import create_engine, text
import pandas as pd
from config import Config
import logging

logger = logging.getLogger(__name__)

def create_db_engine():
    """Create a SQLAlchemy engine to connect to the RDS database."""
    engine = create_engine(f"mysql+pymysql://{Config.RDS_USER}:{Config.RDS_PASSWORD}@{Config.RDS_HOST}:{Config.RDS_PORT}/{Config.RDS_DB_NAME}")
    return engine

def create_iris_table(engine):
    """Create the Iris table if it doesn't exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Iris (
        sepal_length FLOAT,
        sepal_width FLOAT,
        petal_length FLOAT,
        petal_width FLOAT,
        species VARCHAR(50)
    );
    """
    with engine.connect() as connection:
        connection.execute(text(create_table_query))
        logger.info("Iris table created or already exists.")

def insert_data_to_rds(df, engine):
    """Insert the Iris dataset into the RDS table."""
    try:
        df.to_sql('Iris', con=engine, if_exists='append', index=False)
        logger.info("Data inserted successfully into RDS.")
    except Exception as e:
        logger.error(f"Error inserting data into RDS: {e}")
        raise

