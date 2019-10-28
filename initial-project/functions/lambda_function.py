square = lambda a: a*a

print(square(10))

print(square.__name__)

squaredList = list(map(lambda a: a*a, list(range(1,10))))

print(squaredList)