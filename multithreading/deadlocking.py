import time
from threading import Lock, Thread, current_thread

lock1 = Lock()
lock2 = Lock()

def func1():
    lock1.acquire()
    lock2.acquire()
    time.sleep(1)
    lock2.release()
    lock1.release()

def func2():
    lock2.acquire()
    lock1.acquire()
    time.sleep(1)
    lock1.acquire()
    lock2.acquire()

t1 = Thread(target=func1)
t2 = Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()