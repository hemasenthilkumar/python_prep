"""
Docstring for multithreading.timer_class

time.sleep() --> blocks the current thread
whereas

timer --> creates a daemon thread which delays the target function

we can pass interval, the function and the args to the function also
and we can cancel the timer also before the task has been executed
"""

from threading import Timer 

def task(*args):
    print("I am executing!")
    for a in args:
        print(a)

t1 = Timer(2, task, [1,2,3,4,5])
t1.start()

t1.join()