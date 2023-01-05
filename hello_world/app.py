from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(log_uncaught_exceptions=True)

def lambda_handler(event: dict, context: LambdaContext) -> str:
    logger.error("This will create a structured log")
    
    raise(Exception("This will create a unstructured log"))
