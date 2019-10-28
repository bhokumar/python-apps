class Card:

    allowed_suits = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suite}"
