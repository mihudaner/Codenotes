# 锁lock  处理共享内存，需要有先后顺序
import threading
import time
import copy
from queue import Queue


def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A, '\n')
    lock.release()
    print('release')


def job2():
    global A, lock
    lock.acquire()  # 要等其他线程释放才能申请到所，会阻塞在这里
    print('ok')
    for i in range(10):
        A += 10
        print('job2', A, '\n')
    lock.release()


def multithreading():
    global A, lock
    A = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    multithreading()
