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
from pytest import approx, raises, fixture
from pricing import PriceCalculator

@fixture
def init_pc():
    pc = PriceCalculator(tax_rate=0.1)
    return pc

def test_correct_final_price(init_pc):
    assert init_pc.final_price(40) == 44 

def test_correct_final_price_discount(init_pc):
    assert approx(init_pc.final_price(40, 0.15) )== 37.4

def test_invalid_base_price(init_pc):
    with raises(ValueError):
        init_pc.final_price(-1)

def test_invalid_discount_price(init_pc):
    with raises(ValueError):
        init_pc.final_price(400, 1.5)

def test_full_discount(init_pc):
    assert init_pc.final_price(400,1) == 0