#include <iostream>
#include <sstream>
using namespace std;
int n;

template <class T>
class vector
{
public:
    vector() : m_data(nullptr), m_size(0), m_capacity(0)
    {
    }
    ~vector()
    {
        if (m_data != nullptr)
        {
            delete[] m_data;
        }
        m_size = 0;
        m_capacity = 0;
    }

    void push_back(T &value)
    {
        if (m_size < m_capacity)
        {
            m_data[m_size] = value;
            m_size++;
            return;
        }
        if (m_capacity == 0)
            m_capacity = 1;
        else
            m_capacity *= 2;

        T *data = new T[m_capacity];
        for (int i = 0; i < m_size; i++)
        {
            data[i] = m_data[i];
        }

        if (m_data != nullptr)
        {
            delete[] m_data;
            m_data = nullptr; // 防止指针悬挂，指向被释放的空间
        }
        m_data = data;
        m_data[m_size++] = value;
    }

    void pop_back()
    {
        if (m_size > 0)
            m_size--;
    }

    // 拷贝构造函数
    vector(const vector<T> &other) : m_data(nullptr), m_size(other.m_size), m_capacity(other.m_capacity)
    {
        if (m_capacity > 0)
        {
            m_data = new T[m_capacity];
            for (int i = 0; i < m_size; ++i)
            {
                m_data[i] = other.m_data[i];
            }
        }
    }

    // 赋值运算符重载
    vector<T> &operator=(const vector<T> &other)
    {
        if (this == &other)
            return *this; // 防止自赋值

        delete[] m_data; // 释放已有资源

        m_size = other.m_size;
        m_capacity = other.m_capacity;
        m_data = nullptr;

        if (m_capacity > 0)
        {
            m_data = new T[m_capacity];
            for (int i = 0; i < m_size; ++i)
            {
                m_data[i] = other.m_data[i];
            }
        }

        return *this;
    }

     // 移动构造函数
    vector(vector<T>&& other) noexcept // 声明一个不会抛出异常的函数
        : m_data(other.m_data), m_size(other.m_size), m_capacity(other.m_capacity)
    {
        other.m_data = nullptr;
        other.m_size = 0;
        other.m_capacity = 0;
    }

    // 访问
    T &at(int index)
    {
        if (index < 0 || index >= m_size)
            throw std::out_of_range("out of range");
        return m_data[index];
    }

    T &front() // 返回第一个
    {
        // if(m_data == nullptr)
        //     throw std::out_of_range("out of range");  可以抛出合适的异常，可能不是outofrange
        return m_data[0];
    }

    T &back() // 返回都是&引用类型，这样就可以直接对数据进行修改
    {
        return m_data[m_size - 1];
    }

    T &operator[](int index) // 使用重载  如果这里放在其他文件进行定义 那么就要加上作用域  比如  template <class T>  然后函数前面加上 vector<T>
    {
        return m_data[index];
    }

    T &operator[](int index) const // 使用重载  如果这里放在其他文件进行定义 那么就要加上作用域  比如  template <class T>  然后函数前面加上 vector<T>
    {
        return m_data[index];
    }

    const int size() const
    {
        return m_size;
    }

private:
    T *m_data; // 指向T类型的指针  这里如果T是 int 就可以理解为什么样的数组，
    int m_size;
    int m_capacity;
};

// template<class T>
// vector<T>::vector()
// {

// }

void print_vector(const vector<int> &v)
{
    // 输出数组内容
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << v[i] << " ";
    }
    std::cout << endl;
}

int main()
{
    string line;
    getline(std::cin, line);      // 读取一行文本
    std::istringstream iss(line); // 将行文本放入字符串流中
    int num;
    vector<int> nums;
    while (iss >> num)
    {                        // 从字符串流中读取数字
        nums.push_back(num); // 将数字添加到向量中
    }
    vector<int> nums2(nums);
    print_vector(nums2);
    return 0;
}

// 1 2 3 42 41
