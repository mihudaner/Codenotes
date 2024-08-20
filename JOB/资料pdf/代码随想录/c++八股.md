## static_cast move

```
dfs(pRoot, static_cast<DesiredType>(std::move(deep)));
```

## 如何修改const修饰的变量的值

> ### 方法1：使用`const_cast`
>
> `const_cast`可以移除`const`属性，使得你可以修改变量的值。但是这仅在变量原本不是`const`时才是安全的。如果变量本身就是`const`的，这么做是未定义行为。
>
> ```
> cpp复制代码void modifyConst(const int& value) {
>     int& nonConstValue = const_cast<int&>(value);
>     nonConstValue = 42;  // 修改变量的值
> }
> 
> int main() {
>     const int num = 10;
>     modifyConst(num);  // 修改num的值
>     // 未定义行为，因为num本身是const的
> }
> ```
>
> ### 方法2：使用`mutable`
>
> 如果你在一个类中，并且需要修改类中的`const`成员变量，可以使用`mutable`关键字。`mutable`关键字允许你在`const`方法中修改成员变量。
>
> ```
> cpp复制代码class MyClass {
> public:
>     MyClass(int v) : value(v) {}
> 
>     void modifyValue() const {
>         value = 42;  // 即使在const方法中，也可以修改mutable变量
>     }
> 
>     int getValue() const {
>         return value;
>     }
> 
> private:
>     mutable int value;
> };
> 
> int main() {
>     const MyClass obj(10);
>     obj.modifyValue();
>     // 可以安全地修改const对象中的mutable变量
>     return 0;
> }
> ```

## 静态成员变量在类外初始化



## [运算符重载](https://download.csdn.net/blog/column/12279145/129201512)



> 运算符重载前置++和后置
>
> 
>
> ChatGPT
>
> 在C++中，可以重载前置（`++a`）和后置（`a++`）递增运算符。这两者的重载方式略有不同。以下是如何分别重载前置和后置递增运算符的详细说明和示例代码。
>
> ### 前置递增运算符（`++a`）
>
> 前置递增运算符返回递增后的对象自身。
>
> #### 重载方法：
>
> ```c
> cpp复制代码class MyClass {
> public:
>     // 构造函数
>     MyClass(int value) : data(value) {}
> 
>     // 前置递增运算符重载
>     MyClass& operator++() {
>         ++data;
>         return *this;
>     }
> 
>     // 获取当前值
>     int getValue() const {
>         return data;
>     }
> 
> private:
>     int data;
> };
> ```
>
> ### 后置递增运算符（`a++`）
>
> 后置递增运算符在参数列表中使用一个 `int` 作为区分标志。这个参数不会被实际使用，只是用于区分前置和后置版本。后置递增运算符返回递增前的对象的副本。
>
> #### 重载方法：
>
> ```c
> cpp复制代码class MyClass {
> public:
>     // 构造函数
>     MyClass(int value) : data(value) {}
> 
>     // 后置递增运算符重载
>     MyClass operator++(int) {
>         MyClass temp = *this; // 创建当前对象的副本
>         ++data;               // 递增当前对象的值
>         return temp;          // 返回递增前的副本
>     }
> 
>     // 获取当前值
>     int getValue() const {
>         return data;
>     }
> 
> private:
>     int data;
> };
> ```

## 哈希冲突

```c
#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> myMap;

    // 插入元素
    myMap[1] = "one";
    myMap[2] = "two";
    myMap[3] = "three";

    // 获取键的哈希值
    int key = 2;
    auto hashValue = myMap.hash_function()(key);
    std::cout << "Hash value of key " << key << " is: " << hashValue << std::endl;

    // 查找键对应的桶
    size_t bucketIndex = myMap.bucket(key);
    std::cout << "Key " << key << " is in bucket: " << bucketIndex << std::endl;

    // 打印桶中的所有元素
    std::cout << "Bucket " << bucketIndex << " contains: ";
    for (auto it = myMap.begin(bucketIndex); it != myMap.end(bucketIndex); ++it) {
        std::cout << "(" << it->first << ", " << it->second << ") ";
    }
    std::cout << std::endl;

    return 0;
}
```

## vector和unordered_map的扩容

```c
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;
int main()
{
    vector<int> a;
    unordered_map<int, int> mp;
    cout << a.capacity() << endl;
    a.push_back(1);
    cout << a.capacity() << endl;
    a.push_back(1);
    cout << a.capacity() << endl;
    a.push_back(1);
    cout << a.capacity() << endl;

    cout << mp.bucket_count() << endl;
    mp[1] = 1;
    cout << mp.bucket_size(1) << endl;
    cout << mp.bucket_count() << endl;
    mp[2] = 1;
    cout << mp.bucket_size(1) << endl;
    cout << mp.bucket_count() << endl;
    mp[3] = 1;
    cout << mp.bucket_size(1) << endl;
    cout << mp.bucket_count() << endl;
    return 0;
}
```

