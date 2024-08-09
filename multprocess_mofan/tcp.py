import requests
import socket
import os
import time


def get():
    r = requests.get("https://www.cnblogs.com/xwltest/p/16526663.html")
    print(r.text)


def tcp():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  连接
    soc.connect(("cgi.im.qq.com", 80))
    soc.send(b"GET http://cgi.im.qq.com\n\n")
    r = soc.recv(1024)
    r = bytes(r).decode()
    print(r)


def map():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  连接
    soc.connect(("restapi.amap.com", 80))
    soc.send(b"GET http://restapi.amap.com/v3/ip?key=8f59ba3487479be1ba2660259485ffa4&language=en\n\n")
    r = soc.recv(1024)
    r = bytes(r).decode()
    print(r)


if __name__ == '__main__':
    # get()
    tcp()
    map()
