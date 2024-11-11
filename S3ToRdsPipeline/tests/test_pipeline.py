import pytest
from src.s3_handler import download_file_from_s3
from src.rds_handler import create_db_engine, create_iris_table, insert_data_to_rds

def test_s3_download(mocker):
    mocker.patch('boto3.client')
    download_file_from_s3()

def test_rds_connection():
    engine = create_db_engine()
    assert engine is not None

def test_table_creation(mocker):
    engine = create_db_engine()
    create_iris_table(engine)
    # Add assertions if needed

def test_data_insertion(mocker, data_frame):
    engine = create_db_engine()
    insert_data_to_rds(data_frame, engine)

