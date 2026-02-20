"""
Docstring for multithreading.locking

Lock => basic/primitive synchronization construct available in python
methods:
    - acquire()
    - release()
- Doesnt have any ownership, it just needs to be locked/unlocked
Locks => equivalent to mutex

Acquire
---------
Locks are initialized with unlocked state
Any thread can call acquire => but only single thread can invoke
If any other thread tries to acquire, then it will blocked untill the lock object is released
If any thread doesnt want to wait indefinitely, acquire can be called with timeout(float)

Release
----------
Will change the state of the lock => unlocked
among many waiting threads only one will be chosen to acquire lock and proceed

"""
import time
from threading import Thread, Lock, current_thread

# shared variable
shared_list = [1,2,3,4]

def update_list():
    print(f"{current_thread().name} is running ...")
    shared_list.append(5)
    time.sleep(5)
    shared_list.append(6)

def get_count():
    print(f"{current_thread().name} is running ...")
    print(f"Length: {len(shared_list)}")

t1 = Thread(name="t1", target=update_list)
t2 = Thread(name="t2", target=get_count)

"""
t1.start()
t2. start()

t1.join()
t2.join()
"""

# the above example might cause inconsistency

# lets see now with use of locks

shared_list2 = [1,2,3,4]
_lock = Lock()

def update_list2():
    _lock.acquire()
    print(f"{current_thread().name} is running ...")
    shared_list2.append(5)
    time.sleep(5)
    shared_list2.append(6)

def get_count2():
    _lock.release() # this will not cause any problem
    _lock.acquire()
    print(f"{current_thread().name} is running ...")
    print(f"Length: {len(shared_list2)}")
    _lock.release()

t3 = Thread(name="t3", target=update_list2)
t4 = Thread(name="t4", target=get_count2)

t3.start()
t4.start()

t3.join()
t4.join()

# This will print the length correctly