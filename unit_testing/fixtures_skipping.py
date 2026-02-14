"""
🧠 Exercise 2: User Registration System (Fixtures + Skipping)

Now we simulate real backend logic.

🧩 Build This
# user_service.py
class UserService:
    def __init__(self):
        self.users = {}

    def register(self, username, email):
        ...

    def delete(self, username):
        ...

    def get_user(self, username):
        ...


Rules:

Username must be unique

Email must contain "@"

Raise custom exceptions

🧪 Write Tests

Now cover:

✅ Fixtures

setUp()

tearDown()

setUpClass()

tearDownClass()

Example ideas:

setUp() creates fresh UserService

tearDown() clears users

✅ Different Assertions

Use:

assertTrue

assertFalse

assertIn

assertNotIn

assertDictEqual

assertRaisesRegex

✅ Skipping Tests

Use:

@unittest.skip("Feature not implemented yet")
@unittest.skipIf(condition, "reason")
@unittest.skipUnless(condition, "reason")


For example:

Skip email validation test on Windows

Skip integration test if env variable not set
"""

import sys

class UserService:
    def __init__(self):
        self.users = {}

    def register(self, username, email):
        if username in self.users:
            raise ValueError("Username already exists!")
        if '@' not in email:
            raise ValueError("Invalid Email ID")
        self.users[username] = {'email': email}
        return "User Registered."
    
    def verify_user(self, username):
        return username in self.users

    def delete(self, username):
        if username in self.users:
            self.users.pop(username)
            return "User Deleted."
        raise ValueError("User not found!")

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        raise ValueError("User not found!")
    

import unittest 

class TestUserService(unittest.TestCase):

    def setUp(self):
        """
        Setting up testcases
        """
        self.user_service = UserService()
        self.user_service.users = {
            'hema': {'email': 'hema@gmail.com'},
            'vasanth' : {'email': 'vasanth@outlook.com'}
        }
    
    def tearDown(self):
        """
        Tear Down for cleanup
        """
        del self.user_service 

    def test_user_exists(self):
        self.assertTrue(self.user_service.verify_user('hema'))
    
    def test_user_not_exists(self):
        self.assertFalse(self.user_service.verify_user('hema1'))

    def test_user_registeration(self):
        self.user_service.register('pooja', 'pooja@gmail.com')
        self.assertIn('pooja', self.user_service.users)
    
    def test_get_user(self):
        self.assertDictEqual(self.user_service.get_user('vasanth'), {'email': 'vasanth@outlook.com'})

    def test_user_deletion(self):
        self.user_service.register('pooja', 'pooja@gmail.com')
        self.user_service.delete('pooja')
        self.assertNotIn('pooja', self.user_service.users)
        with self.assertRaisesRegex(ValueError, r".*not found.*"):
            self.user_service.delete('pooja')
    
    @unittest.skip("Not Implemented Yet")
    def test_user_authentication(self):
        ...

    @unittest.skipIf("Not supported", "3.13" in sys.version)
    def test_user_login(self):
        return "User Authenticated!"

    @unittest.skipUnless("Not supported", "3.13" in sys.version)
    def test_password_validity(self):
        return "Password verified"
    
    def test_email_validity(self):
        email = self.user_service.get_user('hema').get("email")
        if 'hotmail' in email:
            self.skipTest("Hotmail not supported!")
        return "Email Verified"

if __name__ == "__main__":
    unittest.main(verbosity=2)