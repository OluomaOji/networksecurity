import sys
from NetworkSecurity.logging.logger import get_logger

logger = get_logger(__name__)

class NetworkSecurityException(Exception):
    """ Basic Exception for all the other errors raised in this project"""
    def __init__(self,message=None,errors=None):
        super().__init__(message)
        self.errors=errors
        if message:
            #Log the Error Message
            logger.error(message)
        if errors:
            #Log the Error Details
            logger.error(errors)

class DataLoadingException(NetworkSecurityException):
    """Exception raised in the Data Ingestion Process"""
    def __init__(self, message="Error occured during the Data Loading Process", errors=None):
        super().__init__(message, errors)

class DataIngestionException(NetworkSecurityException):
    """Exception raised in the Data Ingestion Process"""
    def __init__(self, message="Error occured during the Data Ingestion Process", errors=None):
        super().__init__(message, errors)

class DataTransformationException(NetworkSecurityException):
    """Exception raised in the Data Transformation Process"""
    def __init__(self, message="Error occured during the Data Transformation Process", errors=None):
        super().__init__(message, errors)

class DataValidationException(NetworkSecurityException):
    """Exception raised in the Feature Engineering Process"""
    def __init__(self, message="Error occured during the Data Validation Process", errors=None):
        super().__init__(message, errors)

class ModelTrainerException(NetworkSecurityException):
    """Exception raised in the Model Trainer Process"""
    def __init__(self, message="Error occured during the Model Trainer Process", errors=None):
        super().__init__(message, errors)

class PipelineException(NetworkSecurityException):
    """Exception raised in the Pipeline Process"""
    def __init__(self, message="Error occured during the Pipeline Process", errors=None):
        super().__init__(message, errors)