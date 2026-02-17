"""
🧪 5. Marks – Categorization + Selective Runs
Scenario

You have:

Unit tests

Integration tests

Slow tests

🧠 Exercise

Create:

@pytest.mark.unit

@pytest.mark.integration

@pytest.mark.slow

Configure markers in pytest.ini

Run:

only unit

exclude slow

Use xfail

Use skipif based on OS

Bonus:

Mark flaky test

Custom mark requiring API key

"""
import pytest 
import sys, platform

# pytest -s .\test_marking.py -m "not unit" --> To skip unit
# -m unit --> only unit
# -m unit or slow -> unit and slow


@pytest.mark.unit
@pytest.mark.xfail
def test_unit_test1():
    assert True == False 

@pytest.mark.unit
def test_unit_test2():
    assert True == True 

@pytest.mark.unit
def test_unit_test3():
    assert True == True 

@pytest.mark.skipif(platform.os.name == "nt" , reason="Only for Linux based platforms")
@pytest.mark.integration
def test_intg_test1():
    assert True == True 

@pytest.mark.integration
def test_intg_test2():
    assert True == True 

@pytest.mark.integration
def test_intg_test3():
    assert True == True 

@pytest.mark.slow
def test_slow_test1():
    assert True == True 

@pytest.mark.slow
def test_slow_test2():
    assert True == True 

@pytest.mark.slow
def test_slow_test3():
    assert True == True 