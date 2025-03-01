import requests
import json
from tkinter import messagebox


class Model:
    def __init__(self):
        self.supported_currencies = ["EUR", "USD", "GBP", "SEK"]
        self.rates = self.load_rates()

    def load_rates(self):
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            rates = {key: data["rates"].get(key, None) for key in self.supported_currencies}
            return rates
        except:
            messagebox.showerror("Error", "Could not fetch exchange rates.")
            return {}

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Invalid currency")
        rate = self.rates[to_currency] / self.rates[from_currency]
        return round(amount * rate, 2)