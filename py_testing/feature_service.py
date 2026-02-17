import os

def is_feature_enabled(user_id):
    if os.getenv("ENABLE_FEATURE") != "true":
        return False
    return user_id % 2 == 0
