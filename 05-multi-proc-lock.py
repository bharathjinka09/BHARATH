import _thread
import os
import time
from multiprocessing import Process, Lock

my_global_variable = 0

def printer(tname, lock):
    global my_global_variable 
    print('%d.%8s Before Modifying global data :%d' % (os.getpid(), tname, my_global_variable))
    print('%d.%8s Locking critical section' % (os.getpid(), tname))
    lock.acquire()
    print('%d.%8s Locking Success' % (os.getpid(), tname))
    try:
        for i in range(1, 4):
            print('%d.%8s **** In critical section...%d sec, global_data :%d' % (os.getpid(), tname,  i, my_global_variable))
            time.sleep(2)
            my_global_variable += 1
        print('%d.%8s Out of critical section...' % (os.getpid(), tname))
    finally:
        print('%d.%8s Before Unlock, global data :%d' % (os.getpid(), tname, my_global_variable))
        lock.release()
        print('%d.%8s After  Unlock, global data :%d' % (os.getpid(), tname, my_global_variable))
 
def main():
	lock = Lock()
	task_names = ['ganga', 'kaveri', 'penna']
	new_task_list = []

	for tname in task_names:
		try:
			ntask = Process(target=printer, args=(tname, lock))
			new_task_list.append(ntask) 
			ntask.start()
		except:
			print("Error: unable to start thread")

	time.sleep(20)

if (__name__ == "__main__"):
	main()
