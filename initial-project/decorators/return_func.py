from random import choice


def make_laugh_function():
    def get_laugh():
        lol = choice(('HAHAHAHA', 'LOL', 'TEHEHE'))
        return lol
    return get_laugh


laugh = make_laugh_function()
print(laugh())
