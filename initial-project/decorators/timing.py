from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing function {fn.__name__}")
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums():
    return sum(x for x in range(9000000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(9000000000)])


print(sum_nums())
print(sum_nums_list())

