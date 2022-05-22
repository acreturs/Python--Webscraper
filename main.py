import csv

import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3


def versuch():
    zahl = 0
    street = ""

    address_string = "123 versuch"
    # Separate the address string into parts

    # Traverse through the address parts
    for x in address_string:

        wert = isinstance(x, int)

        if wert:
            continue
        else:
            zahl = address_string[0, x - 1]
            street = address_string[x]
            break

    # Determine if the address part is the
    # house number or part of the street name


# Does anything else need to be done
# before returning the result?

# Return the formatted string


URL_seite = "https://www.amazon.de/s/ref=nb_sb_noss?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Delectronics&field-keywords=&crid=H38X7ORY4QTN&sprefix=%2Celectronics%2C70"

headers = ({
    "User-Agend": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
})

headers3 = ({
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

url_test = "https://www.amazon.de/s?k=Monitor&rh=n%3A1966060031&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"


# print(soup)

def scrapepage():
    page = requests.get(url_test, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")
    mydivs = soup.find_all("div", class_="s-main-slot s-result-list s-search-results sg-row")
    print(soup)
    print(len(mydivs))
    print(mydivs)
    print("test")


def test():
    with open("asin.csv", "a") as f:
        csv_wirter = csv.writer(f)
        csv_wirter.writerow(["dasd", "ist", "ein", "test"])


def run():
    asins = []
    # das r heißt read only
    # dadurch kann ich einfach in asin alle meine Links schreiben
    with open("asin.csv", "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            asins.append(row[0])

    print(asins)

    for i in range(len(asins)):
        URL = "https://www.amazon.de/dp/" + asins[i]

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, "lxml")

        mydivs = soup.find_all("span", {"class": "a-price-whole"})

        title = soup.find_all("span", {"id": "productTitle"})

        gefunden = mydivs[0].text.replace(",", " ")
        print(title[0].text.strip(), "Price", gefunden)


if __name__ == '__main__':
   versuch()
