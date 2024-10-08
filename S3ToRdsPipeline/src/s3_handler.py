import boto3
import logging
from botocore.exceptions import ClientError
from config import Config

logger = logging.getLogger(__name__)

def download_file_from_s3():
    """Download the iris.csv file from the specified S3 bucket."""
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(Config.S3_BUCKET, Config.S3_FILE_KEY, Config.LOCAL_FILE_PATH)
        logger.info(f"File downloaded successfully from S3: {Config.S3_FILE_KEY}")
    except ClientError as e:
        logger.error(f"Failed to download file from S3: {e}")
        raise
