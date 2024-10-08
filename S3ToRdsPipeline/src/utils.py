import logging

def setup_logging(log_level='INFO'):
    """Set up logging configuration."""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=getattr(logging, log_level.upper(), logging.INFO)
    )
