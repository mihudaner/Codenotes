#第29讲
import sys
'''
def file_write(file_name):
    '接收用户输入并且保存为新的文件'
    f=open(file_name,"w")
    print("请输入，输入的内容为\":w\"保存并退出")
    while True:
        write_some =input()
        if write_some != ":w":
            f.write("%s\n"%write_some)#字符串还能这样写
        else:
            break
    f.close()
file_name = input("输入文件名")
file_write(".\data\\"infile_name)

'''



'''
def file_view(file_name, line_num):
    '把指定路径的文件的前N行内容打印到屏幕'
    print('\n文件%s的前%s的内容如下: \n' %(file_name, line_num))
    f = open (file_name,"r", encoding="utf-8")#这里需要设置为encoding="utf-8"编码格式
  #  f = open (file_name)
    for i in range (int (line_num)):
        print(f.readline(), end= '')
    f.close()
file_name = input (r'请输入要打开的文件(C: (test.txt)：')
line_num = input('请输入需要显示该文件前几行：')
file_view(".\\data\\"+file_name, line_num)
'''



'''
def file_replace(file_name, rep_word, new_word):
    '编写一个函数可以把输入路径的文件的一个字符串全部替换成新的字符串'
    f_read = open (file_name,"r", encoding="utf-8")
    content= []
    count = 0 
    for eachline in f_read:#!!这里的f_read是一个迭代对象，并且每一行都是
        if rep_word in eachline:
            count += eachline.count (rep_word)#count减觉应该用这个
            eachline = eachline.replace(rep_word,new_word)
        content.append (eachline)
    decide = input('\n文件%s共有%s个【%s】\n确认全部【%s】替换【%s】?\n' \
                   %(file_name, count, rep_word, rep_word,new_word))
    if decide in ('YES', 'Yes', 'yes'):
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write. close()
file_name=input('请输入文件名：')
rep_word,=input('请输入需替换单词：')
new_word=input('请输入新单词：')
file_replace(file_name, rep_word, new_word)
'''

#os 模块操作系统
import os
os.getcwd()
os.listdir()
'''
getcwd()#返回当前工作目录
chdir(path)#改变工作目录
listdir(path='.')#列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）!!!!
mkdir(path)#创建单层目录，如该目录已存在抛出异常
makedirs(path)#递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突
remove(path)#删除文件
rmdir(path)#删除单层目录，如该目录非空则抛出异常
removedirs(path)#递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
rename(old, new)#将文件old重命名为newj,路径不一样可以移动位置
'''
#os.system('cmd')
#os.system('calc')


import os

def print_pos(key_dict):
    '输入的是关键字和关键字的位置的字典'
    keys = key_dict.keys()
    keys = sorted(keys)# 由于字典是无序的，我们这里对行数进行排序

    for each_key in keys:
        print('关键字出现在第%s行，第 %s个位置' %(each_key, str(key_dict[each_key])))

    
def pos_in_line(line, key):
    '输入一行字符串和关键字，返回这一行的列位置的列表'
    pos =[]
    begin = line.find(key)
    while begin != -1:#如果没有找到，会返回-1
        pos.append(begin+1)#用户的角度是从1开始数
        begin =  line.find(key, begin+1)#从下一个位置继续查找
    return pos

def search_in_file(file_name, key):
    '输入文件名字，返回一个列表，字典的键是行，值是列位置的列表'
    '''print(search_in_file('C:\\Users\\wangkai\\Desktop\\重命名.txt', '的'))'''
    f = open (file_name,"r", encoding="utf-8")
    count = 0#记录行数
    key_dict = dict()#字典，用户存放key所在行，值对应具体位置
    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line,key)# pos里key在每行的列位置
            key_dict[count] = pos
    f.close()
    return key_dict

def search_files(key, detail):
    '输入关键字，返回所在的位置的顶层文件'
    all_files = os.walk(os.getcwd())
   #遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])
    txt_files = []
    for i in all_files:#i中是一个元组，元组的元素是每一类文件的列表
        for each_file in i[2]:#i[2]中是文本文件
            if os.path.splitext(each_file)[1] =='.py' or os.path.splitext(each_file)[1] =='.txt' or os.path.splitext(each_file)[1] =='.md' or os.path.splitext(each_file)[1] =='.ipynb':
            #split(path)分割文件名与路径，返回(f_path, f_name)元组
                each_file = os.path.join(i[0],each_file)#i(0)是父文件路径
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('======================================================')
            print('在文件【%s】中找到关键字【%s】'%(each_txt_file, key))
        if detail in ['YES', 'Yes', 'yes']:
            print_pos(key_dict)
key =input('将该脚本放入文件夹内，输入查找的关键字：')
detail=input('是否需要打印关键字【%s】在文件中的具体位置 (YES/NO) ：'% key)
search_files(key, detail)

import time
while 1:
    time.sleep(1000)
#第31讲
#使用pickle.dump需要用'wb'open模式打开文件
#读取文件时候需要使用pickle.load需要用'rb'模式打开文件
