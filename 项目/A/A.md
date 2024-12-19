## [pycharm配置pyqt5_手把手教你写一个基于python+pyqt5的股票盯盘软件](https://blog.csdn.net/weixin_39634900/article/details/110364258)

**一**．**开发环境搭建 
1.Python环境搭建 
1)下载python3.7 
2)安装Python 3.7.6 
2.Pycharm 环境搭建 
1)下载Pycharm 
2)安装Community版本Pycharm 
3.Pyqt5安装 
1)安装pyqt5 
2)配置pycharm 
二.量化概述 
1.数据源 
2.策略 
三.软件介绍 
1.设置策略 
2.微信实时盯盘 
3.新闻关键字云图 
4.持仓亏盈统计 
四．代码源文件** 

## [实现迷你盯盘](https://github.com/xgzit/miniStock)



## [tushare](https://tushare.pro/document/2)

### 1. https://blog.csdn.net/wsdc0521/article/details/105864817

![image-20241129025035582](E:\codenotes\项目\A\img\image-20241129025035582.png)

### 2. 

![image-20241129025206402](E:\codenotes\项目\A\img\image-20241129025206402.png)

```

# coding=utf8
import sys
from datetime import datetime
import matplotlib
import tushare as ts

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget

global real_data
real_data = [20]

# 设置 Tushare Pro API Token
ts.set_token('52d9bb788e8735cd0833f1bfd632b84617b15c8e4488f3b0fe9bc4b0')  # 替换为你的 Tushare Pro Token
pro = ts.pro_api()


class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（也是FigureCanvasAgg）"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """静态画布"""

    def compute_initial_figure(self):
        # 获取历史数据
        try:
            data = pro.daily(ts_code='000002.SZ', start_date='20240522', end_date='20240531')
            dates = [datetime.strptime(d, '%Y%m%d').date() for d in data['trade_date']]
            prices = data['open']
            self.axes.plot(dates[::-1], prices[::-1])  # 日期和价格倒序以正确显示
        except Exception as e:
            print(f"获取历史数据失败: {e}")


class MyDynamicMplCanvas(MyMplCanvas):
    """动态画布：每1秒自动更新"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot(real_data, 'r')

    def update_figure(self):
        global real_data
        try:
            # 获取实时数据
            data = pro.daily(ts_code='000581.SZ', start_date='20240101', end_date='20241231')
            latest_price = float(data['close'].iloc[0])  # 获取最近收盘价
            real_data.append(latest_price)

            self.axes.clear()
            self.axes.plot(real_data, 'r')
            self.draw()
        except Exception as e:
            print(f"实时数据获取失败: {e}")


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("程序主窗口")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        layout = QVBoxLayout(self.main_widget)
        static_canvas = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dynamic_canvas = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        layout.addWidget(static_canvas)
        layout.addWidget(dynamic_canvas)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.statusBar().showMessage("Matplotlib 示例程序", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
                          """PyQt5 和 Matplotlib 示例程序.
                          使用 Tushare Pro 获取股票数据.""")


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 与 Matplotlib 示例")
    aw.show()
    app.exec_()

```

### 3. **[==stock_predict==](https://gitee.com/szluyu99/stock_predict)**

![image-20241129025621012](E:\codenotes\项目\A\img\image-20241129025621012.png)

## [同花顺python自动化交易接口-easytrader](https://www.bilibili.com/video/BV1eL411w7pW/?spm_id_from=333.1391.0.0)



## [==上帝之手==](https://gitee.com/lawrence2012/Heaven_Hand_stock)

使用的上海证券交易所接口，白天不知道为什么

```
r = requests.get(url, params=params, headers=headers)
```

打不开

![image-20241129025518083](E:\codenotes\项目\A\img\image-20241129025518083.png)



## talib

https://github.com/cgohlke/talib-build/releases