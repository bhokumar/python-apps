from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go Away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))