from PySide2.QtWidgets import *  # 不止这一个外部库，其它的库我在需要用到时单独引入
from sql import SQL
import pymysql  # 引入连接数据库需要用到的包


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.db = SQL()
        self.initUI()  # 初始化窗口

    def initUI(self):
        self.setWindowTitle("使用表格显示数据库中的数据")
        self.resize(800, 500)  # 设置窗口大小
        vhayout = QHBoxLayout()  # 创建水平布局
        self.tableWidget = QTableWidget()  # 创建表格
        self.text_input = QTextEdit()  # 创建表格

        result = self.db.show_all_items()  # 获取所有记录
        row = self.db.cursor.rowcount  # 获取记录个数，用于设置表格的行数
        vol = len(result[0])  # 获取字段数，用于设置表格的列数

        self.db.cursor.close()  # 关闭游标
        self.db.conn.close()  # 关闭连接

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(vol)  # 设置表格列数

        # 设置表头的名称

        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'rgb_path', 'point_path', 'timestemp', ' frame_rate', 'exposure', 'gain', 'rgb_h', 'rgb_w', 'points_num', 'defect_num'])

        for i in range(row):  # 遍历行
            for j in range(vol):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)  # 转换后可插入表格

        self.tableWidget.resizeColumnToContents(row)  # 使列宽跟随内容改变
        self.tableWidget.resizeRowToContents(vol)  # 使行高跟随内容改变
        self.tableWidget.setAlternatingRowColors(True)  # 使表格颜色交错显示

        vhayout.addWidget(self.tableWidget)  # 将表格添加到水平布局中
        vhayout.addWidget(self.text_input)  # 将表格添加到水平布局中
        self.setLayout(vhayout)  # 设置当前窗口的布局方式

        # 连接双击信号和槽函数
        self.tableWidget.itemDoubleClicked.connect(self.on_item_double_clicked)

    def add_frame(self):

        return

    def on_item_double_clicked(self, item):
        # 获取双击的行和列
        row = item.row()
        col = item.column()

        # 获取该行的数据
        data = [self.tableWidget.item(row, c).text() for c in range(self.tableWidget.columnCount())]

        # 打印该行的信息
        print(f'Double clicked on row {row}, data: {data}')
        return data


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # 创建窗口程序
    demo = Demo()  # 创建窗口类对象
    demo.show()  # 显示窗口
    sys.exit(app.exec_())
