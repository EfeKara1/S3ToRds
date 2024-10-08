import os

class Config:
    # S3 Configuration
    S3_BUCKET = os.getenv('S3_BUCKET', 'your-bucket-name')
    S3_FILE_KEY = os.getenv('S3_FILE_KEY', 'iris.csv')
    LOCAL_FILE_PATH = os.getenv('LOCAL_FILE_PATH', '/tmp/iris.csv')

    # RDS Configuration
    RDS_HOST = os.getenv('RDS_HOST', 'your-rds-endpoint')
    RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Use 5432 for PostgreSQL
    RDS_DB_NAME = os.getenv('RDS_DB_NAME', 'your-database-name')
    RDS_USER = os.getenv('RDS_USER', 'your-username')
    RDS_PASSWORD = os.getenv('RDS_PASSWORD', 'your-password')

    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

