class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @classmethod
    def display_active_users(cls):
        print(cls)

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

    def __repr__(self):
        return f"{self.first} is {self.age}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.first, user1.last)
print(user2.first, user2.last)

print(user2.full_name())

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user1.initials())
print(user2.initials())

print(user2.is_senior())

print(user1)

