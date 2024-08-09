import numpy as np
import cv2, multiprocessing
from multiprocessing import shared_memory
import time


def show_image():
    i = 0
    while 1:
        i = i + 1

        existing_shm = shared_memory.SharedMemory(create=False, name='img')
        image_out1 = np.ndarray((300, 300, 3), dtype='uint8', buffer=existing_shm.buf)
        print(image_out1)
        time.sleep(1)
        if i > 50:
            break


def change_img():
    while True:
        time.sleep(5)
        existing_shm = shared_memory.SharedMemory(name='img')
        image_in2 = np.ndarray((300, 300, 3), dtype='uint8', buffer=existing_shm.buf)
        image_in2[:] = np.zeros((300, 300, 3), dtype='uint8')
        print('clear')


def print_list():
    shm_b = shared_memory.ShareableList(name='123')
    print(shm_b[0])  # ‘张三’
    print(shm_b[1])  # 2
    print(shm_b[2])  # ‘abc


if __name__ == '__main__':
    image = cv2.imread(r'C:\Users\33567\Desktop\test_batch0_labels.jpg')
    image = cv2.resize(image, (300, 300))
    shape = np.shape(image)
    dtype = image.dtype

    images = multiprocessing.Manager().dict()

    shm = shared_memory.SharedMemory(create=True, size=image.nbytes, name='img')  # 共享内存
    shm_l = shared_memory.ShareableList(['张三', 2, 'abc'], name='123')  # 共享列表

    image_in = np.ndarray(shape, dtype=dtype, buffer=shm.buf)  # 设置np存在shm.buf中
    image_in[:] = image.copy()

    a = multiprocessing.Process(target=show_image)
    b = multiprocessing.Process(target=change_img)
    c = multiprocessing.Process(target=print_list)
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()
