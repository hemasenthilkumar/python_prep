"""
Docstring for multithreading.barrier

- Synchronization construct to wait for certain number of threads to
reach a common synchronization point in code
- involved threads invoke the barrier object's wait and get blocked till all all threads call wait
- when the last thread invokes wait, all threads gets released same time

We can also pass a callable which will get triggered when all threads are released

Broken Barriers:
we can use the abort() method to avoid deadlocks if needed.
The threads which are waiting will experience a BrokenBarrierError when abort() is invoked
"""


import random 
import time 

from threading import Barrier, Thread, current_thread 

def task():
    # sleeps for random time per thread
    time.sleep(random.randint(0,5))
    print(f"[{current_thread().name}] Curerntly {barrier.n_waiting} threads blocked on the barrier")
    # invoke the wait function
    barrier.wait()
    print("Barrier Broken!!")

def final_task():
    print(f"[{current_thread().name}] All threads have been completed")

barrier = Barrier(5, action=final_task)
threads = [0] * 5 

for i in range(5):
    threads[i] = Thread(target=task)

for i in range(5):
    threads[i].start()

# in case of abort
time.sleep(3)
print("Invoking abort() ...")
barrier.abort()