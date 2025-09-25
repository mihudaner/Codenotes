#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :PytorchAir
@File    :P1.py
@IDE     :PyCharm
@Author  :你的名字
@Date    :2025/8/14/014 23:37
@explain :  PyTorch 2.0 编译基础设施解读——计算图捕获（Graph Capture） # https://zhuanlan.zhihu.com/p/644590863
'''
# 按 Shift+F10 执行或将其替换为您的代码。


import torch
from torch import fx

def f(x:int,y:int):
    """
    一个包含多种控制流的函数
    :param x:
    :return:
    """
    return (x.relu() + 1) * x.pow(5)

def conditional_computation(x):
    """

    Args:
        x:

    Returns:

    """
    if x.sum() < 0:
        return x + 1
    else:
        return x - 1

# 包含形状相关的代码
def shape_dependent(x):
    bsz, *sizes = x.shape
    return x.reshape(bsz, -1)

# 包含外部代码
def external_code(x):
    import numpy as np
    return x + torch.from_numpy(np.random.random((5, 5, 5)))

def case1():
    fx_model = fx.symbolic_trace(f)
    print(fx_model.graph)

def case2():
    input = torch.randn(5, 5, 5)
    f_traced = torch.jit.trace(f, input)
    print(f_traced.graph)

def custom_backend(gm, example_inputs):
    print(gm.compile_subgraph_reason)
    print(gm.graph)
    print(gm.code)
    return gm.forward


def case3():
    opt_f = torch.compile(conditional_computation, backend=custom_backend)
    output = opt_f(input)

case3()