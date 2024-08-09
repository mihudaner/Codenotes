# THU安装

```
conda create -n THU python==3.7
```
```
pip install -r requirements.txt
```
```
pip install .\torch-1.8.0+cu111-cp37-cp37m-win_amd64.whl
```
```
pip install --no-deps  torchvision==0.14.0
```
![img.png](img.png)
修改mydetect，py文件的  
weights='../yolov7/yolov7.pt',  # 训练好的模型路径   （必改）
会下载别的版本但是没关系
<br/><br/><br/>





## zivid 安装
### SDK安装
[github]（https://github.com/zivid/zivid-python）  
安装Zivid SDK version 2.8.1 (see here for help)
<br/><br/><br/>



### 安装python库
```
pip install zivid
```
Successfully installed numpy-1.21.6 zivid-2.7.0.2.8.1   
<br/><br/><br/>



### Compiler with C++17 support
https://www.cnblogs.com/XieSir/articles/11921800.html
https://blog.csdn.net/honeysuckle_luo/article/details/128009794
<br/><br/><br/>



# tensorflow-gpu安装
```
pip install tensorflow-gpu
```
还需要安装一个cudnn把安装的文件夹的几个文件夹放到对应的位置
https://blog.csdn.net/qq_43215538/article/details/123852028

https://blog.csdn.net/qq_44898938/article/details/118341219
<br/><br/><br/>



# 服务器配置环境
### pip list地址不对
https://www.jb51.net/article/256189.htm

`python -m site`  查看路径在哪  
`python -m site -help`查看site文件的路径

![img_1.png](img_1.png)
<br/><br/>

vim命令  
https://blog.csdn.net/blood_Z/article/details/125064927 
 ```
 vim /home/vip417/.conda/envs/tensorwk/lib/python3.7/site.py
 ```
 <br/>
第87行修改  
USER_SITE = None  
USER_BASE = None  
为  
USER_SITE = "/home/vip417/.conda/envs/tensorwk/lib/python3.7/site-packages"  
USER_BASE = "/home/vip417/.conda/envs/tensorwk/Scripts"（无路径）

USER_SITE = "/home/vip417/.conda/envs/tensorwk"
USER_BASE = "/home/vip417/.conda/envs/tensorwk/lib/python3.7/site-packages"

<br/><br/>
### 服务器创建路径
```
 sudo conda create -p /home/vip417/anaconda3/envs/wktensor python=3.7
```
<br/><br/><br/>


# conda
删除环境
```
conda env remove -n 环境名称
```
添加源  
https://blog.csdn.net/YPP0229/article/details/105630429/  
```
conda config --show channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

conda config --set show_channel_urls yes
```
pip添加源
1、临时使用
1 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

2、永久更改pip源
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：
1 pip install pip -U
2 pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

直接写入配置文件：

vim ~/.pip/pip.conf

将配置文件写入:

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
<br/><br/><br/>


# ubuntu安装
### 磁盘分配

|  分区   |     大小     |  类型  |
|:-----:|:----------:|:----:|
|  系统   |    400M    | 逻辑分区 |
| swap  | 电脑物理内存的2倍  | 逻辑分区 |
|   /   |    30G     | 逻辑分区 |
| /home |    200+    | 逻辑分区 |    

![](2023-03-04-23-50-45.png)
![](img-2023-03-06-13-32-51.png)  
软件安装在了/
<br/><br/>
![](img-2023-03-06-17-39-55.png)
<br/><br/><br/>

### 亮度问题
https://blog.csdn.net/weixin_44120025/article/details/118875998
应该是bois独显和混显修改的问题
<br/><br/><br/>


### clashy
复制托管链接，下载txt
/home/wangkai/.config/Clashy
新建一个yaml把txt文件复制进去

### ubuntu命令
- activate
- ls
- ls -l
- cd
- pwd
- ~主目录  .当前目录  ..上一级目录
- mkdir -p abd/asd/a1
- rmdir  #只能删除空目录
- cp   -rf  递归强制
- rm -rf 递归强制
- mv
- tar -zcvf example.tar.gz example
- tar -zxvf example.tar.gz -C dir
- zip
- unzip
- ln -s example example2 创建软链接
- source activate *** source .sh
- tab自动补全
- 上下键可以查看上一条命令
- nvidia-smi
- df -h 查看磁盘
- watch -n 1 nvidia-smi
- screen -r wk
- df -h 查看内存 
- sudu dpkg -i deb
- sudo cat /proc/version
- source ~/.bashrc 刷新环境
- echo 输出信息到文件或者打印
- chomd 权限
<br/><br/><br/>




