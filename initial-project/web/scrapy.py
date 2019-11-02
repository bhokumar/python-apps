import requests
from bs4 import BeautifulSoup


BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for q in quotes:
            all_quotes.append({
                "text": q.find(class_="text").get_text(),
                "author": q.find(class_="author").get_text(),
                "bio-link": q.find("a")["href"]
            })

        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None
    return all_quotes


