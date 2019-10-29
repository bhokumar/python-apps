class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    @classmethod
    def make_sound(cls, sound):
        return f"this animal says {sound}"


class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

blue = Cat("Blue", "Cat", "Scottish fold", "String")

print(blue)
print(blue.species)


#print(Cat().make_sound("Meow"))
