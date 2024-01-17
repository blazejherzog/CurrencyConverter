import requests

API_KEY = "fca_live_ZIGEcnMsKg8cKRn5fV1WTLU7CtAxkgD0cvc7UtSr"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["PLN", "EUR", "USD", "CAD", "CZK", "DKK", "NOK"]


def convert_currency(base_currency):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base_currency}&currencies={currencies}"

    try:
        response = requests.get(url)
        json_data = response.json()
        return json_data["data"]
    except:
        print("Sorry, the currency you entered is not recognized.")
        return None


while True:
    base_currency = input("Enter the base currency or 'q' for quit: ").upper()

    if base_currency == "Q":
        break

    result = convert_currency(base_currency)

    if result is not None:
        del result[base_currency]
        for key, value in result.items():
            print(f"{key}: {value}")
