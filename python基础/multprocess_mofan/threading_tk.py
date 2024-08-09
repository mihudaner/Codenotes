import cv2
import threading
import time
import copy
from queue import Queue


# 多线程也不能同时打开两个窗口
def job1():
    img_1 = cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\1.jpg')
    cv2.imshow('img1', img_1)
    cv2.waitKey(0)


def job2():
    time.sleep(1)
    img_2 = cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\team.png')
    # cv2.namedWindow('img2')
    cv2.imshow('img2', img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()

    '''
    # 可以同时打开俩个窗口
    img_1=cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\1.jpg')
    img_2=cv2.imread(r'C:\Users\wangkai\Desktop\pythonwork\data\team.png')
    cv2.imshow('img1',img_1)
    cv2.imshow('img2',img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
