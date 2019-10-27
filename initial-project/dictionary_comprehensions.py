numbers = {
    'first': 1,
    'second': 2,
    'third': 3
}

square = {k: v**2 for k, v in numbers.items()}

print(square)

num_list = [1, 2, 3, 4, 5]

num_dictionary = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}

print(num_dictionary)


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

print(answer)

answer = {k: v for k, v in person}

print(answer)

answer = dict(person)

print(answer)