#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :PytorchAir
@File    :P1.py
@IDE     :PyCharm
@Author  :你的名字
@Date    :2025/8/14/014 23:37
@explain :  https://zhuanlan.zhihu.com/p/12712224407
'''


import torch
import warnings

t1 = torch.randn(10, 10)
t2 = torch.randn(10, 10)

@torch.compile
def opt_foo2(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b

print(opt_foo2(t1, t2))