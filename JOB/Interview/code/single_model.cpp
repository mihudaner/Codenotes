#include <iostream>
using namespace std;

class Singleton
{
private:
   
    static Singleton* ptr;
    Singleton(const Singleton & other) = delete;
    Singleton operator=(const Singleton & other) = delete;
    Singleton(){};

    class Des
    {
    public:
        Des(){}
        ~Des()
        {
            if(Singleton::ptr != NULL)
            {
                delete Singleton::ptr;
                Singleton::ptr = NULL;
            }
        }
    };
    static Des des;

public:
    int val = 0;
  
    static Singleton* instance()
    {
        return ptr;
    }
};

Singleton* Singleton::ptr = new Singleton();


int main()
{
    Singleton* a = Singleton::instance();
    cout << a->val++ << endl;

    Singleton* b = Singleton::instance();
    cout << b->val++ << endl;
}

