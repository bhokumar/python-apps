from functools import wraps

def my_decorator(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        pass
    return wrapper