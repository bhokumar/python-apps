from random import random

def flip_coin():
    r = random()

    if r > .5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())