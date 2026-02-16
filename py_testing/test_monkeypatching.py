"""
🧪 3. MonkeyPatch – Environment + External API
Scenario
# payment.py
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

🧠 Exercise

Monkeypatch os.environ

Monkeypatch requests.post

Simulate:

success response

failure response

network exception

Assert correct JSON handling

Ensure no real HTTP call happens

Bonus:

Patch at correct import location (important!)

Create reusable fixture for mocked requests
"""
import payment
import pytest
from payment import call_payment_gateway

class FakeResponse:

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data 
    
    def json(self):
        return self.data

def fake_os_environ():
    return "XXXYYYZZZ"


def test_success_response(monkeypatch):
    monkeypatch.setenv("PAYMENT_API_KEY", fake_os_environ())
    called = {}
    def fake_post(url, json, headers):
        # same input as of post [! IMPORTANT !]
        # tracking inputs

        called['url'] = url 
        called['json']= json 
        called['headers'] = headers
        return FakeResponse(200, {"msg": "success"})

    monkeypatch.setattr(payment.requests, "post", fake_post)

    result = call_payment_gateway(1000)
    assert result == {"msg": "success"}
    
    # make sure whether this is only called

    assert called['json'] == {'amount': 1000}
    assert called['headers']['Authorization'] == fake_os_environ()

def test_failure_response(monkeypatch):

    monkeypatch.setenv("PAYMENT_API_KEY", "AAABBBCCC")
    
    def fake_response(url, json, headers):
        return FakeResponse(500, {'msg': 'failure'})
    
    monkeypatch.setattr(payment.requests, "post", fake_response)

    result = call_payment_gateway(-1)
    assert result == {'msg': 'failure'}

def test_network_failure(monkeypatch):

    monkeypatch.setenv("PAYMENT_API_KEY", "AAABBBCCC")

    def fake_response(*args, **kwargs):
        raise payment.requests.ConnectionError
    
    monkeypatch.setattr(payment.requests, "post", fake_response)

    with pytest.raises(payment.requests.ConnectionError):
        call_payment_gateway(500)
    

