"""
🧪 2. Fixtures – DB Layer Simulation
Scenario
# user_repo.py
class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.get(user_id)

    def create_user(self, user_id, name):
        self.db[user_id] = name

🧠 Exercise

Create a fixture fake_db() that returns a fresh dict every test.

Create a fixture user_repo(fake_db)

Write tests to:

Create user

Fetch user

Ensure isolation between tests

Convert fixtures into:

module scope

session scope

Add autouse=True fixture that logs start/end of each test

Bonus:

Use yield fixture for setup/teardown.
"""