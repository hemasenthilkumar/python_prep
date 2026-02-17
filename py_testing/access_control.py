# access_control.py
def can_access(role, is_active, has_subscription):
    if not is_active:
        return False
    if role == "admin":
        return True
    if role == "user" and has_subscription:
        return True
    return False