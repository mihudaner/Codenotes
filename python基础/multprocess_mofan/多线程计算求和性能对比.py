# python之不一定效率高，pyhon的多线程其实是在运行一个进程之后，会锁住其他的进程
# 他是在运行的时候在进程之间不停的切换，
# 所以说不是1个进程10秒完成，分配给5个进程就是2秒,可能节省一点读写时间
# 多核运算

import threading
import time
import copy
from queue import Queue


def job(l, q):
    res = sum(l)
    q.put(res)


def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]  # 借用列表生成器，实现for循环
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)


if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l * 4)  # 列表赋值4次
    print('normal:', time.time() - s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading:', time.time() - s_t)
