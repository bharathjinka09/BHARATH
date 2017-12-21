import os
import time

print ("Hello world")

print(("my process id pid :%d, ppid :%d" % (os.getpid(), os.getppid())))

time.sleep(3)

os.fork()

while(1):
    print(("Pid :%d, Ppid :%d" % (os.getpid(), os.getppid())))
    time.sleep(1)
