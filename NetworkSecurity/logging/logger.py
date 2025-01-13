import logging
import os
from datetime import datetime

#Directory to store the logging file
LOG_FILE = "LOGS"
if not os.path.exists(LOG_FILE):
    os.makedirs(LOG_FILE)

#Configure the Logging Path
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_FILE,"network_security.logs")),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    """Get a logger instance with a given name"""
    return logging.getLogger(name)