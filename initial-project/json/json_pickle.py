import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"{self.name} is of breed {self.breed}"


c = Cat("Charles", "Tabby")


#with open("cat.json", "w") as file:
#    frozen = jsonpickle.encode(c)
#    file.write(frozen)

with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)


