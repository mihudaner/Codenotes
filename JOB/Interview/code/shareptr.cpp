#include<iostream>
using namespace std;

template<class T>
class Node
{
public:
    Node(){
        cnt = new int(1);
    };
    Node(T other):{
        ptr = new T(other)
        cnt = new int(1);
    };
    Node(const Node& other){
        ptr = new T(*other.ptr);
        cnt = other->cnt;
    };
    ~Node(){
        if(--(*cnt)==0)
        {
            delete ptr;
            delete cnt;
        }
    };
    Node(const Node&& other){
        ptr = other.ptr;
        delete other.ptr;
        other.ptr = nullptr;
        cnt = *(other.cnt);
    };
    operator=(const Node& other)
    {
        ptr = other.ptr;
        cnt = ++*(other->cnt);
    };
private:
    T* ptr;
    int* cnt;
};

int main()
{
    Node* a = new Node(1);
    Node* a1 = new Node(2);
    Node* a2 = new Node(3);
    Node* a3 = new Node(4);
    Node* a4 = new Node(5);
    return 0;
}