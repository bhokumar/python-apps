from scrapy import scrape_quotes
from csv import DictWriter


def write_quotes(all_quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in all_quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)