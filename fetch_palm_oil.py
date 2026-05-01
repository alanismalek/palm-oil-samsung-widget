print("=== Script START ===")

import requests
from bs4 import BeautifulSoup
import json

url = "https://markets.businessinsider.com/commodities/palm-oil-price"

print("Fetching URL...")
response = requests.get(url)
print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

price_element = soup.find("span", {"class": "price-section__current-value"})

if price_element:
    raw_price = price_element.text.strip()
    price = round(float(raw_price), 2)
    print("Price found:", price)
else:
    price = "Not found"
    print("Price NOT found")

data = {
    "commodity": "Palm Oil",
    "price": price,
    "unit": "MYR/ton",
    "source": url
}

with open("docs/palm_oil.json", "w") as f:
    json.dump(data, f, indent=4)

print("=== DONE ===")
print(data)