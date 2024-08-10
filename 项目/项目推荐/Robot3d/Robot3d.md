



# Robot3D

## [VS+qt配置](https://blog.csdn.net/MelyLenient/article/details/123854069)



## [改终端输出](https://blog.csdn.net/weixin_68161781/article/details/127336255?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-127336255-blog-131726713.235%5Ev38%5Epc_relevant_sort_base2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-127336255-blog-131726713.235%5Ev38%5Epc_relevant_sort_base2&utm_relevant_index=6)





# 添加osg头文件和链接库

==添加作者编译好的但是最后osgqt运行报错dll,排查是qt库连接上运行不行，感觉是环境问题最后自己试试cmake==

## [Visual Studio添加第三方库的实现步骤](https://www.jb51.net/program/292485yzj.htm)

最后不要

![image-20231127214417696](E:\codenotes\c++\Robot3d\img\image-20231127214417696.png)

会报错没有  ；libxl32.obj 因为lib路径里没有

## [osg环境部署 OSG3.6.5+vs2017+win10_x64](https://blog.csdn.net/qq_43718758/article/details/129486298)

直接操作的四和五-导入作者编辑好的库

##  “QOpenGLWidget”: No such file or directory

![image-20231127215503314](E:\codenotes\c++\Robot3d\img\image-20231127215503314.png)

在D:\Soft\Qt5.12.12\5.12.12\msvc2017_64\include\QtOpenGL下

所以环境里只有D:\Soft\Qt5.12.12\5.12.12\msvc2017_64\include\

所以==#include <QtOpenGL/QGLWidget>==

```
    #include <QGLWidget>       --------- ->          #include <QtOpenGL/QGLWidget>
```



## vcruntime140.dll发生访问冲突

<img src="E:\codenotes\c++\Robot3d\img\image-20231128212249717.png" alt="image-20231128212249717" style="zoom: 80%;" />

尝试重新编译

<img src="E:\codenotes\c++\Robot3d\img\image-20231129111124592.png" alt="image-20231129111124592" style="zoom: 50%;" />

把这个从第一个改成第二个就好了，但是其他代码还是会报错



# [常见vs报错](https://blog.csdn.net/LebronBear/article/details/124036654)



## vs第三方库链接报错一堆无法解析的外部命令

https://blog.csdn.net/qq_43718758/article/details/129486298





![image-20231130110008662](E:\codenotes\c++\Robot3d\img\image-20231130110008662.png)

![image-20231128085517587](E:\codenotes\c++\Robot3d\img\image-20231128085517587.png)

```
%(AdditionalDependencies)
$(Qt_LIBS_)
OpenThreadsd.lib
osgd.lib
osgDBd.lib
osgUtild.lib
osgGAd.lib
osgViewerd.lib
osgTextd.lib
osgWidget.lib
osgWidgetd.lib
osgUI.lib
osgUId.lib
osgViewer.lib
osgViewerd.lib
osgQt5.lib
```



## 找不到dll

![image-20231128085528208](E:\codenotes\c++\Robot3d\img\image-20231128085528208.png)

添加环境变量E:\project\c++\Robot3d\osgLIB\build\bin，重新打开vs

### ![image-20231128085820749](E:\codenotes\c++\Robot3d\img\image-20231128085820749.png)

又找不到zlibd.dll

一样搜索加环境变量



## 项目属性没有qt

![image-20231129011622900](E:\codenotes\c++\Robot3d\img\image-20231129011622900.png)



## 库添加opengl

![image-20231129190742383](E:\codenotes\c++\Robot3d\img\image-20231129190742383.png)

![image-20231129193721963](E:\codenotes\c++\Robot3d\img\image-20231129193721963.png)

## ==动态链接库 xd.lib x.lib==

![image-20231130144929857](E:\codenotes\c++\Robot3d\img\image-20231130144929857.png)

所以说最好带d结尾的库和realse不带d结尾的lib库可以分两个文件夹

