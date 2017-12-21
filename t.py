import os
import time

retval = os.fork()

if (retval == 0):
    print("I am child   retval :%d, pid :%d, ppid :%d"  % (retval, os.getpid(), os.getppid()))
else:
    print("I am parent  retval :%d, pid :%d, ppid :%d"  % (retval, os.getpid(), os.getppid()))

time.sleep(1)
