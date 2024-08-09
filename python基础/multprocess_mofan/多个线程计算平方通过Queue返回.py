import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    # return l #线程调用的函数不能返回值，因为时间同步不一的问题
    q.put(l)


def multmain():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]

    for i in range(4):
        l = data[i]
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    print(threads)
    for thread in threads:
        thread.join()

    results = []

    for _ in range(4):
        results.append(q.get())
    print(data)


if __name__ == '__main__':
    multmain()
