"""
Docstring for multithreading.condition_variables

Sometimes along with locks we might need conditions also, or signaling between the threads

# Eg - producer consumer problem for prime numbers

Producer -> checks and produces prime number
Consumer -> waits and prints prime number

Concept:
We need to maintain 3 shared variables:
- exit_program (bool)
- is_prime_found (bool)
- prime_holder (int)

Consumer:
- till exit program == False --> check if is prime found --> if yes then print the prime holder and make the prime holder None, is prime found to false
- if exit prograam == True -> exit

Producer:
- till exit program == False --> from 1 start checking and setting prime found true & prime holder value only if they are set to false
--> but if we found prime, then wait untill it becomes true to start checking again
- if exit program == exit

The problem with the above scenario is, we should not do busy waiting / continously polling untill producer produces. This wastes CPU Cycles.
This can be solved in conditional variables.
"""
import time
from threading import Thread

global exit_program
global is_prime_found
global prime_holder

def prime_printer():
    global prime_holder
    global is_prime_found

    while not exit_program:

        while not is_prime_found and not exit_program:
            time.sleep(0.1)
        
        if not exit_program:
            print(prime_holder)

            is_prime_found = False 
            prime_holder = None 

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
    global is_prime_found
    i = 1

    while not exit_program:

        while not is_prime(i):
            i += 1
        
        prime_holder = i 
        is_prime_found = True

        # sleep till consumer makes it false
        while is_prime_found and not exit_program:
            time.sleep(0.1)

        i += 1



exit_program = False 
is_prime_found = False 
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