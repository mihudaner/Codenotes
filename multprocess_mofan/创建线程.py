import threading
import time


def thread_job1():
    """
    第二个线程停留3秒
    :return:
    :return:
    """
    print('T1 start\n')
    for i in range(30):
        time.sleep(0.1)
    print('T1 finish\n')


def thread_job2():
    """
    第二个线程停留1秒
    :return:
    """
    print('T2 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T2 finish\n')


def main():
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

    thread1 = threading.Thread(target=thread_job1, name='T1')
    thread2 = threading.Thread(target=thread_job2, name='T2')

    thread1.start()
    thread2.start()

    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

    print('thread2.join\n')
    thread2.join()  # 加入主进程

    print('thread1.join\n')
    thread1.join()  # 加入主进程,接在start后

    print('main all done\n')


if __name__ == '__main__':
    main()
