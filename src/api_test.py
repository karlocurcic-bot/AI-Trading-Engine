import requests

url = "https://api.frankfurter.app/latest?from=EUR&to=USD"

response = requests.get(url)

data = response.json()

eur_usd = data["rates"]["USD"]

print("EUR/USD exchange rate:", eur_usd)