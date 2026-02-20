"""
Docstring for multithreading.semaphores

Semaphores = atomic counters
that decrements if acquire() is invoked &
incremenets if release() is invoked

It can be initialized with some count value.
Default is 1

Main usage: Signaling among threads which are working for a common goal

if some thread calls notify() before the remaining thread(s) get a chance to wait()
then this is miscommunited signal / missed signal

Solution: Use semaphores

Even if we call release() first, it will cause any block
"""

# Creating Semaphores
from threading import Semaphore

sem = Semaphore()
sem1 = Semaphore(5)


# rewriting the prime program with semaphores

import time
from threading import Thread

sem_find = Semaphore(0)
sem_print = Semaphore(0)
global exit_program
global prime_holder

def prime_printer():
    global prime_holder

    while not exit_program:
        # wait for the producer thread to find a prime and release
        sem_find.acquire()
        
        print(prime_holder)
        prime_holder = None 
        
        # let the producer thread know that we have finished printing
        sem_print.release()

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
        sem_find.release()

        # wait for the printer thread to print and release the lock
        sem_print.acquire()

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
