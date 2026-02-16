import os
import requests

def get_api_key():
    return os.environ["PAYMENT_API_KEY"]

def call_payment_gateway(amount):
    key = get_api_key()
    response = requests.post(
        "https://api.payments.com/pay",
        json={"amount": amount},
        headers={"Authorization": key}
    )
    return response.json()