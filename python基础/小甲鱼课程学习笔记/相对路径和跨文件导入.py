import argparse
import os
import sys
import tkinter
sys.path.append("D:/deeplearning/pseudo_lidar-master/psmnet")
sys.path.append("D:/桌面/pythonwork")
from models import *
from 小甲鱼课程学习笔记 import *

# 发现了，arg传入的只是字符串，相对路径还是相对与运行.py工程时候 终端的路径，vscode运行就是项目的路径
'''python D:\桌面\pythonwork\小甲鱼课程学习笔记\相对路径和跨文件导入.py --data_path ./KITTI/object/training/ --split_file ./KITTI/object/train.txt'''

def pathfunc():
    parser = argparse.ArgumentParser(description='Generate Disparity')
    parser.add_argument('--data_path', type=str, default='~/Kitti/object/training/')
    parser.add_argument('--split_file', type=str, default='~/Kitti/object/train.txt')
    args = parser.parse_args()
    path = os.path.abspath('.')
    print(os.path.abspath('.'))
    print( os.path.abspath(os.path.join(args.data_path)) )
    print(os.path.join(path,args.split_file))

def importfunc():
    model = stackhourglass(137)
    #print(model)
    Tkinter2_cal('123456')#在init文件中修改为printf

if __name__ == '__main__':
    pathfunc()
    importfunc()
