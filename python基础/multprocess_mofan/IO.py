# 非阻塞IO
# 阻塞IO
# IO多路复用:多个非阻塞io，用轮询去接受看每个io是否有数据
# https://www.python51.com/jc/17038.html


import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time
selector = DefaultSelector()


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.con.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(self.path, self.host).
                      encode('utf-8'))
        selector.register(self.con.fileno(), EVENT_READ, self.read)

    def read(self, key):
        d = self.con.recv(1024)
        if d:
            print(d)
            self.data += d
        else:
            selector.unregister(key.fd)
            self.data = self.data.decode('utf-8')
            html_data = self.data.split('\r\n\r\n')[1]
            print(html_data)
            self.con.close()

    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == "":
            self.path = '/'
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.setblocking(False)
        try:
            self.con.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册
        selector.register(self.con.fileno(), EVENT_WRITE, self.connected)
        # self.con.fileno表示当前连接在进程中的描述符，EVENT_WRITE表示socket准备是否就绪，self.connected为回调函数


def loop():
    while True:
        ready = selector.select()  # 注册的进程selector.register(self.con.fileno(), EVENT_WRITE, self.connected) 查询ready的然后执行
        for key, mask in ready:
            callback = key.data  # callback =  bound method Fetcher.read
            callback(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url('http://www.baidu.com')
    loop()
