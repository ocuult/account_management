# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhgl_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/鑫远.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 899, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.jcsj_paypay = QtWidgets.QWidget()
        self.jcsj_paypay.setObjectName("jcsj_paypay")
        self.lineEdit = QtWidgets.QLineEdit(self.jcsj_paypay)
        self.lineEdit.setGeometry(QtCore.QRect(58, 1, 171, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.jcsj_paypay)
        self.label.setGeometry(QtCore.QRect(3, 1, 50, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.jcsj_paypay)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 0, 171, 19))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.jcsj_paypay)
        self.label_2.setGeometry(QtCore.QRect(371, 0, 44, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.jcsj_paypay)
        self.lineEdit_3.setGeometry(QtCore.QRect(272, 1, 91, 19))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.jcsj_paypay)
        self.label_3.setGeometry(QtCore.QRect(239, 1, 28, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.jcsj_paypay)
        self.pushButton.setGeometry(QtCore.QRect(820, 50, 65, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.jcsj_paypay)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 50, 65, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.jcsj_paypay)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 530, 65, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.jcsj_paypay)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 898, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.jcsj_paypay)
        self.label_4.setGeometry(QtCore.QRect(602, 0, 33, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.jcsj_paypay)
        self.lineEdit_4.setGeometry(QtCore.QRect(640, 0, 61, 19))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.jcsj_paypay)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 50, 65, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.jcsj_paypay)
        self.jcj_vps = QtWidgets.QWidget()
        self.jcj_vps.setObjectName("jcj_vps")
        self.pushButton_4 = QtWidgets.QPushButton(self.jcj_vps)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 170, 141, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.jcj_vps)
        self.jcsj_sjk = QtWidgets.QWidget()
        self.jcsj_sjk.setObjectName("jcsj_sjk")
        self.stackedWidget.addWidget(self.jcsj_sjk)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPaypal = QtWidgets.QAction(MainWindow)
        self.actionPaypal.setCheckable(False)
        self.actionPaypal.setObjectName("actionPaypal")
        self.actionVPS = QtWidgets.QAction(MainWindow)
        self.actionVPS.setObjectName("actionVPS")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.actionVAT = QtWidgets.QAction(MainWindow)
        self.actionVAT.setObjectName("actionVAT")
        self.actionPingP = QtWidgets.QAction(MainWindow)
        self.actionPingP.setObjectName("actionPingP")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.actionEbay = QtWidgets.QAction(MainWindow)
        self.actionEbay.setObjectName("actionEbay")
        self.actionAliexpress = QtWidgets.QAction(MainWindow)
        self.actionAliexpress.setObjectName("actionAliexpress")
        self.actionAmazon = QtWidgets.QAction(MainWindow)
        self.actionAmazon.setObjectName("actionAmazon")
        self.actionWish = QtWidgets.QAction(MainWindow)
        self.actionWish.setObjectName("actionWish")
        self.actionCD = QtWidgets.QAction(MainWindow)
        self.actionCD.setObjectName("actionCD")
        self.actionWal_Mart = QtWidgets.QAction(MainWindow)
        self.actionWal_Mart.setObjectName("actionWal_Mart")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action1688 = QtWidgets.QAction(MainWindow)
        self.action1688.setObjectName("action1688")
        self.actionJOOM = QtWidgets.QAction(MainWindow)
        self.actionJOOM.setObjectName("actionJOOM")
        self.actionMMC = QtWidgets.QAction(MainWindow)
        self.actionMMC.setObjectName("actionMMC")
        self.actionShopee = QtWidgets.QAction(MainWindow)
        self.actionShopee.setObjectName("actionShopee")
        self.actionEbay_2 = QtWidgets.QAction(MainWindow)
        self.actionEbay_2.setObjectName("actionEbay_2")
        self.actionAliexpress_2 = QtWidgets.QAction(MainWindow)
        self.actionAliexpress_2.setObjectName("actionAliexpress_2")
        self.actionAmazon_2 = QtWidgets.QAction(MainWindow)
        self.actionAmazon_2.setObjectName("actionAmazon_2")
        self.actionWish_2 = QtWidgets.QAction(MainWindow)
        self.actionWish_2.setObjectName("actionWish_2")
        self.actionCD_2 = QtWidgets.QAction(MainWindow)
        self.actionCD_2.setObjectName("actionCD_2")
        self.actionWal_Mart_2 = QtWidgets.QAction(MainWindow)
        self.actionWal_Mart_2.setObjectName("actionWal_Mart_2")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action1688_2 = QtWidgets.QAction(MainWindow)
        self.action1688_2.setObjectName("action1688_2")
        self.actionJOOM_2 = QtWidgets.QAction(MainWindow)
        self.actionJOOM_2.setObjectName("actionJOOM_2")
        self.actionMMC_2 = QtWidgets.QAction(MainWindow)
        self.actionMMC_2.setObjectName("actionMMC_2")
        self.actionShopee_2 = QtWidgets.QAction(MainWindow)
        self.actionShopee_2.setObjectName("actionShopee_2")
        self.menu.addAction(self.actionPaypal)
        self.menu.addAction(self.actionVPS)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.actionVAT)
        self.menu.addAction(self.actionPingP)
        self.menu.addAction(self.action_8)
        self.menu_2.addAction(self.actionEbay)
        self.menu_2.addAction(self.actionAliexpress)
        self.menu_2.addAction(self.actionAmazon)
        self.menu_2.addAction(self.actionWish)
        self.menu_2.addAction(self.actionCD)
        self.menu_2.addAction(self.actionWal_Mart)
        self.menu_2.addAction(self.action_9)
        self.menu_2.addAction(self.action1688)
        self.menu_2.addAction(self.actionJOOM)
        self.menu_2.addAction(self.actionMMC)
        self.menu_2.addAction(self.actionShopee)
        self.menu_3.addAction(self.actionEbay_2)
        self.menu_3.addAction(self.actionAliexpress_2)
        self.menu_3.addAction(self.actionAmazon_2)
        self.menu_3.addAction(self.actionWish_2)
        self.menu_3.addAction(self.actionCD_2)
        self.menu_3.addAction(self.actionWal_Mart_2)
        self.menu_3.addAction(self.action_10)
        self.menu_3.addAction(self.action1688_2)
        self.menu_3.addAction(self.actionJOOM_2)
        self.menu_3.addAction(self.actionMMC_2)
        self.menu_3.addAction(self.actionShopee_2)
        self.menu_4.addAction(self.action_5)
        self.menu_4.addAction(self.action_6)
        self.menu_4.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "鑫远账号管理系统"))
        self.label.setText(_translate("MainWindow", "Paypa账号"))
        self.label_2.setText(_translate("MainWindow", "邮箱信息"))
        self.label_3.setText(_translate("MainWindow", "姓 名"))
        self.pushButton.setText(_translate("MainWindow", "查 询"))
        self.pushButton_2.setText(_translate("MainWindow", "删  除"))
        self.pushButton_3.setText(_translate("MainWindow", "保  存"))
        self.label_4.setText(_translate("MainWindow", "注册地"))
        self.pushButton_5.setText(_translate("MainWindow", "新 增"))
        self.pushButton_4.setText(_translate("MainWindow", "第二个层叠页面"))
        self.menu.setTitle(_translate("MainWindow", "基础数据维护"))
        self.menu_2.setTitle(_translate("MainWindow", "账号信息"))
        self.menu_3.setTitle(_translate("MainWindow", "店铺信息"))
        self.menu_4.setTitle(_translate("MainWindow", "管理工具"))
        self.menu_5.setTitle(_translate("MainWindow", "关于"))
        self.actionPaypal.setText(_translate("MainWindow", "Paypal信息"))
        self.actionVPS.setText(_translate("MainWindow", "VPS信息"))
        self.action.setText(_translate("MainWindow", "手机卡信息"))
        self.action_2.setText(_translate("MainWindow", "信用卡信息"))
        self.action_3.setText(_translate("MainWindow", "邮箱信息"))
        self.action_4.setText(_translate("MainWindow", "银行卡信息"))
        self.action_5.setText(_translate("MainWindow", "账号资料自动生成器"))
        self.action_6.setText(_translate("MainWindow", "查询工具"))
        self.action_7.setText(_translate("MainWindow", "风险检查器"))
        self.actionVAT.setText(_translate("MainWindow", "VAT信息"))
        self.actionPingP.setText(_translate("MainWindow", "PingP信息"))
        self.action_8.setText(_translate("MainWindow", "连连信息"))
        self.actionEbay.setText(_translate("MainWindow", "Ebay"))
        self.actionAliexpress.setText(_translate("MainWindow", "Aliexpress"))
        self.actionAmazon.setText(_translate("MainWindow", "Amazon"))
        self.actionWish.setText(_translate("MainWindow", "Wish"))
        self.actionCD.setText(_translate("MainWindow", "CD"))
        self.actionWal_Mart.setText(_translate("MainWindow", "Wal-Mart"))
        self.action_9.setText(_translate("MainWindow", "国际站"))
        self.action1688.setText(_translate("MainWindow", "1688"))
        self.actionJOOM.setText(_translate("MainWindow", "JOOM"))
        self.actionMMC.setText(_translate("MainWindow", "MMC"))
        self.actionShopee.setText(_translate("MainWindow", "Shopee"))
        self.actionEbay_2.setText(_translate("MainWindow", "Ebay"))
        self.actionAliexpress_2.setText(_translate("MainWindow", "Aliexpress"))
        self.actionAmazon_2.setText(_translate("MainWindow", "Amazon"))
        self.actionWish_2.setText(_translate("MainWindow", "Wish"))
        self.actionCD_2.setText(_translate("MainWindow", "CD"))
        self.actionWal_Mart_2.setText(_translate("MainWindow", "Wal-Mart"))
        self.action_10.setText(_translate("MainWindow", "国际站"))
        self.action1688_2.setText(_translate("MainWindow", "1688"))
        self.actionJOOM_2.setText(_translate("MainWindow", "JOOM"))
        self.actionMMC_2.setText(_translate("MainWindow", "MMC"))
        self.actionShopee_2.setText(_translate("MainWindow", "Shopee"))
