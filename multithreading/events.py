"""
Docstring for multithreading.events

- Simplest primitives available for synchronization
- it has a boolean flag which can be modified by set() and clear()
- can be checked by is_set() method
- has a wait() that threads can invoke to wait for the bool value to become true
- if its already true -> the threads returns immediately
- if multiple are waiting for the flag, then all will be unblocked
- Useful when multiple threads co-ordinate among them based on boolean predicate

Diff with Semaphores

- Unbounded semaphore can be can incremented many times
- event object can flip between only 2 states - set or unset

- bounded semaphore(1) != event
because the semaphore will raise value error if its acquired more number of times than 1

- thread never gets blocked on wait() of event object if the internal is set to true

"""
import time
from threading import Thread, Event 

event = Event()

def task1():
    for _ in range(5):
        event.wait()

def task2():
    time.sleep(1)
    event.set()

t1 = Thread(target=task2)
t1.start()

t2 = Thread(target=task1)
t2.start()

t1.join()
t2.join()

# Prime program using events

prime_avaialble = Event()
prime_printed = Event()

global exit_program
global prime_holder

def prime_printer():
    global prime_holder

    while not exit_program:
        # wait for the producer thread to find a prime and release
        prime_avaialble.wait()
        
        print(prime_holder)
        prime_holder = None 
        prime_avaialble.clear()
        
        
        # let the producer thread know that we have finished printing
        prime_printed.set()

def is_prime(n):
    if n == 2 or n == 3:
        return True 

    div = 2
    while div <= n/2:
        if n % div == 0:
            return False 
        div += 1
    return True

def prime_producer():
    global prime_holder
    i = 1

    while not exit_program:

        while not is_prime(i):
            i += 1
            time.sleep(0.1)
        
        prime_holder = i 

        # let the printer thread know that we have a prime available for printing
        prime_avaialble.set()

        prime_printed.wait()
        # wait for the printer thread to print and release the lock
        prime_avaialble.clear()

        i += 1



exit_program = False 
prime_holder = None

producer = Thread(name="producer", target=prime_producer)
producer.start()
consumer = Thread(name="consumer", target=prime_printer)
consumer.start()

# let it run for few seconds
time.sleep(3)

exit_program = True 

producer.join()
consumer.join()

