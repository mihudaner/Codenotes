#include <vector>
#include <thread>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include "mingw.thread.h"
#include "mingw.mutex.h"
#include "mingw.condition_variable.h"

using namespace std;
mutex mx;
condition_variable cv;
int flag = 0;

void printA()
{
    unique_lock<mutex> lock(mx);
    int cnt = 10;
    while(cnt--)
    {
        cv.wait(lock,[&](){return flag==0;});
        cout << 'A' <<endl;
        flag = 1;
        cv.notify_all();
    }
}

void printB()
{
    unique_lock<mutex> lock(mx);
    int cnt = 10;
    while(cnt--)
    {
        cv.wait(lock,[&](){return flag==1;});
        cout << 'B' <<endl;
        flag = 2;
        cv.notify_all();
    }
}

void printC()
{
   unique_lock<mutex> lock(mx);
    int cnt = 10;
    while(cnt--)
    {
        cv.wait(lock,[&](){return flag==2;});
        cout << 'C' <<endl;
        flag = 0;
        cv.notify_all();
    }
}

int main()
{
    thread A(printA);
    thread B(printB);
    thread C(printC);
    A.join();
    B.join();
    C.join();
    return 0;
}

