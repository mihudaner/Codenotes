#include <atomic>
#include "mingw.thread.h"
#include <iostream>
#include <sstream>
#include <vector>
#include <unistd.h> // POSIX sleep 函数
#include <chrono>   // 用于 std::chrono::milliseconds
using namespace std;
int n;

void print_vector(const vector<int> &v)
{
    // 输出数组内容
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << v[i] << " ";
    }
    std::cout << endl;
}

class MySpinLock
{
public:
    atomic_flag flag = ATOMIC_FLAG_INIT;
    void lock()
    {
        while (flag.test_and_set(memory_order_acquire));
    }
    void unlock()
    {
        flag.clear(memory_order_release);
    }
};

void thread_fun(MySpinLock &lock)
{
    lock.lock();
    cout << "thread_fun" << endl;
    //this_thread::sleep_for(chrono::milliseconds(1000)); // 让线程休眠 1 秒
    sleep(1);
    lock.unlock();
}

// int main()
// {
//     cout << "spinbox" << endl;
//     MySpinLock lock;

//     thread myThread1(thread_fun, ref(lock));
//     thread myThread2(thread_fun, ref(lock));

//     myThread1.join();
//     myThread2.join();

//     return 0;
// }

// 1 2 3 42 41
