from ast import Num, arg
import multiprocessing as mp
import time
import cv2


# 多进程的共享内存,和lock锁
# 不能像多线程一样用global，会报错的，未定义变量
# 多进程可以打开两张图片

def job(x, v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        x = x + 10
        print(v.value)
        print(x)

    l.release()


def job1(q):
    img_1 = q.get()
    cv2.imshow('可以传进来参数的', img_1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def multicore():
    l = mp.Lock()
    q = mp.Queue()
    global x
    x = 0
    img_1 = cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\1.jpg')
    q.put(img_1)
    v = mp.Value('i', 0)
    m = mp.Value('d', 0)  # 双字节
    p1 = mp.Process(target=job, args=(x, v, 1, l))  # 参数传递可以，全局变量不行
    p2 = mp.Process(target=job, args=(x, v, 3, l))
    p3 = mp.Process(target=job1, args=(q,))  # 对进程用Queue传图
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('final v=%s' % v)  # 共享内存就是多个进程公用
    print('final x=%s' % x)  # 启动的时候传进去的这个x直接传进去的，是深拷贝，内部修改另一个进程不变，而且主进程只有启动进去时候的值



if __name__ == '__main__':
    multicore()
