import multiprocessing
import time

'''
pipe可以双通道
'''


def proc1(pipe):
    x = 10
    pipe.send(x)
    print("proc1 send: x")
    print("proc1 recv:", pipe.recv())


def proc2(pipe):
    x = 20
    recv = pipe.send(x)
    print("proc2 send: x")
    time.sleep(3)
    print("proc2 recv:", pipe.recv())


if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
