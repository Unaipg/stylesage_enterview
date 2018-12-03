"""Decorators from the products module"""
from functools import wraps
import time

def timer():
    def timer_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            """Print the elapsed time with an optional message."""
            message = kwargs.get('message', '')
            starting_time = time.time()
            result = func(*args, **kwargs)
            print(f"{func.__name__} took {round(time.time() - starting_time, 4)}s to run{message}.")
            return result
        return func_wrapper
    return timer_decorator

