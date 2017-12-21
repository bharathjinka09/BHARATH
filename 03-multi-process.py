import os
import time
import sys

from multiprocessing import Process
 
def doubler1(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(('-->proc:%d. double value is :%d' % (proc, result)))

def doubler2(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(('-->proc:%d. double value is :%d' % (proc, result)))

def doubler3(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(('-->proc:%d. double value is :%d' % (proc, result)))

def main():
	procs = []

	pid = os.getpid()

	print(('-->Parent :%d' % (pid)))

	proc1 = Process(target=doubler1, args=(10,))
	proc2 = Process(target=doubler2, args=(15,))
	proc3 = Process(target=doubler3, args=(20,))

	procs.append(proc1)
	procs.append(proc2)
	procs.append(proc3)

	proc1.start()
	proc2.start()
	proc3.start()

	time.sleep(10)

	for proc in procs:
		proc.join()


if (__name__ == '__main__'):
    main()
