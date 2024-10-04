#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/28 23:21
# @Author  : mihudan~
# @File    : Click.py
# @Description : 

import pyautogui
import time

try:
    while True:
        # 获取鼠标当前位置
        x, y = pyautogui.position()

        # 左移
        pyautogui.moveTo(x - 10, y)  # 向左移动 10 像素
        pyautogui.click()  # 点击鼠标左键

        time.sleep(0.5)  # 等待 0.5 秒

        # 右移
        pyautogui.moveTo(x + 10, y)  # 向右移动 10 像素
        pyautogui.click()  # 点击鼠标左键

        time.sleep(5)  # 等待 5 秒
except KeyboardInterrupt:
    print("程序已停止。")
