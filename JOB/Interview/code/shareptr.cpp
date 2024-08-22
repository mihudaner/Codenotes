#include<iostream>
#include<memory>
using namespace std;

template<class T>
class Shareptr
{
public:
    Shareptr(){
        cnt = new int(1);
    };
    Shareptr(T other){
        ptr = new T(other);
        cnt = new int(1);
    };
    Shareptr(const Shareptr& other){
        ptr = other.ptr;
        cnt = other.cnt;
        ++*cnt;
    };
    ~Shareptr(){
        if(--(*cnt)==0)
        {
            delete ptr;
            delete cnt;
        }
    };
    Shareptr(const Shareptr&& other){
        ptr = other.ptr;
        delete other.ptr;
        other.ptr = nullptr;
        cnt = *(other.cnt);
    };
    operator=(const Shareptr& other)
    {
        if(--(*cnt)==0)
        {
            delete ptr;
            delete cnt;
        }
        ptr = other.ptr;
        cnt = ++*(other->cnt);
    };
private:
    T* ptr;
    int* cnt;
};

int main()
{   
    int *a = new int(8);
    
    shared_ptr<int> p1;
    auto p2 = std::make_shared<int>(2);
    cout << p1.use_count() <<endl;
    return 0;
}