import multiprocessing
import time

'''
由于Pipe之间的通信时通过，in_conn.send()、out_conn.recv() 这种方式进行通信的，
因此如果当某一方调用了 .recv() 函数但一直没有另外的端口使用 .send() 方法的话，recv() 函数就会阻塞住。为了避免程序阻塞，

传过去的对象和原来的对象不是一个了
'''


class dog():
    color = 'green'
    weight = 10


def proc1(pipe):
    dog1_send = dog
    time.sleep(3)
    pipe.send(dog1_send)
    print("send: dog")
    time.sleep(3)
    print(dog1_send.weight)


def proc2(pipe):
    while True:
        dog1_recv = pipe.recv()
        print("proc2 rev:", dog1_recv.weight)
        dog1_recv.weight = 20
        print("接受端修改weigt=20")
        time.sleep(1)


if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
