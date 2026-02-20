"""
Docstring for multithreading.wait_notify

We will take a closer look at wait and notify methods here

1. wait(n)
 n = timeout seconds (float)
 after that it will be woken up even if no one notified it

2. notify_all()

3. notify(n)
n = number of threads to wake up

"""

import time
from threading import Thread, Condition 

cond = Condition()
predicate = False

def wait_task():

    cond.acquire()
    """
    IF CLAUSE --> Bug because it doesnt recheck and being waken up, it proceeds even if the predicate is false
    WHILE CLAUSE --> It wakes up every 2 seconds and goes to sleep again if the predicate is False , only when its True, it proceeds

    The timeout is not useless.

        It changes semantics from:

        Wait forever until notified

        to

        Periodically wake up and check something.

    🎯 Final Mental Model

    Condition variable = Doorbell.

    wait(timeout) → “Wake me when doorbell rings OR after 2 seconds.”

    while not predicate → “Only open the door if the package is actually there.”

    Doorbell ringing doesn’t mean package exists.
    """
    if not predicate: 
        cond.wait(2)
    print("Completed wait!")
    cond.release()

t1 = Thread(target=wait_task)
t1.start()

time.sleep(5)

cond.acquire()
predicate = True
cond.notify()
cond.release()

t1.join()