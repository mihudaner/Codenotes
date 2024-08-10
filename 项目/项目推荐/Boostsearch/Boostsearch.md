https://blog.51cto.com/byte/7427307

[OJ,boostsearch](https://gitee.com/xifeng026/project/tree/master)

# V1

OJ项目是一点点复制粘贴的，看懂了但是没有手敲

这从只看博客，不复制粘贴手敲，不然函数都不会用

## boost链接不到踩坑

### 安装boost

[Oj安装的boost](https://blog.csdn.net/challenglistic/article/details/129097988)

![image-20231109175444042](/home/wangkai/codenotes_ubuntu/项目/Boostsearch/img/image-20231109175444042.png)

不export BOOST_INCLUDE=/usr/local/include/boost
export BOOST_LIB=/usr/local/lib？



```
(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/project/Boostsearch$ g++ main.cpp -o main.o -lboost_thread -lboost_filesystem -lpthread -lboost_system -std=c++11 -I /usr/local/include/boost -L /usr/local/lib
/usr/bin/ld: /tmp/ccZ5Kp0a.o: in function `boost::filesystem::recursive_directory_iterator::recursive_directory_iterator(boost::filesystem::path const&)':
main.cpp:(.text._ZN5boost10filesystem28recursive_directory_iteratorC2ERKNS0_4pathE[_ZN5boost10filesystem28recursive_directory_iteratorC5ERKNS0_4pathE]+0x37): undefined reference to `boost::filesystem::detail::recursive_directory_iterator_construct(boost::filesystem::recursive_directory_iterator&, boost::filesystem::path const&, unsigned int, boost::system::error_code*)'
collect2: error: ld returned 1 exit status


(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/project/Boostsearch$ sudo rm -r /usr/local/lib/cmake/boost*
rm: 无法删除 '/usr/local/lib/cmake/boost*': 没有那个文件或目录


(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/下载/boost_1_78_0$ sudo ./bootstrap.sh --with-libraries=all --with-toolset=gcc


(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/下载/boost_1_78_0$ sudo ./b2 toolset=gcc

(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/下载/boost_1_78_0$ sudo ./b2 install


(base) wangkai@wangkai-Legion-Y9000P-IAH7H:~/project/Boostsearch$ g++ main.cpp -o main -lboost_thread -lboost_filesystem -lpthread -lboost_system -std=c++11 -I /usr/local/include/boost -L /usr/local/lib

```

```
 g++ main.cpp -o main -lboost_thread -lboost_filesystem -lpthread -lboost_system -std=c++11 -I /usr/local/include/boost -L /usr/local/lib
```



### [换源安装yum-修改了aptget配置文件](https://blog.csdn.net/qq_43029747/article/details/94874442)

 

```
sudo apt-get install yum
```

yum : 依赖: python-libxml2 但是它将不会被安装
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系



## cmakelist链接不到boost

### [cmakelist语法](https://blog.csdn.net/qq_43964318/article/details/124618520)

**find_package(Boost COMPONENTS thread filesystem system REQUIRED)**

- COMPONENTS，components：可选字段，表示查找的包中必须要找到的组件（components），如果有任何一个找不到就算失败，类似于 REQUIRED，导致 CMake 停止执行

  

- 其中具体查找库并给 XXX_INCLUDE_DIRS 和 XXX_LIBRARIES 两个变量赋值的操作由XXXConfig.cmake 模块完成。

  

- XXX_FOUND 代表库是否查找成功
  XXX_INCLUDE_DIRS 代表头文件的路径
  XXX_LIBRARIES 代表库文件的路径

  

- 默认搜索路径/usr/local/.......

```cmake
cmake_minimum_required(VERSION 3.0)

project(main)


set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O2 -Wall -lboost_thread -lboost_filesystem -lpthread -lboost_system -std=c++11 -I /usr/local/include/boost -L /usr/local/lib")
set(CMAKE_BUILD_TYPE Debug)

# 添加Boost库的查找
find_package(Boost COMPONENTS thread filesystem system REQUIRED)

# 将Boost库的头文件目录添加到包含路径中
include_directories(include ${Boost_INCLUDE_DIRS})

# 将Boost库的库目录添加到链接路径中
link_directories(${Boost_LIBRARY_DIRS})

include_directories(include /usr/local/include/boost)
link_directories(/usr/local/lib)

add_executable(main main.cpp)
target_link_libraries(main ${Boost_LIBRARIES})  # 必须加这个




```

### jsoncpp也是

```cmake
cmake_minimum_required(VERSION 3.0)

project(main)


set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O2 -Wall -lboost_thread -lboost_filesystem -lpthread -lboost_system  -ljsoncpp -std=c++11")
set(CMAKE_BUILD_TYPE Debug)

# 添加Boost库的查找
find_package(Boost COMPONENTS thread filesystem system REQUIRED)
# 将Boost库的头文件目录添加到包含路径中
include_directories(include ${Boost_INCLUDE_DIRS})
# 将Boost库的库目录添加到链接路径中
message(Boost_LIBRARIES)
message(${Boost_LIBRARIES})
link_directories(${Boost_LIBRARIES})

include_directories(/usr/include/)
link_directories(/usr/lib/)
# .a文件就是所需要的库，上两行就是在绝对地址上找到他
find_library(JSON_CPP libjsoncpp.a PATHS /usr/lib NO_DEFAULT_PATH)
message(JSON_CPP)
message(${JSON_CPP})  # 不知道为什么就是找错到/usr/local/lib/libjsoncpp.a

add_executable(main main.cpp)
target_link_libraries(main ${Boost_LIBRARIES} /usr/lib/libjsoncpp.a )


# 。file(GLOB sources CONFIGURE_DEPENDS *.cpp *.h)
# 。target_sources(main PUBLIC ${sources})
```



## [windows cmake](https://blog.csdn.net/X_trans/article/details/131914477)



## [fstream](https://blog.csdn.net/weixin_52591952/article/details/127283578)

### ifstram

```c++
std::ifstream in(src_path, std::ios::in | std::ios::binary);
            if (in.is_open() == false)
while (std::getline(in, line))
```

### ofstream

```c++
std::ofstream out(save_path, std::ios_base::out | std::ios_base::binary);
out.write(str.c_str(),str.size());//读哪里，读多长
//str.c_str() 是字符串STL转字符数组
```

## [jsoncpp语法](https://blog.csdn.net/qq_43441284/article/details/130983076)



## 静态成员变量

```c++
 class JiebaUtil
    {
    public:
        static void CutString(const std::string &src, std::vector<std::string> *out)
        {
            assert(out);
    	    jieba.CutForSearch(src, *out);
        }

    private:
        static cppjieba::Jieba jieba;
    };
    cppjieba::Jieba JiebaUtil::jieba(DICT_PATH, HMM_PATH, USER_DICT_PATH,
                            IDF_PATH, STOP_WORD_PATH);
    //静态成员类外初始化 变量类型 类名：：变量名
    //静态成员类内初始化必须是常量

```

只有const static 才可以类内初始化



## 单例模式

```c++
 class Index
 {
private:
        // 正排索引 -- 根据vector下标可以更加高效作为id找到内容
        std::vector<struct DocInfo> forward_index;
        // 倒排索引 一个关键字 可能在很多的文档中出现,一定是一个关键字和一组InvertedElem对应
        std::unordered_map<std::string, InvertedList> inverted_index;
		Index(){};                                  // 构造函数私有化
        Index(const Index &in) = delete;            // 禁止拷贝构造
        Index &operator=(const Index &in) = delete; // 禁止赋值拷贝
        //单个实例对象，由static Index *GetIndex()创建
        //所以叫设计为单例模式
        static Index *singleton_index; 
        static std::mutex mtx; // 创建一把锁
    

public:
        ~Index() {}
        static Index *GetInstance()//私有化的创建对象接口
        {
        // 线程不安全,加锁,可能两个线程同时进来发现没有创建单例就
        if (nullptr == singleton_index)
        {
            mtx.lock();
            if (singleton_index == nullptr)
            {
            singleton_index = new Index;
            }
            mtx.unlock();
        }
        return singleton_index;
        }
    Index *Index::singleton_index = nullptr;//类外初始化
    std::mutex Index::mtx;
}
```

只由一个私有化的函数接口创建唯一的一个静态对象



为什么singleton_index = new Index;析构不需要释放

我觉得还是因为这个指针是静态变量的原因，创建的对象成员其实没有指针存在就不需要析构释放

## 字符串指针和引用

```c++
std::string js;
std::string query = "to_low";
Searcher.Search(query,&js);
void Search(const std::string &query, std::string *json_string)
{
    ....
    *json_string = writer.write(root);
}

```

对的但是

```c++
std::string *js;
std::string query = "to_low";
Searcher.Search(query,js);
void Search(const std::string &query, std::string *json_string)
{
    ....
    *json_string = writer.write(root);
}

```

就报错，==字符串一般不用指针==

## httplib

注意get请求前面是有一个/的

```
svr.Get("hi", [](const Request& req, Response& res){
错误

svr.Get("/hi", [](const Request& req, Response& res){

```

## [w3school 在线教程](https://www.w3school.com.cn/index.html)



## 发送请求和解析json

```html
<script>
        function Search() {
            //是浏览器的弹出框，当点击搜索一下会弹出alert的内容
            //alert("hello js");
            //1.提取数据，$可以理解成JQuery的别称
            //()里面填写的是要提取谁里面的数据，提input里面的value
            let query = $(".container .search input").val();
            if(query == '' || query == null)
            {
                return;
            }
            console.log("query = " + query);//console 是浏览器的对话框，可以用来查看js数据
            //2.发送http请求,ajax:属于一个和后端进行数据交互的函数
            //type是请求的方法(GET,POSE)这里用GET，url就是自己的url后面加上/s?word=query
            //success:function(data)请求成功返回的参数就存在data中，相当于设置了一个回调
            $.ajax({
                type: "GET",
                url: "/s?word=" + query,
                success: function(data) {
                    console.log(data);   
                    BuildHtml(data);
                }
            });
        }
        function BuildHtml(data) {
            if(data == '' || data == null)
            {
                document.write("抱歉，没有查询到搜索内容");
                return;
            }
            //想重新构建一个网页信息，data是从http_server中返回的json_string
            let result_tag = $(".container .result");//获取网页中的result标签
            result_tag.empty();//清空历史搜索结果
            //类似于c++里面的for(auto e : result)
            for(let elem of data){
                let a_tag = $("<a>", {
                    text: elem.title, //text就代表标签内容
                    href: elem.url,  //设置跳转网页的url
                    target: "_blank" //设置跳转，即跳转到一个新的网页中
                });
                let p_tag = $("<p>", {
                    text: elem.desc
                });
                let i_tag = $("<i>", {
                    text: elem.url
                });
                let doc_tag = $("<div>", {
                    class: "docinfo"
                });
                a_tag.appendTo(doc_tag);//表示a_tag添加到doc_tag中
                p_tag.appendTo(doc_tag);
                i_tag.appendTo(doc_tag);
                doc_tag.appendTo(result_tag);//doc_tag要添加到result标签中
            }
        }
    </script>
```

$(".container .result") 是jQury语法

