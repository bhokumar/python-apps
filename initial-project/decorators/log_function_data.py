def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are abou to call {fn.__name__}")
        print(f"Here is the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    return x + y

print(add(10, 20))