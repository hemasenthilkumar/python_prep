

"""
Docstring for multithreading.conditional_variables

Spurious wakeups: Even if notify() is not called, still a waiting/sleeping thread can wakeup
Eventhough it woke up, doesnt mean it gets to move forward
So we have to check the conditions again inorder to make sure

Using different condition variables for notify() and wait() is bad design as it will be difficult to debug in the future
Because:

GOLDEN RULE:
All reads and writes happen under the SAME lock.

SHARED STATE MUST HAVE:
One state → One lock → One synchronization domain

CORRECT DESIGN
Use ONE lock protecting the state.

And create multiple condition variables that SHARE that same lock.
EG:
lock = Lock()

producer_condition = Condition(lock)
consumer_condition = Condition(lock)

EVEN BETTER
One condition is enough

🔥 Real-World Analogy

Imagine:

Two security guards guarding the same vault.

But they don’t talk to each other.

One guard locks the vault.
Other guard checks a different lock.

Vault is not actually secure.

You need:

One vault → One key → One guard at a time.

Why is using different condition variables with different locks on the same state bad?

Answer:

Because shared state must be protected by a single lock.
Using multiple condition variables with different locks breaks mutual exclusion guarantees and makes correctness
depend on fragile program structure rather than enforced synchronization.
"""

import time
from threading import Thread, Condition, current_thread

global exit_program
global is_prime_found
global prime_holder
cond = Condition() # default is RLock

def prime_printer():
    global prime_holder
    global is_prime_found

    while not exit_program:

        #while not is_prime_found and not exit_program:
        #    time.sleep(0.1)

        """
        Docstring for prime_printer

        Correct Usage for wait() --> this should be done only with while loop and not if loop

        Why??
         
        Because in case of IF clause --> it doesn't recheck if the condition becomes true
        Lets say multiple threads wait on the if condition to be true, once it has been set true, one of a thread will proceed
        and change the shared variable, and release the lock.
        now the remaining threads will continue whatever is after the if statement, since for them it already became true when it was notified

        So, to avoid this we have to use while loop -- which will recheck.

        Chef announces:

        "Food is ready!"
        
        Everyone wakes up and runs.
        
        But there is only 1 plate.
        
        First person takes it.
        
        Second person arrives and sees:
        No food.
        
        If they used if, they would assume:
        "Chef said food is ready → must be true."
        
        Wrong.
        
        If they used while, they would:
        Check again.
        If no food → wait again.

        So the best way is:

        acquire lock
        while(condition_to_test is not satisfied):
            wait

        # condition is now true, perform necessary tasks

        release lock
        """

        # for doing any operation like wait, notify, release, we have to acquire it first
        cond.acquire()
        while not is_prime and not exit_program:
            # wait
            cond.wait() # this will give up the lock for time being untill its woken up by notifying # NO CPU CYCLE WASTED as its sleeping
        # once done release
        cond.release()
        

        """
        Correct usage for notify()

        acquire lock
        set condition_to_test to true/satisfied  __
        notify                                   __} --> These 2 can be swapped lines, because anyway untill we release the lock, no other thread is gonna come
        release lock
        """
        if not exit_program:
            print(prime_holder)
            # Here we have to notify the consumer that we have done consuming
            cond.acquire()
            is_prime_found = False 
           # prime_holder = None   # this is not required as anyway we will override
            cond.notify()
            cond.release()

"""
If we want multiple threads to be the printer function but prints only unique value at a time, then

no changes in producer function
we have to use notifyAll() in both consumer & producer since multiple threads involved
"""

def printer_by_multiple():
    global is_prime_found 
    global prime_holder 

    while not exit_program:

        cond.acquire()
        while not is_prime_found and not exit_program:
            cond.wait()

        # we will not release right now, because we want to make sure that only 1 threads to gets to print at a time
        if not exit_program:
            print(f"{current_thread().name}: {prime_holder}")
            is_prime_found = False 
            prime_holder = None
            """
            We can't use notify() here, eventhough its supposed to wake up the producer thread, but it may wakeup other printer threads which are sleeping
            and it might cause deadlock in some scenarios because:
                another thread waking up and waiting for producer to produce
                producer sleeping hoping that some woken up printer thread would notify it.

            So we have to use notify all only here.
            """
            cond.notify_all()
        
        # we will release only after its printed.
        cond.release()

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
            # adding a timer to slow down
            time.sleep(0.5)

        prime_holder = i # this is set outside as no other thread would change it
        
        cond.acquire()
        is_prime_found = True
        # in case of using multiple printer threads use notify_all()
        # cond.notify()
        cond.notify_all()
        cond.release()

        # sleep till consumer makes it false
        cond.acquire()
        while is_prime_found and not exit_program:
            cond.wait()
        cond.release()

        i += 1
    print("Producer exiting!")


"""
We have to notify() all in the main section also because:

May be one of the thread exited -> which is supposed to send notify()
So be remaining threads would be waiting indefinitely.

So to end the program properly we have to call notify_all() 

"""
exit_program = False 
is_prime_found = False 
prime_holder = None

producer = Thread(name="producer", target=prime_producer)
producer.start()
consumer1 = Thread(name="consumer1", target=printer_by_multiple)
consumer1.start()
consumer2 = Thread(name="consumer2", target=printer_by_multiple)
consumer2.start()

# let it run for few seconds
time.sleep(3)

exit_program = True 

cond.acquire()
cond.notify_all()
cond.release()


producer.join()
consumer1.join()
consumer2.join()