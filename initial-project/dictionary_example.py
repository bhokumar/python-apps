cat = {'name': 'blue', 'age': 3.5, 'isCute': True}

print(cat)

for v in cat.keys():
    print(v)

for v in cat.values():
    print(v)

for k, v in cat.items():
    print(f"{k} and value is {v}")