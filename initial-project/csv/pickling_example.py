import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        return f"{self.species} animal makes sound {sound}"


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"


blue = Cat("Blue", "Scottish fold", "String")

with open("pets.pickle", "wb") as file:
    pickle.dump(blue, file)


