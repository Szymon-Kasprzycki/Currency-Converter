# Script gives possibility to get real time exchange rates
# Made by Szymon Kasprzycki
# Educational project, not to use
# v1.0.0

import requests
from bs4 import BeautifulSoup

# Get data from website
def get_data(amount, base, to):
    if "," in amount:
        amount = amount.replace(",", ".")
    if amount is float:
        amount = round(amount, 2)
    if len(base) != 3 or len(to) != 3:
        return print("Your currencies are invalid!")
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={base}&To={to}"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    else:
        return None


# Read data from scraped content
def read(html_doc):
    if html:
        soup = BeautifulSoup(html_doc, "html.parser")
        result = soup.find(class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        return result.text
    else:
        return None


# Run script
if __name__ == "__main__":
    base = input("Tell me the base currency (in international meaning): ").upper()
    to = input("Tell me the end currency (in international meaning): ").upper()
    amount = input("Tell me the amount of base: ")
    html = get_data(amount, base, to)
    result = read(html)
    if result:
        result = round(float(result[:9]), 3)
        print(f"{amount} {base} equals {result} {to}")
    else:
        print("Error while getting data from server!")
        print("It may be caused by bad currencies symbols")
