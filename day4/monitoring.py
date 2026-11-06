from functools import wraps
import time
from functools import wraps
from venv import logger

from Lib import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("monitoring.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            logger.info(f"Starting {func.__name__} with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            logger.info(f"Completed {func.__name__} in {elapsed_time:.4f} seconds")
            return result
        except Exception as e:
            logger.error(f"Error occurred while executing {func.__name__}: {e}")
            raise
        finally:
            end_time = time.time()
            elapsed_time = end_time - start_time
            logger.info(f"Execution of {func.__name__} finished in {elapsed_time:.4f} seconds")
    return wrapper

@monitor
def process_data(data):
    return (sum(range(data)))

result =(process_data(10000000))
print(f"Result of processing data: {result}")