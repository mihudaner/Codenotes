#include <vector>
#include <thread>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include "mingw.thread.h"
#include "mingw.mutex.h"
#include "mingw.condition_variable.h"
/*
定义线程池类：接下来定义线程池类，其中包含了线程池的管理逻辑，
如线程的创建、销毁、任务的添加等。线程池类需要包含一个线程池容器，用于存放线程对象。
*/

class Task
{
public:
    void execute()
    {
        std::cout << "Task is excuting" << std::endl;
    }
};

using namespace std;
class ThreadPool
{
public:
    ThreadPool(size_t numThreads);
    ~ThreadPool();
 
    void addTask(Task* task);
private:
    vector<std::thread> workers;  // 线程池中的线程
    queue<Task*> tasks;           // 任务队列
    mutex queueMutex;             // 保护任务队列的互斥量
    condition_variable condition; // 用于线程间通信的条件变量
    bool stop;                         // 标志线程池是否停止的标志位
};

ThreadPool::ThreadPool(size_t numThreads)
: stop(false)
{
    for(size_t i = 0; i < numThreads; ++i) 
    {
        workers.emplace_back([this] {
            while(true)
            {
                Task* task = nullptr;
                // 此线程取任务的时候  别的线程不可以取 所以必须上锁
                // 其他线程无法同时访问任务队列
                std::unique_lock<std::mutex> lock(queueMutex);
                // condition调用wait方法 使线程在条件变量condition上等待 
                // 当不满足条件时 会释放锁lock 满足条件时(stop为true 或 tasks不为空 满足之一时) 重新获取lock 并向下继续执行
                // 假如此时没有任务了 线程会阻塞在这里 直到任务队列有新任务到来时 该线程会被再次激活
                condition.wait(lock, [this] {return stop || !tasks.empty();});
                // 线程池停止 且 任务队列为空时 直接返回 默认情况下stop为false
                if(stop && tasks.empty())
                {
                    cout << "workers out! " <<endl;
                    return;
                }
                // 获取并执行任务
                task = tasks.front();
                tasks.pop();
                task->execute();
                delete task;
            }
        });
    }
}
 
ThreadPool::~ThreadPool()
{
    {
        std::unique_lock<std::mutex> lock(queueMutex);
        stop = true;

        // 清空任务队列
        while (!tasks.empty()) {
            Task* task = tasks.front();
            tasks.pop();
            delete task;
        }
    } // 这里结束作用域，lock 会自动释放!!
    condition.notify_all();
    for(std::thread& work : workers)
    {
        if (work.joinable()) {
            work.join();
        }
    }
}
 
void ThreadPool::addTask(Task* task)
{
    std::unique_lock<std::mutex> lock(queueMutex);
    tasks.push(task);
    // 向等待condition条件变量的一个线程发出通知
    // 告诉它有新的任务可执行 可以取出任务
    condition.notify_one();
}
 

// int main()
// {
//     ThreadPool pool(4);   // 创建一个包含4个线程的线程池
//     cout << 1 <<endl;
//     // 添加任务到线程池
//     for(int i = 0; i < 8; ++i)
//     {
//         pool.addTask(new Task());
//     }
//     cout << 1 <<endl;
//     return 0;
// }

