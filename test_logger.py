from src.logger import get_logger
from src.custom_exception import CustomException
import sys


logger  = get_logger(__name__)

def divide_numbers(a, b):
    try:
        result = a / b
        logger.info("Dividing two numbers")
        return result
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Custom Error Zero", sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting main program")
        result = divide_numbers(10, 0)
    except CustomException as ce:
        logger.error(f"Custom Exception: {str(ce)}")