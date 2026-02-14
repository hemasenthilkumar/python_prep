"""
🧠 Exercise 1: Calculator Service (Foundations)
🎯 Goal

Cover:

TestCase

Basic assertions

Running using unittest.main()

🧩 Build This

Create:

# calculator.py
class Calculator:
    def add(self, a, b): ...
    def subtract(self, a, b): ...
    def divide(self, a, b): ...


Add proper exception handling for division by zero.

🧪 Write Tests

Create test_calculator.py:

You must cover:

assertEqual

assertNotEqual

assertAlmostEqual

assertRaises

assertIsInstance

🚀 Advanced Twist

Write a main() block

Run via CLI:

python -m unittest test_calculator.py


Also try:

python test_calculator.py

"""

import unittest 

class Calculator:

    def add(self, a, b):
        return a+b 

    def subtract(self, a, b):
        return a-b 

    def multiply(self, a, b):
        return a*b 

    def divide(self, a, b):
        if b == 0:
            raise ValueError("The divisor cannot be 0!")
        return a/b 
    
class TestCalculator(unittest.TestCase):

    def test_isinstance(self):
        """
        Testing if its of same instance
        """
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add(self):
        """
        Testing add function
        """
        self.assertEqual(Calculator().add(5,6), 11)
        self.assertNotEqual(Calculator().add(5,6), 1)

    def test_subtract(self):
        """
        Testing subtract function
        """
        self.assertEqual(Calculator().subtract(5,6), -1)
        self.assertNotEqual(Calculator().subtract(5,6), 1)

    def test_multiply(self):
        """
        Testing multiply function
        """
        self.assertEqual(Calculator().multiply(5,6), 30)
        self.assertNotEqual(Calculator().multiply(5,6), 1)

    def test_divide(self):
        """
        Testing divide function
        """
        self.assertEqual(Calculator().divide(35,5), 7.0)
        with self.assertRaises(ValueError):
            Calculator().divide(6,0)
        self.assertAlmostEqual(Calculator().divide(35,5), Calculator().divide(35,4.999), places = 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # python -m unittest unit_testing.basics -v