## [STL destory](https://blog.csdn.net/weixin_30333885/article/details/99155382)

```c
#include <iostream>
#include <stdlib.h>
#include <unistd.h>
using namespace std;
class A
{
public:
	A()
	{
		data=new char[1000000];
	}
	~A()
	{
		//free the data memory
		delete []data;
	}
private:
	char *data;
};
int main(int argc,char* argv[])
{
	for(;;)
	{
		A *a=new A;
		std::allocator<A> allocat;
		allocat.deallocate(a,sizeof(A));
 
	}
	return 0;
}
```

> 　明显 这样的做法会出问题，运行到一定的时间内会抛出异常。所以deallocate只是释放对象内存，并没有调用对象的构造函数释放对象内的动态内存  这点要注意  如果调用了一个  allocat.destory(a); 程序就不会有bug了 
>
> 所以在C++中， 对象释放和对象内动态内存释放是需要注意的 弄不好 就会出现内存泄露现象。
>
> 这里的delete操作符号本身带有2个动作：调用[析构函数](https://so.csdn.net/so/search?q=析构函数&spm=1001.2101.3001.7020) 2释放内存。而::operator delete就只有释放内存。 deallocate函数就是基于operator delete函数封装的。 这点需要记住
>
> 可以通过看STL源码发现 ：像vector()的析构函数都是有2个操作： destory() 释放对象内的动态内存（如果有） deallocate是释放对象本身占有的内存  通过这2点  就能保证内存不能泄露了  嘿嘿  这节就说到这里哦  写这个也是为了记忆和方便以后查阅

```
uninitialized_copy 
destory
头文件都是memory
```

## 虚析构

> 调用了派生类的析构函数还会调用基类的虚析构函数么
>
> 
>
> ChatGPT
>
> 在C++中，当一个对象被销毁时，如果该对象的类有虚析构函数，基类和派生类的析构函数将按特定的顺序被调用。特别是，如果基类的析构函数被声明为虚函数，那么通过基类指针删除派生类对象时，将会首先调用派生类的析构函数，然后再调用基类的析构函数





## Vector插入对象

![image-20240715152920108](E:\codenotes\就业\代码随想录\img\image-20240715152920108.png)

可见插入是在另一段未初始化的内存构造了对象，然后释放了原有的对象



> 为什么要uninitialized_copy在未初始化的内存中构造对象不用构造函数构造对象
>
> ### 为什么不直接使用构造函数
>
> 直接使用构造函数会在已初始化的内存中构造对象，适用于大多数常见的高层次应用场景。但在一些需要细粒度内存控制的低层次应用中，比如实现自定义容器、内存池或其他高性能数据结构时，`std::uninitialized_copy` 和类似的函数（如 `std::uninitialized_fill`）提供了更灵活的控制。

## 容器的底层

![image-20240715153854037](E:\codenotes\就业\代码随想录\img\image-20240715153854037.png)

自定义priority_queue排序

```c
#include <iostream>
#include <queue>
#include <vector>

// 自定义比较函数对象（仿函数）
struct Compare {
    bool operator()(int lhs, int rhs) {
        return lhs > rhs; // 从小到大排序
    }
};

int main() {
    std::priority_queue<int, std::vector<int>, Compare> pq;

    pq.push(10);
    pq.push(5);
    pq.push(20);
    pq.push(1);

    while (!pq.empty()) {
        std::cout << pq.top() << " ";
        pq.pop();
    }

    return 0;
}

```

自定义set排序

```c
#include <iostream>
#include <set>

// 自定义比较函数对象（仿函数）
struct Compare {
    bool operator()(int lhs, int rhs) const {
        return lhs > rhs; // 降序排列
    }
};

int main() {
    // 使用自定义比较函数对象创建 set
    std::set<int, Compare> mySet = {10, 20, 30, 40, 50};

    for (int value : mySet) {
        std::cout << value << " ";
    }

    return 0;
}

```

自定义hash函数

```c
#include <iostream>
#include <unordered_map>
#include <string>

// 自定义哈希函数对象
struct CustomHash {
    std::size_t operator()(const std::string& key) const {
        std::size_t hash = 0;
        for (char c : key) {
            hash = hash * 31 + c; // 一个简单的哈希函数
        }
        return hash;
    }
};

int main() {
    // 使用自定义哈希函数的unordered_map
    std::unordered_map<std::string, int, CustomHash> myMap;
    myMap["apple"] = 1;
    myMap["banana"] = 2;
    myMap["cherry"] = 3;

    for (const auto& pair : myMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}

```

## 迭代器失效

> 如果我再for循环的同时push_back会不会因为扩容导致迭代器失效
> ChatGPT
> 是的，如果在 for 循环中使用 push_back 向 std::vector 添加元素，可能会导致迭代器失效。这是因为 std::vector 在需要扩容时会重新分配内存并移动已有的元素，这会使所有指向旧内存位置的迭代器失效。

