class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        return self._age

    def full_name(self):
        return f"{self.first} {self.last}"

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = new_age

    @property
    def age(self):
        return self._age


class Moderator(Human):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community}"

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active user"

print(Moderator.display_active_mods())

