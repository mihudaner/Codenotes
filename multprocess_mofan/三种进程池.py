import multiprocessing as mp
import time

# pool进程池
'''  
map函数说明
    x=[i for i in range(10)]
    def job(x):
        return x*x
    x= map (job,x)
结果：
    x
    <map object at 0x000001DA4336E530>
    list(x)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''


def delay_return(msg):
    print('mas:', msg)
    time.sleep(2)
    print('end:', msg)
    return msg


def delay(msg):
    print('mas:', msg)
    time.sleep(2)
    print('end:', msg)


def multicore_map():
    pool = mp.Pool()
    # pool = mp.Pool(processes=3)
    print('pool begin 1')
    res = pool.map(delay_return, range(10))  # 直接阻塞，map:（阻塞到任务列表中所有任务完成再往下执行 map）
    print('pool end 1')
    print(res)

    print('pool begin 2')
    res = pool.map(delay_return, range(20))  # 直接阻塞，map:（阻塞到任务列表中所有任务完成再往下执行 map）
    print('pool end 2')
    print(res)


def multicore_async():
    pool = mp.Pool()
    x = [pool.apply_async(delay, (i,)) for i in range(10)]
    print('没有返回值' + str(x))
    pool.close()
    pool.join()  # 加了join就会阻塞在这一直到所有任务计算完，类似map，去掉就是每个任务在get阻塞，类似async_return
    for result in x:
        print(result.get())


def multicore_async_return():
    pool = mp.Pool()
    mult_res = [pool.apply_async(delay_return, (i,)) for i in range(10)]  # 异步往里丢任务，异步返回结果
    print('ok')
    print([res.get() for res in mult_res])  # 验证了apply_async会在get地方阻塞


def run_async_return():
    print('multicore_async_return start')
    multicore_async_return()
    print('multicore_async_return over')


def run_async():
    print('multicore_async start')
    multicore_async()
    print('multicore_async over')


def run_map():
    print('multicore_map start')
    multicore_map()
    print('multicore_map over')


if __name__ == '__main__':
    # run_map()
    run_async()
