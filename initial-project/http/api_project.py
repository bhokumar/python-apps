import requests
from random import choice
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKE 3000!")

print(header)

user_input = input("What would you like to search for?")

url ="https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print("There atre many jokes")
    print(choice(results))
elif num_jokes == 1:
    print("There is one joke")
    print(res["results"][0]["joke"])
else:
    print(f"There could not be joke with your term {user_input}")