==release模式千万不要加入带d结尾的库，带d结尾的debug模式，就会报各种奇怪的dll错误==

![image-20231130144812662](E:\codenotes\c++\Robot3d\img\image-20231130144812662.png)



![image-20231130144737172](E:\codenotes\c++\Robot3d\img\image-20231130144737172.png)



# 自己cmake

## [cmake osgQT](https://blog.csdn.net/qq_38697743/article/details/120808066)

[用的是旧版本](https://blog.51cto.com/SpaceVision/5205123)

![image-20231130130856269](E:\codenotes\c++\Robot3d\img\image-20231130130856269.png)

https://github.com/mathieu/osgQt

![image-20231129000901631](E:\codenotes\c++\Robot3d\img\image-20231129000901631.png)

![image-20231129001932238](E:\codenotes\c++\Robot3d\img\image-20231129001932238.png)





[无法打开输入文件“optimized.lib”](https://wenku.baidu.com/view/2c15da045a0102020740be1e650e52ea5518ceac.html?_wkts_=1701189046250&bdQuery=%E7%BC%96%E8%AF%91osgQt%E7%9A%84%E6%97%A7%E7%89%88%E6%9C%AC)

​		

![image-20231129003142792](E:\codenotes\c++\Robot3d\img\image-20231129003142792.png)

![image-20231129015342692](E:\codenotes\c++\Robot3d\img\image-20231129015342692.png)





### cmake一堆LINK错误

![image-20231129013651379](E:\codenotes\c++\Robot3d\img\image-20231129013651379.png)



## [Windows 下编译安装 OSG 及 osgQt](https://www.imwtx.com/archives/193/)

==讲的很细  Osg3.6.5==

本篇非常麻烦，博主用QtCreator作为IDE，因为Osg3.6.3放弃对osgQt的支持，集成起来比较繁琐



作者osg库应该是Osg3.6.3之前，然后支持老版的osgQ

不能使用感觉应该是因为作者是qt5.9编译的库，支持老版的osgQt

而我qt.5.12.6报错 qtcore.dll可能qt版本太高不支持老版的osgQt



==其实是debug报错release不报错==

重新cmake也不行，有的说是库debug和release不要放在一起

## [修改release断点不停](https://blog.csdn.net/weixin_41079881/article/details/123095462)

# 语法

## 三大特性

*封装、继承、多态*

## 函数重载

在C++中，根据参数类型的不同调用不同函数的特性被称为**函数重载**（Function Overloading）。函数重载允许你定义多个具有相同名称但参数列表不同的函数。编译器根据调用的函数参数类型或数量来确定要调用的具体函数



## [虚函数](https://blog.csdn.net/Dasis/article/details/121047964)实现多态

纯虚  virtual   func = 0

父类虚函数 子类重新实现多态

<img src="E:\codenotes\c++\Robot3d\img\image-20231129112634254.png" alt="image-20231129112634254" style="zoom: 67%;" />

```c++
#include<iostream>
using namespace std;

// 动物类
class Animal
{
public:
	// 虚函数 virtual
	virtual void speak()
	{
		cout << "动物在说话" << endl;
	}
};

// 猫类
class Cat :public Animal
{
public:
	// 重写：函数返回值类型 函数名 参数列表 三个完全相同
	void speak()
	{
		cout << "小猫在说话" << endl;
	}
};

//狗类
class Dog :public Animal
{
public:
	void speak()
	{
		cout << "小狗在说话" << endl;
	}
};

// 我们希望传入什么对象，那么就调用什么对象的函数
// 如果函数地址在编译阶段就能确定，那么静态联编
// 如果函数地址在运行阶段才能确定，就是动态联编

// 执行说话的函数
// 地址早绑定，在编译阶段就确定函数地址
// 如果想执行让猫说话，那么这个函数地址就不能提前绑定，需要在运行阶段进行绑定，地址晚绑定
void dospeak(Animal& animal)// 类似Animal &animal=cat，父类引用指向子类的传递对象
{
	animal.speak();// 加了virtual后，由于加入的对象不同，确定不同函数地址
}


int main(int argc, char* argv[])
{
    #include<vector>

    Cat cat;
    dospeak(cat);  //小猫说话

    Dog dog;
    dospeak(dog);   //小狗说话  

    vector<Animal*> anis;
    anis.push_back(&cat);
    anis.push_back(&dog);

    for (Animal* a : anis)
    {
        a->speak();   //小猫说话    小狗说话  
    }
}

```

所以父类函数应该也是一个指针指向子类的函数地址了

## [虚继承](https://blog.csdn.net/weixin_61857742/article/details/127344922)

![img](https://i0.hdslb.com/bfs/article/5ba1a5a42e36a520bc956b6c090a4a882fd7c812.png@1256w_868h_!web-article-pic.avif)

继承的是一个虚基表

vbptr 指向 vbtable（虚 基类 表），表中记录了一个偏移量，vbptr+偏移量 就是唯一继承的 m_Age 的地址

![image-20231129112141071](E:\codenotes\c++\Robot3d\img\image-20231129112141071.png)

```c++
1 //动物类
 2 class Animal
 3 {
 4 public:
 5     int m_Age;
 6 };
 7 
 8 //利用虚继承，可以解决菱形继承的问题
 9 //继承方式之前，加上关键字virtual，变为虚继承
10 //被虚继承的 Animal 类，称为虚基类
11 //羊类
12 class Sheep :virtual public Animal
13 {};
14 //驼类
15 class Camel :virtual public Animal
16 {};
17 //草泥马类
18 class Alpaca :public Sheep, public Camel
19 {};
20 
21 void test01()
22 {
23     Alpaca a1;25     //当菱形继承，两个父类拥有相同成员，需要加作用域区分
26     a1.Sheep::m_Age = 18;
27     a1.Camel::m_Age = 28;
28     cout << "a1.Sheep::m_Age = " << a1.Sheep::m_Age << endl;
29     cout << "a1.Camel::m_Age = " << a1.Camel::m_Age << endl;
30 
31     cout << "a1.m_Age = " << a1.m_Age << endl;　　//此时可以直接访问到 a1.m_Age 了
32 }
33 
34 int main()
35 {
36     test01();
37     return 0;
38 }
```



## [QT命名空间](https://blog.csdn.net/weixin_40583088/article/details/126863248)



## QT的前置声明

在你提供的代码中，确实没有直接使用 QT_NAMESPACE::QListWidget 的形式，
这可能是因为 QListWidget 类型是在全局命名空间（global namespace）中可见的
在这种情况下，前置声明 class QListWidget; 就足够了，而不需要使用 QT_NAMESPACE。
这通常是 Qt 中的一种约定。这有助于减小头文件的依赖关系，提高编译速度。

头文件前置声明，源文件里再添加头文件加快编译速度



## connect

```
 connect(textEdit->document(), &QTextDocument::contentsChanged, this, &CodeEditWidget::documentWasModified);
```



## QT继承父类初始化

```c++
MainWindow::MainWindow(QWidget* parent) :
    //构造函数初始化列表
    QMainWindow(parent),    //继承父类初始化
    ui(new Ui_MainWindow),   //初始化成员
    listWidget(new QListWidget),
    stackedWidget(new QStackedWidget),
    dockWidget(new QDockWidget),
    codeEditWidget(new CodeEditWidget)
```

## static_cast

```
在你提供的代码中，static_cast<Shape*>(*res) 尝试将 *res 转换为 Shape* 类型的指针。这种类型的转换通常用于将基类指针指向派生类对象的情况。
```

智能指针和dynamic_cast？



对于你的情况，如果你确定 `res` 的类型是 `Shape` 或其派生类，并且不需要运行时类型检查，那么 `static_cast` 是合适的选择。如果你需要进行安全的运行时类型检查，建议使用 `dynamic_cast`



C风格的强制类型转换 `(Shape*)res` 是一种旧式的类型转换语法，也称为C风格的强制类型转换。尽管它在某些情况下是有效的，但不推荐使用，因为它具有较低的类型安全性，并且在面对继承层次结构时可能导致未定义的行为。

## GM

```text
GM代码（Geometric Manufacturing Code）是一种用于数控机床的编程语言，用于控制机床执行特定的运动和操作。GM代码的格式和含义可能因制造商和机床型号而异。以下是一个简单的GM代码示例，演示了一些常见的运动和操作：

plaintext
Copy code
% O1000 (Program Start)
G90 (Set to Absolute Programming)
G54 (Work Coordinate System 1)
S500 (Set Spindle Speed to 500 RPM)
M03 (Start Spindle Clockwise)
G00 X100 Y50 Z20 (Rapid Positioning to X=100, Y=50, Z=20)
G01 Z-5 F100 (Linear Interpolation to Z=-5 at Feed Rate 100)
G01 X120 Y70 F150 (Linear Interpolation to X=120, Y=70 at Feed Rate 150)
G02 X150 Y50 I10 J0 F100 (Clockwise Circular Interpolation to X=150, Y=50 with Center at X=160, Y=50 at Feed Rate 100)
G00 Z20 (Rapid Positioning to Z=20)
M05 (Stop Spindle)
M30 (Program End)
%
在这个简单的GM代码示例中：

% 表示程序的开始和结束。
O1000 是程序的名称。
G90 设置为绝对编程。
G54 设置工作坐标系。
S500 设置主轴速度为500 RPM。
M03 启动主轴正转。
G00 是快速定位运动。
G01 是线性插补运动。
G02 是顺时针圆弧插补运动。
Z-5 表示在Z轴上的移动。
F100, F150 是进给速率。
I10, J0 是圆弧的中心偏移。
M05 停止主轴。
M30 结束程序。
请注意，GM代码的确切含义和语法可能因制造商而异。在实际应用中，应根据具体的机床和控制系统来编写和理解GM代码
```

## 缩放移动

就是调试不好累计拖拽和缩放，每次缩放之后累计的拖拽距离计算就不对了



## 自动绑定

[【Qt】信号槽自动绑定](https://blog.csdn.net/weixin_44591035/article/details/102563433)



## 检测不到cow交线

```
https://blog.csdn.net/s634772208/article/details/126975006?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-126975006-blog-51656247.235^v39^pc_relevant_default_base&spm=1001.2101.3001.4242.2&utm_relevant_index=4
```

![image-20231201111005032](E:\codenotes\c++\Robot3d\img\image-20231201111005032.png)

LineSegmentIntersector

```c++
    osg::Vec3 p_start(-100, 0, 0);
    osg::Vec3 p_end(100, 0, 0);
    osgUtil::LineSegmentIntersector::Intersections _intersections;
    osg::ref_ptr< osgUtil::LineSegmentIntersector > _lineSegmentIntersector = new osgUtil::LineSegmentIntersector(p_start, p_end);
    osgUtil::IntersectionVisitor _iv(_lineSegmentIntersector.get());
    node->accept(_iv);
    _intersections = _lineSegmentIntersector->getIntersections();
    int _intersectionNumber = _intersections.size();
    /// 判断是否有相交的节点
    if (_lineSegmentIntersector->containsIntersections())
    {
        /// 从Intersections对象中获取交到的所有内容
        osgUtil::LineSegmentIntersector::Intersections& intersections = _lineSegmentIntersector->getIntersections();
        std::cout << "DrawPathWidget::createPlaneIntersector(): 找到相交点" << std::endl;
    }
```

![image-20231201141113534](E:\codenotes\c++\Robot3d\img\image-20231201141113534.png)

