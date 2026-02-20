"""
Docstring for multithreading.subclassing_thread

Another way to create thread is by subclassing the Thread class

- We can override only the run() method and the constructor
- Thread.__init__() must be invoked by the subclass's init method
- args or kwargs don't get passed to the run method - we have to store them as variables and use them in run method
"""

from threading import Thread, current_thread

class TestThread(Thread):

    # override method
    def __init__(self):
        super().__init__()
        self.name = "test-thread"
        self.args = (1,2,3,4)
        self.kwargs = {'a':'bc', 'b':'cd'}
    
    def run(self):
        print(current_thread().getName())
        for a in self.args:
            print(a)
        for k,v in self.kwargs.items():
            print(f"{k} = {v}")

t1 = TestThread()
t1.start()
t1.join()