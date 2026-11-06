import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def log_func_call(func):
    def wrapper(*args,**kwargs):
        logging.info(f"calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args,**kwargs)
        logging.info(f"completed {func.__name__}")
        return result
    return wrapper

@log_func_call
def add(a,b):
    return a+b

print(add(2,3))
