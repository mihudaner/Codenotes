import multiprocessing as mp
import time


# pool进程池,如何不是多次执行一个函数，而是两个函数
# 异步进程可以在后边一直往进程池里边丢任务
# map和apply的区别就是apply的返回值需要get，并且在get的时候会阻塞

def func1(msg):
    print('mas:', msg)
    time.sleep(1)
    print('end:', msg)


def func2(msg):
    print('mas:', msg)
    time.sleep(5)
    print('end:', msg)


def func3(msg):
    print('mas:', msg)
    time.sleep(8)
    print('end:', msg)


if __name__ == '__main__':
    pool = mp.Pool()
    res1 = [pool.apply_async(func1, ('func1',)), pool.apply_async(func2, ('func2',))]
    res2 = pool.apply_async(func3, ('func3',))
    pool.close()
    print('没有阻塞')
    pool.join()  # 会在join地方阻塞
