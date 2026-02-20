"""
Docstring for multithreading.daemon_thread

Difference between regular thread and daemon thread:
- python program will not exit untill all regular/user threads terminate
- but program may exit even if the daemon thread is still not finished

Creating a daemon thread:

dthread = Thread(target=some_func, daemon=True)

This daemonic property comes from the current thread. (thats why it can be None, rather than True/False)
"""

# Regular thread exiting

import time
from threading import Thread, current_thread 


def infinite_loop():
    while True:
        print(f"{current_thread()} is still executing")
        time.sleep(1)

t1 = Thread(
    name="user thread",
    target = infinite_loop,
    daemon=None
)

"""
t1.start ()

# No join
# we will simply print exit msg
# this will cause infitie loop
print("Program exiting")
"""

# Daemon thread exiting

t2 = Thread(
    target = infinite_loop,
    name="d_thread",
    daemon=True
)

t2.start()

# This will exit
print("Program exiting")