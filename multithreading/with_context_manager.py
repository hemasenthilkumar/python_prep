"""
Docstring for multithreading.with_context_manager

Instead of using try-except-finally block, where cleanup happens explicitly in finally block
we can use "with statement"

in multi-threading, we can use locks using this statement
in that case, we dont have explicitly acquire or release the lock
"""

import time
from threading import Lock, Thread, current_thread

lock = Lock()
shared_var = 123

def task1():
    print(f"[{current_thread().name}] attempting to acquire the lock")
    with lock:
        print(f"[{current_thread().name}] acquired the lock")
        time.sleep(3)
        shared_var = 456
    print(f"[{current_thread().name}] released the lock")


def task2():
    print(f"[{current_thread().name}] attempting to acquire the lock")
    with lock:
        print(f"[{current_thread().name}] acquired the lock")
        print(f"Shared Value: {shared_var}")
    print(f"[{current_thread().name}] released the lock")

t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()