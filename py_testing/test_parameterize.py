"""
🧪 4. Parametrize – Business Rules Matrix
Scenario
# access_control.py
def can_access(role, is_active, has_subscription):
    if not is_active:
        return False
    if role == "admin":
        return True
    if role == "user" and has_subscription:
        return True
    return False

🧠 Exercise

Use @pytest.mark.parametrize to:

Create matrix covering:

admin active/inactive

user with/without subscription

guest

Include readable IDs

Combine multiple parametrize decorators

Use custom object instead of primitive

Bonus:

Parametrize fixture

Use indirect parametrization
"""
import pytest
from access_control import can_access

@pytest.mark.parametrize("role, is_active, has_subscription, expected", [
    ("admin", True, False, True),
    ("admin", False, False, False),
    ("user", True, True, True),
    ("user", True, False, False),
    ("user", False, False, False),
    ("guest", True, False, False)

], 
ids=[
    "admin_active", "admin_inactive", "user_active_subscription", "user_active_no_subscription",
    "user_inactive", "guest_active"
])
def test_can_access(role, is_active, has_subscription, expected):
    assert can_access(role, is_active, has_subscription) == expected