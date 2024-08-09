#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/23 20:26
# @Author  : 我的名字
# @File    : tool.py.py
# @Description : 这个函数是用来balabalabala自己写

from scipy import signal
import numpy as np
import cv2
import matplotlib.pyplot as plt


def threshold_max(image, threshold):
    _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    result = np.where(image > threshold, threshold, image)
    return result.astype(np.uint8)


def enhance_image(image, alpha, beta):
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced_image


def show(result):
    cv2.imshow('Enhanced Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def use():
    img = cv2.imread(r"E:\codenotes\opencv\photo\img_1.png")
    result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show(result)

    # 增强图像
    # 设置对比度和亮度增益
    alpha = 1.5
    # 对比度增益
    beta = -100  # 亮度增益
    result = enhance_image(img, alpha, beta)
    show(result)


if __name__ == '__main__':
    use()

    img = cv2.imread(r"E:\codenotes\opencv\photo\img.png")

    # 增强图像
    # 设置对比度和亮度增益
    alpha = 2
    # 对比度增益
    beta = -40  # 亮度增益
    result = enhance_image(img, alpha, beta)
    show(result)

    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    show(result)

    # 设置阈值
    threshold = 200
    # 进行阈值处理
    result = threshold_max(result, threshold)
    # 显示结果
    cv2.imshow('Threshold Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # result = cv2.medianBlur(result, 3)
    # show(result)
    # # 获取结构元素
    # k = np.ones((10, 10), np.uint8)
    # # # 开操作
    # result = cv2.morphologyEx(result, cv2.MORPH_OPEN, k)
    # show(result)
    #

