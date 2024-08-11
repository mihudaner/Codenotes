#include <iostream>
#include <sstream>
using namespace std;
int n;

template<class T>
class vector
{
private:
    /* data */
public:
    
    int size=0;
    T* data;
    int capcity=0;
    int len=0;
    vector()
    {
        data = NULL;
        len = size = 0;
    }
    ~vector(){};
    vector(int _len)
    {
        data = new T[_len];
        len = _len;
        size = 0;
    }
    const vector& push_back(const T tmp)
    {
        if(size >= len)
        {
            T* newData = new T[len*2 + 1];
            memcpy(newData, data, len*sizeof(T));
            delete []data;
            data = newData;
            len = 2*len + 1;
        }
        data[size++] = tmp;
        return *this;
    }
    void pop_back();
    T& operator[](int index)
    {
        return data[index];
    }
     // 常量版本
    const T& operator[](int index) const
    {
        return data[index];
    }
};


void print_vector(const vector<int> &v)
{
     // 输出数组内容
    for (int i=0;i<v.size;i++)
    {
        std::cout << v[i] << " ";
    }
    std::cout << endl;
}

int main()
{
    string line;
    getline(std::cin, line); // 读取一行文本
    std::istringstream iss(line); // 将行文本放入字符串流中
    int num;
    vector<int> row_nums;
    while (iss >> num)
    {                        // 从字符串流中读取数字
        row_nums.push_back(num); // 将数字添加到向量中
    }
    print_vector(row_nums);
    return 0;
}

// 1 2 3 42 41



