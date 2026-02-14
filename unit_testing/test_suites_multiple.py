"""
🧠 Exercise 3: TestSuite + Multiple Test Classes

Now move from beginner to structured testing.

🧩 Build This

Create:

math_utils.py
string_utils.py


Write separate test classes:

TestMathUtils

TestStringUtils

🧪 Create a Custom TestSuite

Instead of auto discovery:

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestMathUtils))
suite.addTest(unittest.makeSuite(TestStringUtils))

runner = unittest.TextTestRunner()
runner.run(suite)


Now you understand what CI systems actually run.
"""

from math_utils import MathUtils
from string_utils import StringUtils
import unittest 

class TestMathUtils(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.mutils = MathUtils()

    @classmethod
    def tearDown(cls):
        del cls.mutils

    def test_integer_division(self):
        self.assertEqual(self.mutils.int_division(36, 5), 7)

    def test_integer_division_with_0(self):
        with self.assertRaises(ValueError):
            self.mutils.int_division(6,0)

    def test_power(self):
        self.assertEqual(self.mutils.power(2,3), 8)

    # Subtest for sending multiple values
    def test_multiple_values_power(self):
        for number in [2,4,5,6,7,8]:
            with self.subTest(number=number):
                self.assertEqual(self.mutils.power(number, 2), number**2)


class TestStringUtils(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.sutils = StringUtils()
    
    @classmethod
    def tearDown(cls):
        del cls.sutils 

    def test_string_join(self):
        self.assertEqual(self.sutils.join("hello", "world"), "hello world")

    def test_string_capitalize(self):
        self.assertEqual(self.sutils.capitalize("hello world"), "Hello world")

    def test_string_lower(self):
        self.assertEqual(self.sutils.make_lower("HELLO"), "hello")

    def test_string_upper(self):
        self.assertEqual(self.sutils.make_upper("hello"), "HELLO")


def create_and_run_suite(): 
    """
    addTest
    addTests
    loadTests
    """
    math_suite = unittest.TestSuite()
    math_tests = [
        TestMathUtils("test_integer_division"),
        TestMathUtils("test_integer_division_with_0"),
    ]
    math_suite.addTests(math_tests)
    math_suite.addTest(TestMathUtils("test_power"))
    math_suite.addTest(TestMathUtils("test_multiple_values_power"))

    loader = unittest.TestLoader()
    string_suite = loader.loadTestsFromTestCase(TestStringUtils)

    main_suite = unittest.TestSuite()
    main_suite.addTest(math_suite)
    main_suite.addTest(string_suite)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(main_suite)


if __name__ == "__main__":
   # unittest.main(verbosity=2)
   create_and_run_suite()