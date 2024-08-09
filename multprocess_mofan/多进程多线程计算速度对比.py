import multiprocessing as mp
import threading as td
import time

"""计算速度的比较"""
#  多进程
def job(q):
    res = 0
    for i in range(3000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))  # 这里的逗号说明这是一个可以迭代的东西
    p2 = mp.Process(target=job, args=(q,))
    p3 = mp.Process(target=job, args=(q,))
    p4 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('multcore', res1 + res2 + res3 + res4)


def normal():
    res = 0
    for _ in range(4):
        for i in range(3000000):
            res += i + i ** 2 + i ** 3
    print("normal", res)


def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))  # 这里的逗号说明这是一个可以迭代的东西
    t2 = td.Thread(target=job, args=(q,))
    t3 = td.Thread(target=job, args=(q,))
    t4 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('thread', res1 + res2 + res3 + res4)


if __name__ == '__main__':
    st = time.time()
    print('timestart')
    normal()
    st1 = time.time()
    print('normaltime', st1 - st)  # normaltime 11.245430946350098
    multithread()
    st2 = time.time()
    print('multithreadtime', st2 - st1)  # multithreadtime 9.925086736679077
    multicore()
    st3 = time.time()
    print('multicoretime', st3 - st2)  # multicoretime 5.998522758483887