# ROS
https://blog.csdn.net/qq_44339029/article/details/108916820  更新软件源
<br/>

https://mp.weixin.qq.com/s?__biz=MzU1NjEwMTY0Mw==&mid=2247562322&idx=1&sn=b8d6d08a2f55bae4dbb532ede6e3d314&chksm=fbc98d36ccbe042000b03ba0ba9ff31c3bd8d97c8c2926bcb55e6d6dc3b9dc702d7609c968dd&scene=27  安装ROS
<br/>

https://www.bilibili.com/read/cv12059277 基础教学资源
https://github.com/guyuehome/ros_21_tutorials  b站故月居ppt
<br/><br/><br/>

## 基础
![](img-2023-03-06-13-35-04.png)  
节点： 类似进程
<br/>
![](img-2023-03-06-13-50-13.png)  
![](img-2023-03-06-20-08-20.png)
话题：数据管道  ，一段是Node publisher,一段是Node subscriber  
消息：数据格式
<br/>
同步：发布阻塞后立马收到  
异步：不阻塞，其他任务去get  
<br/>
![](img-2023-03-06-14-05-18.png)
![](img-2023-03-06-14-07-24.png)
![](img-2023-03-06-14-14-09.png)
<br/><br/>



## 命令
  
常用命令


• rostopic  
• rosservice  
• rosnode 
• rosparam   
• rosmsg  
• rossrv 

• sudo rosdep init 

• roscore  启动rosmaster
• rosrun turtlesim turtlesim_node   
• rosrun turtlesim turtle_teleop_key  
一个包名参数，一个node，两次tab列出node，
<br/><br/>
 

### 查看模型
rqt_graph  
rosnode list  
rosnode info  
![](img-2023-03-06-15-07-16.png)
<br/><br/>


### 发布topic
rostopic pub -r 10 /turtle1/cmd_vel geometry_msgs/Twist  
频率   topic  数据格式  数据内容
![](img-2023-03-06-15-11-54.png)
<br/><br/>


### 查看数据类型
![](img-2023-03-06-15-18-35.png)
<br/><br/>


### service
![](img-2023-03-06-15-23-20.png)
<br/><br/>



### rosbag
![](img-2023-03-06-15-29-26.png)  
记录的topic的message  
![](img-2023-03-06-15-32-43.png)
<br/><br/>



## 工作空间
### 创建
![](img-2023-03-06-15-42-40.png)
<br/><br/>


### 创建包
```
catkin_create_pkg learning_topic  roscpp rospy std_msgs geometry_msgs turtlesim
```
![](img-2023-03-06-15-45-22.png)
![](img-2023-03-06-16-45-50.png)
![](img-2023-03-06-16-47-22.png)
<br/><br/>

### 发布者publisher
![](img-2023-03-06-17-29-18.png)
![](img-2023-03-06-19-53-07.png)  
python不用编译生成可执行文件和链接到ros     
直接改成rosrun learning_topic velocity_publisher.py  

### 订阅subscriber
### 话题消息类型的定义和使用
### 客户端和服务端
### 参数
### 坐标系
### launch文件
![](img-2023-03-06-20-48-40.png)  
roslaunch learning_topic simple.launch



 






# vscode jupyter C++
https://zhuanlan.zhihu.com/p/561182221?utm_id=0  
https://blog.csdn.net/shelgi/article/details/125131135
https://www.cnblogs.com/dotnetcrazy/p/16884534.html   marrkdown的粘贴  
要修改快捷键
![](2023-03-04-23-49-09.png)  
<br/><br/>


conda install jupyter notebook  
conda install -c conda-forge xeus-cling  
jupyter notebook
配置c++插件json
<br/><br/>



### 无法包含头文件
https://www.bilibili.com/read/cv18556963
改task.json的-g
```
"args": [
				"-fdiagnostics-color=always",
				"-g",
				"${fileDirname}/*.cpp",
				"-o",
				"${fileDirname}/${fileBasenameNoExtension}"
			],
```
<br/><br/>




### use
sudo -i  
echo 3 > /proc/sys/vm/drop_caches  
conda activate cpp
jupyter notebook --allow-root
