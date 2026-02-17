"""
🧪 6. Duration / Performance Testing
Scenario
# analytics.py
import time

def process_large_dataset(data):
    time.sleep(0.2)  # simulate heavy processing
    return sum(data)

🧠 Exercise

Write test to measure execution time

Fail test if > 0.3 seconds

Use pytest --durations=5

Use pytest-benchmark (if installed)

Mock time to speed test

Bonus:

Compare two algorithm implementations

Parametrize input sizes

Generate random large dataset fixture
"""

import time
import analytics
from analytics import process_large_dataset

def test_exec_time():
    start = time.time()
    process_large_dataset([1]*100000000)
    total_time = time.time() - start 
    print(total_time)
    assert total_time < 0.3

def test_processing():
    res = process_large_dataset([1,2,3,4])
    assert res == 10

def test_fast_processing(monkeypatch):
    monkeypatch.setattr(analytics.time, "sleep", lambda x: None)
    res = process_large_dataset([1,2,3,4])
    assert res == 10

