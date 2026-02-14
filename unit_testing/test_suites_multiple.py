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