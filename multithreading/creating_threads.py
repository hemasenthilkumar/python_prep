"""
Docstring for multithreading.creating_threads

We can threads using the thread class

Thread(group = None, 
       target = None, 
       name = None, 
       args = (),
       kwargs = {},
       *,
       daemon = None)

group = future use
target = callable object
name = thread name
args = args that can be passed to the function
kwargs = keyword args that can be passed to the function
daemon = if set to true, then will run as daemon thread
"""

import threading 

def test_func(*args, **kwargs):
    print(threading.current_thread().getName())
    for a in args:
        print(a)
    for k,v in kwargs.items():
        print(f"{k} = {v}")

t1 = threading.Thread(name="test-thread",
                      target=test_func,
                      args=(1,2,3,4),
                      kwargs={'a':'bc', 'b':'cd'})

t1.start()
t1.join()