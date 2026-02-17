"""
🧪 7. Advanced Combined Exercise (Real 5YOE Level)
Scenario: Feature Flag Based System
# feature_service.py
import os

def is_feature_enabled(user_id):
    if os.getenv("ENABLE_FEATURE") != "true":
        return False
    return user_id % 2 == 0

🧠 Write tests that combine:

Fixture for env setup

Monkeypatch env

Parametrize multiple user_ids

Marks for feature tests

Performance constraint

Use custom CLI option to enable feature`
"""
import pytest 
from feature_service import is_feature_enabled

@pytest.fixture()
def env_setup_true():
    return "true"

@pytest.fixture()
def env_setup_false():
    return "false"


@pytest.mark.parametrize("user_id, expected", [
    (1234, True),
    (123, False),
    (45, False),
    (0, True),
    (1, False)
])
def test_feature_enabled_for_users(user_id, expected, env_setup_true, monkeypatch):
    monkeypatch.setenv("ENABLE_FEATURE", env_setup_true)

    assert is_feature_enabled(user_id) == expected


@pytest.mark.parametrize("user_id, expected", [
    (1234, False),
    (123, False),
    (45, False),
    (0, False),
    (1, False)
])
def test_feature_disabled_for_users(user_id, expected, env_setup_false, monkeypatch):
    monkeypatch.setenv("ENABLE_FEATURE", env_setup_false)

    assert is_feature_enabled(user_id) == expected