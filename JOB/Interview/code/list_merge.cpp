#include <iostream>
using namespace std;

class myList
{
    public:
    int val;
    myList* next;
    myList(int x):val(x){}
};


myList* merge(myList* head1,myList* head2)
{
    myList* res = new myList(1);
    myList* head = res;
    while(head1!= nullptr&&head2!= nullptr)
    {
        if(head1->val<head2->val)
        {
            head ->next  = head1;
            head = head ->next;
            head1 = head1->next;
        }
        else
        {
            head ->next  = head2;
            head = head ->next;
            head2 = head2->next;
        }
    }
    if(head1!= nullptr) head ->next  = head1;
    if(head2!= nullptr) head ->next  = head2;
    return res->next;

}

// int main(void) {

//     myList* node0 = new myList(0);
//     myList* node1 = new myList(1);
//     myList* node2 = new myList(2);
//     myList* node3 = new myList(3);

//     myList* node4 = new myList(1);
//     myList* node5 = new myList(4);
//     node0->next = node1;
//     node1->next = node2;
//     node2-> next= node3;
//     node3->next = nullptr;
//     node4->next = node5;
//     node5->next = nullptr;

//     auto node = merge(node0, node4);
//     while (node != nullptr) {
//         cout << node->val << endl;
//         node = node->next;
//     }

//     return 0;
// }
