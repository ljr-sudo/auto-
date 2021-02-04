# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new题目.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

b = random.randint(10, 20)
c = random.randint(1, 10)
x = c+b
str1=str(x)
str2=str(x*x)
str3=str(3.14*x*x)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 140, 176, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 150, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 140, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(600, 400, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(240, 240, 236, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.commandLinkButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.label_3.update)
        self.pushButton.clicked.connect(self.label_7.update)
        self.pushButton.clicked.connect(self.label_9.update)
        self.pushButton.clicked.connect(self.label_11.update)
        self.pushButton.clicked.connect(self.label_13.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    for i in range(200):
        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "自动出题程序"))
            self.label.setText(_translate("MainWindow", "有一个圆，半径为"))
            self.label_3.setText(_translate("MainWindow", str1))
            self.label_2.setText(_translate("MainWindow", '面积是多少'))
            self.pushButton.setText(_translate("MainWindow", "点击显示答案"))
            self.pushButton_2.setText(_translate("MainWindow", "重试"))
            self.commandLinkButton.setText(_translate("MainWindow", "点击退出"))
            self.label_4.setText(_translate("MainWindow", "答案"))
            self.label_7.setText(_translate("MainWindow", str1))
            self.label_5.setText(_translate("MainWindow", "S=πr2"))
            self.label_8.setText(_translate("MainWindow", "x"))
            self.label_10.setText(_translate("MainWindow", " =πx"))
            self.label_6.setText(_translate("MainWindow", " =πx"))
            self.label_9.setText(_translate("MainWindow", str1))
            self.label_11.setText(_translate("MainWindow", str2))
            self.label_12.setText(_translate("MainWindow", " ="))
            self.label_13.setText(_translate("MainWindow", str3))


import sys
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
  MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
  ui = Ui_MainWindow()          # ui是Ui_MainWindow()类的实例化对象
  ui.setupUi(MainWindow)         # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
  MainWindow.show()            # 执行QMainWindow的show()方法，显示这个QMainWindow
  sys.exit(app.exec_())          # 使用exit()或者点击关闭按钮退出QApplicat
