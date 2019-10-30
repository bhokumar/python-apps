from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs["role"] == "admin":
            return fn(args, kwargs)
        return "Unauthorized"
    return wrapper
