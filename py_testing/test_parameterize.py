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