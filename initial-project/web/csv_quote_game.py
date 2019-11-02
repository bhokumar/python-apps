import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader


BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
    return quotes


def start_game(all_quotes):
    quote = choice(all_quotes)
    remaining_guesses = 4
    print("Here is a quote: ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        if quote["author"].lower() == guess.lower():
            print("YOU GOT IT RIGHT!")
            break

        remaining_guesses -= 1

        print_hint(remaining_guesses, quote)

    again = ''
    while again not in ('y', 'Y', 'Yes', 'yes', 'YEs', 'YES', 'n', 'N', 'no', 'No', 'NO'):
        again = input("Would you like to play again (y/n)?: ")
    if again.lower() in ('y', 'Y', 'Yes', 'yes', 'YEs', 'YES'):
        print("OK You play again...")
        return start_game(all_quotes)
    else:
        print("OK, GOODBYE!")


def print_hint(remaining_guesses, quote):
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here is a hint: The Author was born in {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The Author first name starts with {quote['author'][0]} ")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(f"Here's a hint: The Author last name starts with {last_initial} ")
    else:
        print(f"Sorry ran out of guesses, The correct answer was {quote['author']}")


print("GAME IS BOOTING UP...")
quotes_all = read_quotes("quotes.csv")
start_game(quotes_all)
