from threading import Timer, Thread, current_thread

def thread_task():
    print("{0} executing".format(current_thread().name))


myThread = Thread(group=None,  # reserved
                  target=thread_task(), # if u use () --> main thread will get executed
                  name="childThread")

myThread.start()
myThread.join()


def timer_task():
    print("timer task")


timer = Timer(5, timer_task)
timer.start()

print("Main thread exiting")
