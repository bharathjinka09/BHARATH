import os
import time
import sys

from multiprocessing import Process
 
def doubler1(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    pid = os.getpid()
    print(('-->proc:%d. double value is :%d' % (pid, result)))

def main():
    proc_list = []
    pid = os.getpid()

    print(('-->Parent: Before Child created :%d' % (pid)))

    proc = Process(target=doubler1, args=(5,))

    print(('-->Parent: After Child created :%d' % (pid)))

    proc_list.append(proc)

    print ('-->Parent: Starting the Child process')

    proc.start()

    print ('-->Parent: After child started, going for sleep')

    time.sleep(5)

    print ('-->Parent: After after sleep')

    for proc in proc_list:
        proc.join()

    print ('-->Parent: Exiting')

if (__name__ == '__main__'):
    main()
