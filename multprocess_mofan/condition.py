"""
threadiong.Condition
可以把Condiftion理解为一把高级的锁，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。threadiong.Condition在内部维护一个锁对象（默认是RLock），可以在创建Condigtion对象的时候把锁对象作为参数传入。
Condition也提供了acquire, release方法，其含义与锁的acquire, release方法一致，其实它只是简单的调用内部锁对象的对应的方法而已。Condition还提供了如下方法(特别要注意：这些方法只有在占用锁(acquire)之后才能调用，否则将会报RuntimeError异常。)：

Condition.wait([timeout]):
wait方法释放内部所占用的锁，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。当线程被唤醒并重新占有锁的时候，程序才会继续执行下去。

Condition.notify():
唤醒一个挂起的线程（如果存在挂起的线程）。注意：notify()方法不会释放所占用的锁。

Condition.notify_all()或Condition.notifyAll()
唤醒所有挂起的线程（如果存在挂起的线程）。注意：这些方法不会释放所占用的锁
"""
import threading
import time

max_goods_num = 10
min_goods_num = 4
con = threading.Condition()
num = 0


class Producer(threading.Thread):
    def __init__(self, con):
        self.con = con
        super().__init__()

    def run(self):
        global num
        print("*" * 50)
        print("Coming in Producer ", time.ctime())
        self.con.acquire()
        for _ in range(max_goods_num):
            print("----------进入循环生成物品程序------------")
            print("开始生成物品")
            num += 1
            print("资源池里面物品的个数为：{}".format(num))
            time.sleep(1)
            if num == 5:
                print("资源池里面物品的个数已经到达五个, 无法继续生成了")
                self.con.notify()
                self.con.wait()

        self.con.release()
        print("Producer run exit")


class Consumer(threading.Thread):
    def __init__(self, con):
        self.con = con
        super().__init__()

    def run(self):
        print("*" * 50)
        print("Coming in Consumer ", time.ctime())
        self.con.acquire()
        global num
        while num:
            print("----------进入循环消耗物品程序------------")
            num -= 1
            print("资源池里面物品剩余：{}".format(num))
            time.sleep(0.5)
            if num < min_goods_num:
                print("资源池里面物品数量小于 min_goods_num，需要添加！")
                self.con.notify()
                self.con.wait(6)

        self.con.release()
        print("Consumer run exit")


p = Producer(con)
c = Consumer(con)
p.start()
c.start()