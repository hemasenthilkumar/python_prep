"""
Program = set of instructions and associate data (residing on disk), loaded by the OS to perform a task
Process = Program in execution - Program can have copies of process, but process belongs to only one program
Thread = Samllest unit of execution within a process. 
- they share global state
- they have their own local variables

Cooperative vs Preemptive Multitasking
--------------------------------------

Preemptive MultTasking: (Used as core feature of Unix based systems)
- OS preempts a program to allow another task on CPU
- cannot determine when the preempted task will run again

Cooperative Multitasking:
- programs voluntarily gives up control so another program can run
- usually when period of time has expired or it becomes idle or logically blocked
- issues can happen with malicious program not giving up controls

Throughput vs Latency
----------------------

Throughput = how much work gets done per unit of time (This should go Up)
Latency = time required to complete a task or produce a result (This should go Down)

Synchronous vs Asynchronous
----------------------------

Synchronous = Serial execution
Asynchronous = Runs seperately and notifies the main thread of its completion - failure/progress
- doesnt wait for a task to complete before moving on to next
- best for network/disk I/O, waiting type of applications

I/O Bound vs CPU Bound
------------------------

Programs usually require:
- CPU Time (data crunching, image processing, matrix multiplication)
    - parallelism can help here
- I/O:
    - Memory (eg loading GBs of data to main memory)
    - Networking Resources
    - Disk Storage
    - Concurrency can help her to switch out the waiting processes

Thread Safety
-----------------
- Vulnerable due to corruption when state is shared

Critical Section & Race Conditions
-----------------------------------
- Need to be careful when multiple threads attempt simultaneously execute the same portion of code

Critical Section:
- Any piece of code :
    - has the possibility of concurrently executed by more than 1 thread
    - has exposed any shared data or resource

Race condition:
- Happens when thread runs at same time through critical section without thread synchronization
= Causes application inconsistency

DeadLocks, Liveness & Reentrant Locks
---------------------------------------

Deadlocks - resource needed by first thread held by second thread and vice versa
Liveness - Ability of program/app to execute in timely manner (If its in deadlock then its not live)

Live-Lock:

- when 2 threads continously react in response to the actions by other thread without any progress
- eg, 2 people try to cross each other in hallway and keep blocking each other
- Similar to deadlock but its not dead rather in live state

Starvation:
- app can go into starvation mode if it never gets CPU time
- other greedy apps might be hogging the system

Reentrant Lock:
- allows re-locking or re-entering of synchronization lock
- would block as soon as it attempts to reacquire second time instead of waiting forever


Mutex vs Semaphore
--------------------

Mutex:
- guard shared data with mutual exclusion
- allows only a single thread to access a critical section or shared resource
- once a thread acquires a mutex, all other threads are blocked untill its released

Semaphore:
- limiting access to collection of resources (like having limited no of permits)
- if all permits are handed out and new thread comes in, it will blocked until earlier thread comes back with permit
- Eg. DB connections with fixed available connections limit
- Binary Semaphore: With single permit
- Used for signaling among threads

Difference between mutex & semaphore: 
- Mutex: 
     - same thread acquired the mutex should release it (Has ownership)
     - Only guards
- Semaphore: 
    - different threads can acquire and release (No ownership, anyone can lock if unlocked and vice versa)
    - used for signaling among threads

Mutex vs Monitor
-------------------

Monitors: Language-level constructs (Mutex + condition variables) = Monitor with wait set
Mutex: Low level or OS provided constructs

Scenario:
- Sometimes mutual exclusion is not enough
- we want to test a predicate/condition with mutual exclusive lock and
if we find the predicate to be false, we wikl wait on a condition variable
untill its value changed to true

Solution: Spin Waiting

Mesa vs Hoare Monitors
-----------------------

Note: Monitors requires while loop for checking the condition till its false, so that it can
go into wait mode

Then if its signaled and woken up, it has to check again the condition so that another thread
shouldn't have changed it to false again in the meantime (notify() till thread waking up & acquiring the mutext )


Mesa Monitors: (Used in python)

So for the above issue, in Mesa monitors, the woken up thread has to compete with the other threads
to acquire the mutex. So the signaling thread empties the monitor BUT continues to own the 
monitor until it exists the monitor section

More efficient than Hoare monitors. Developer is expected to check for condition/predicate in a while loop

Hoare Monitors:

The signaling thread yields the monitor to the woken up thread and the woken up thread enters the
monitor while the signaling thread sits out.

This ensures that the predicate would not have changed, to avoid checking in a while loop
we can simply use a if clause
No other threads will enter the monitor.

Semaphore vs Monitor
-----------------------
Note:
Monitor is combined of mutex, conditional variables
Mutex is a subset of monitor

- Monitor and semaphore are interchangable
- one can be created out of other
- one can be reduced to other

Monitors:
- takes care of atomically acquiring locks
- pre-packaged solution with less dependency on developer to right locking 
- Only one thread can enter monitor
- Solution for missed signal issue
Semaphore:
- lock acquiring logic is developed by developer, can be error prone
- more lightweight
- multiple threads can enter the critical section
- SOlution for missed signal issue

Global Interpreter Lock (GIL)
-------------------------------

Note:
- Python is interpreted language --> no static compiling
- Even when we run .py file
    Interpreter -> compiles .py file -> byte code -> understood by PVM (Python Virtual Machine)
    PVM is not seperate component, its a just a loop in the interpreter that is responsible for
    executing byte code line by line
    PVM is part of interpreter
- PI (Python Interpreter)
    - can execute only 1 thread at a time
    - can cause consequences on CPU bound programs performance
    - its limited to run a single thread due to -> Memory management in Python = reference counter

- Reference Counter
    - when ref to a object increases -> counter decrease and vice versa
    - when the ref = 0, the object is deallocated
    - the thread limitation is there to ensure the ref counter is safe from race condition
    - Ref counter associated with every object, so more locks would be required to keep it thread safe

GIL = Single lock that provides exclusive access to Python interpreter
Execution of Python bytecode acquires GIL
Cost to be paid is limiting CPU-bound tasks to single thread

Removing GIL:
- removing caused breaking C extensions -> performace degradation of single & multithreaded I/O based programs
- so GIL is not removed
- GIL serializes access to PI
- only good for blocking I/O


Note:
Python 3.13+ Free-Threading: Starting with Python 3.13, developers can compile a special "free-threaded" version of Python where the GIL is disabled,
enabling true multithreading for CPU-bound tasks and allowing them to leverage multiple CPU cores efficiently. 
This feature is experimental in 3.13 and not available in standard pre-built distributions; it requires building Python from source with a specific flag.

Amdahl's Law
-------------
The cap on the maximum speedup can be achieved when parallelizing the execution of a program

programs consists of parts that can be sped up even if more processors = these parts must be executed serially

S(n) = 1 / ((1-P) + P/n)
where S(n) = speed up using N cores/threads
P = fraction of the program which can be parallelized
1-P = fraction of program which should be executed serially

Eg:
Our code has 90% of parallelizable code = 0.9

1 core = 1/(1-0.9)+(0.9/1) = 1
2 cores = 1.81
3 cores = 3.57
10 cores - 5.26
....
1000 cores = 9.91
Infinite = 10 ~ 10 times

We cannot speed up more than 10 times with 10% serializabile code

Utlization = speed-up divided by number of processors
So 
utilization = 5/10 = 0.5 = 50%
so only 50% is utilized , remaining time they will be idle

As N approaches infinity, the law becomes
    S(n) = 1 / 1-P = 1/Serializability program fraction

There are many factors that can mess the speed up. The law is not very realisitic
the actual speed up can be less than calculated

Better law for larger datasets -> Gustafson's Law

Moore's Law
-------------

Number of transistors that can be packed into given unit of space = doubles every 2 years
in turn,
processing power of computers doubles and cost halves

It came down decade ago due to = clock speeds = because supply voltage is already down to an extent
"""