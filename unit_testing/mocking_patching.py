"""
🧠 Exercise 4: Mocking & Patching (Real Backend Scenario)

This is SDE-2 level.

🧩 Build This
# payment_service.py
import requests

class PaymentService:
    def process_payment(self, amount):
        response = requests.post("https://fake-api.com/pay", json={"amount": amount})
        return response.status_code == 200

🧪 Your Job

Test this WITHOUT making real API calls.

Use:

from unittest.mock import patch, MagicMock

What You Must Cover
✅ patch decorator
@patch("payment_service.requests.post")

✅ return_value mocking
✅ side_effect

Simulate success

Simulate timeout

Simulate 500 error

✅ Assert mock called correctly
mock_post.assert_called_once_with(...)

🔥 Advanced Twist

Patch:

Environment variables

Time (datetime.now)

Builtins (open)
"""

import requests

class PaymentService:
    def process_payment(self, amount):
        response = requests.post("https://fake-api.com/pay", json={"amount": amount}, timeout=3)
        if response.status_code == 200:
            return response.json()
        raise Exception(f"[Error] API Returned Status Code: {response.status_code}")
    
import unittest 
from unittest.mock import patch, MagicMock

class TestPaymentService(unittest.TestCase):

    @patch("requests.post")
    def test_payment_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        # return value means what ever () function of reuqest we have to do with return value
        # for eg response.json() ==> mock_response.json.return_value = {}
        mock_response.json.return_value = {'msg': 'payment success'}
        mock_post.return_value = mock_response

        result = PaymentService().process_payment(400)
        self.assertIn('success',result['msg'])

    @patch("requests.post")
    def test_payment_failure_500(self, mock_post):
        # create sample response object
        mock_response = MagicMock()
        mock_response.status_code = 500

        # then assign this response to the request object
        mock_post.return_value = mock_response 
        with self.assertRaisesRegex(Exception, r".*500.*"):
            PaymentService().process_payment(400)
    
    @patch("requests.post")
    def test_timeout_failure(self, mock_post):
        mock_post.side_effect = requests.exceptions.Timeout

        with self.assertRaises(requests.exceptions.Timeout):
            PaymentService().process_payment(900)

    @patch("requests.post")
    def test_if_request_called_only_once(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'msg': 'payment success'}
        mock_post.return_value = mock_response 

        PaymentService().process_payment(400)
        # To make sure if requests.post() was called only once in that function
        mock_post.assert_called_once_with("https://fake-api.com/pay", json={"amount": 400}, timeout=3)

if __name__=="__main__":
    unittest.main(verbosity=2)