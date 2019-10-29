def sum(n, func):
    total = 0
    for num in range(n):
        total += func(n)
    return total


def square(x):
    return x*x


def cube(x):
    return x*x*x


print(sum(10, square))
print(sum(10, cube))