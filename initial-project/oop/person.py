class Person:
    def __init__(self):
        self.name = "tony"
        self._secret = "Hi"
        self.__msg = "I like turtles"
        self.__lol = "HAHAHA"


person = Person()

print(person.name)
print(person._secret)
print(person._Person__lol)
