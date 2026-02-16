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

from user_repo import UserRepository
from pytest import fixture 

# stays for full session 
@fixture(scope="session")
def fake_db_session():
    return {
        'hsenthil': "Hemapriya Senthilkumar",
        'vjaishankar': "Vasanthkumar Jaishankar",
        'gmathly': 'Gurunath Athalye'
    }

@fixture(scope="session")
def user_repo_session(fake_db_session):
    return UserRepository(fake_db_session)

# clears for each function
# default is function
@fixture(scope="function")
def fake_db():
    print("Creating DB object for specific testcase ...\n")
    db = {
        'hsenthil': "Hemapriya Senthilkumar",
        'vjaishankar': "Vasanthkumar Jaishankar",
        'gmathly': 'Gurunath Athalye'
    }
    yield db
    print("Use complete ...\n")
    db.clear()

@fixture(scope="function")
def user_repo(fake_db):
    return UserRepository(fake_db)


@fixture(autouse=True)
def add_logs(request):
    print(f"Starting Test {request.node.name} \n")
    yield 
    print(f"Ending Test {request.node.name} \n")

def test_create_user(user_repo):
    user_repo.create_user("poojas", "Poojapriya Senthilkumar")
    assert 'poojas' in user_repo.db

def test_create_user_session(user_repo_session):
    user_repo_session.create_user("poojas", "Poojapriya Senthilkumar")
    assert 'poojas' in user_repo_session.db

def test_get_user_no_session(user_repo):
    assert 'poojas' not in user_repo.db

def test_get_user_same_session(user_repo_session):
    assert 'poojas' in user_repo_session.db

def test_get_user(user_repo):
    assert user_repo.get_user('hsenthil') == "Hemapriya Senthilkumar"