import sys
from PyQt5.Qt import *
from zhgl_main import Ui_MainWindow
from My_DB import MyDb
from PyQt5 import QtCore


class MyUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyUi, self).__init__()
        self.setupUi(self)
        self.tableWidget.itemChanged.connect(self.table_update)
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取
        self.my_db1 = MyDb()
        self.paypalheaderlabels = ['ID', 'Paypal账号', 'Papal密码', '邮箱信息', '提现账号', 'VPS信息', '个人信息', '注册时间', '注册地址', '状态']

    # 层叠页面的切换
    @pyqtSlot()
    def on_actionPaypal_triggered(self):
        self.stackedWidget.setCurrentIndex(0)

    # 插入一行
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
    #更新数据
    def table_update(self):
        self.tableWidget.blockSignals(True)  # 关闭信号槽，防止itemchange被误触发
        row_select = self.tableWidget.selectedItems()
        idtext = self.tableWidget.item(row_select[0].row(), 0)  # 判断ID是否为空，如果ID为空表示当前数据是插入而不是更新
        if len(row_select) == 0:
            return
        elif idtext == None: # 判断ID是否为空，如果ID为空表示当前数据是插入而不是更新
            sqlstr = '''INSERT INTO "Paypal信息"("{}")VALUES ('{}')'''
            teststr = sqlstr.format(self.paypalheaderlabels[row_select[0].column()], row_select[0].text())
            if self.my_db1.loaddb(teststr) == 0:
                print("当前新增数据失败，清检查是否重复")
                QMessageBox.warning(self,"警告","当前插入数据失败，清检查是否重复",QMessageBox.Yes)
                row_select[0].setText('')  # 这里做唯一约束的检查，如果失败了当前输入的数据清空

        else:
            sqlstr = '''update "Paypal信息" set "{}" = '{}' where id = {} '''
            teststr = sqlstr.format(self.paypalheaderlabels[row_select[0].column()], row_select[0].text(),
                                    self.tableWidget.item(row_select[0].row(), 0).text())
            if self.my_db1.loaddb(teststr) == 0:
                print("当前插入数据失败，清检查是否重复")
                QMessageBox.warning(self, "警告", "当前更新数据失败，清检查是否重复", QMessageBox.Yes)
                row_select[0].setText('')  # 这里做唯一约束的检查，如果失败了当前输入的数据清空
        self.tableWidget.blockSignals(False)  # 打开信号槽，恢复正常的触发

    # 删除只做逻辑删除，不实际删除数据
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        else:
            sqlstr = '''update "Paypal信息" set "状态" = '删除' where id = {} '''
            teststr = sqlstr.format(self.tableWidget.item(row_select[0].row(), 0).text())
            self.my_db1.loaddb(teststr)
            self.tableWidget.removeRow(row_select[0].row())

    # 查询按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.tableWidget.blockSignals(True)  # 关闭信号槽，防止itemchange被误触发
        sqlstr = '''SELECT
                    id,
                    "Paypal账号",
                    "Papal密码",
                    "邮箱信息",
                    "提现账号",
                    "VPS信息",
                    "个人信息",
                    "注册时间",
                    "注册地址",
                    "状态" 
                FROM
                    "Paypal信息" 
                WHERE
                    "Paypal账号" LIKE '{}%' or "Paypal账号" ISNULL
                    AND "个人信息" LIKE '{}%' or "个人信息" ISNULL
                    AND "邮箱信息" LIKE '{}%' or "邮箱信息" ISNULL
                    AND "注册地址" LIKE '{}%' or "注册地址" ISNULL
                    and "状态" != '删除' or "状态" ISNULL '''
        ppzh = self.lineEdit.text()
        grxx = self.lineEdit_3.text()
        yxxx = self.lineEdit_2.text()
        zzdz = self.lineEdit_4.text()
        data = self.my_db1.loaddb(sqlstr.format(ppzh, grxx, yxxx, zzdz))

        columrow = self.my_db1.columnRow()  # 防止两次调用遍历函数
        self.tableWidget.setRowCount(columrow[1])
        self.tableWidget.setColumnCount(columrow[0])

        self.tableWidget.setHorizontalHeaderLabels(self.paypalheaderlabels)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:#D5D5D5;}")
        j = 0
        while data.next():
            for i in range(10):
                if i == 0:  # 当i=0时表示第一列，第一列为ID不能编辑。
                    item0 = QTableWidgetItem(str(data.value(i)))
                    item0.setFlags(QtCore.Qt.ItemIsEnabled)  # 第一列不可以被编辑
                    self.tableWidget.setItem(j, i, item0)
                else:
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(data.value(i))))
            j += 1
        self.tableWidget.blockSignals(False)  # 打开信号槽，恢复正常的触发


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = MyUi()
    ui.show()
    sys.exit(app.exec_())
