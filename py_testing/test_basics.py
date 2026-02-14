"""
🧪 1. Pytest Basics – Service Layer Validation
Scenario

You’re building a pricing engine.

# pricing.py
class PriceCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def final_price(self, base_price: float, discount: float = 0):
        if base_price < 0:
            raise ValueError("Invalid base price")
        if discount < 0 or discount > 1:
            raise ValueError("Invalid discount")
        return base_price * (1 - discount) * (1 + self.tax_rate)

🧠 Exercise

Write tests that:

Validate correct final price

Validate exception cases

Ensure floating precision is handled properly (use pytest.approx)

Ensure test readability using proper naming conventions

Bonus:

Test edge case: discount = 1

Test zero tax rate
"""