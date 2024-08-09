import threading
import time
import random


class Box:
    def __init__(self):
        self.lock = threading.RLock()

    def ex(self):
        self.lock.acquire()
        print("ex")


def fun1(b):
    for i in range(5):
        b.ex()
        print("fun1")


def fun2(b):
    for i in range(5):
        time.sleep(1)
        # b.lock.release()  # rlock其他线程不能解锁，而且属于的进程可以锁多次，也需要多次解
        b.ex()
        print("fun2")


if __name__ == "__main__":
    b = Box()

    t1 = threading.Thread(target=fun1, args=(b,))
    t2 = threading.Thread(target=fun2, args=(b,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
