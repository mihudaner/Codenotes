#include<iostream>
using namespace std;


class Node
{
public:
    Node(int x):val(x){};
    Node* next = nullptr;
    int val;
};

Node* reverse(Node* head)
{
    Node* pre = nullptr;
    Node* nd;
    while(head!=nullptr)
    {
        nd = head->next;
        head->next = pre;
        pre = head;
        head = nd;
    }
    return pre;
}

// int main()
// {
//     Node* a = new Node(1);
//     Node* a1 = new Node(2);
//     Node* a2 = new Node(3);
//     Node* a3 = new Node(4);
//     Node* a4 = new Node(5);
//     a->next = a1;
//     a1->next = a2;
//     a2->next = a3;
//     a3->next = a4;
//     a = reverse(a);
//     while(a!=nullptr)
//     {
//         cout << a->val <<endl;
//         a = a->next;
//     }
//     return 0;
// }