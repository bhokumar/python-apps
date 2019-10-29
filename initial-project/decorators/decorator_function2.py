def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper


def greet(name):
    return f"Hi I'm {name}"


