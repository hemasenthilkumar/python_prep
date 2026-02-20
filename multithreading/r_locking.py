"""
Docstring for multithreading.r_locking

RLock = notion of ownership
The same thread can acquire the lock multiple times

Useful in case of recursive/nested calls.

Why not always use RLock instead of Lock?

Answer:
-RLock has overhead (tracks owner + count)
-Slightly slower
-Simpler lock gives clearer intent
-Avoid unnecessary reentrancy unless needed

"""

# with just simple lock

from threading import Thread, Lock, current_thread, RLock
lock1 = Lock()

def outer():
    with lock1:
        print(f"{current_thread().name} is executing ...")
        inner()

def inner():
    with lock1:
        print("Inner function done!")

t1 = Thread(name="outer", target=outer)
"""
t1.start()
t1.join()
"""

# this will cause a deadlock !

# we will now see the same scenario with Rlock
rlock = RLock()

def outer2():
    with rlock:
        inner2()

def inner2():
    with rlock:
        print("Done!")

t2 = Thread(name="outer2", target=outer2)
t2.start()
t2.join()

# this will work exactly fine!!