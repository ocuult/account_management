import sys
from PyQt5.Qt import *
from zhgl_main import Ui_MainWindow
from My_DB import MyDb
from PyQt5 import QtCore

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()    # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()      # 实例化QMainWindow类
    aw.setupUi(w)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()               # 显示主窗体
    sys.exit(App.exec_())   # 循环中等待退出程序
