# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import getpass
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1452, 1059)
        MainWindow.setFixedSize(1452, 1059)#固定主窗口，不放大缩小

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)#预测模型阈值
        self.textEdit.setGeometry(QtCore.QRect(1160, 800, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(str(0.1))#注意设置初值，预测模型阈值为0.1

        self.label = QtWidgets.QLabel(self.centralwidget)#label在最底下有对应的初值
        self.label.setGeometry(QtCore.QRect(1160, 750, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")




        self.label_2 = QtWidgets.QLabel(self.centralwidget)#放视频
        self.label_2.setText("视频输出窗口\n默认路径均已填写完毕，只需选择所需要预测的视频\n路径中请勿出现中文")
        self.label_2.setGeometry(QtCore.QRect(380, 80, 1011, 621))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(170, 170, 127)")#设置视频输出框的颜色
        self.label_2.setObjectName("label_2")


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 333, 871))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)#上传视频
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(36, 36))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)#选择预测模型
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)#选择特征提取模型
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)#选择视频输出保存路径
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)#开始检测
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)#是否使用GPU
        self.checkBox.setGeometry(QtCore.QRect(900, 860, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(36, 36))
        self.checkBox.setObjectName("checkBox")

        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)#视频结果文件名
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setGeometry(QtCore.QRect(900, 800, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("result.avi")#注意设置初值，预测模型阈值为0.6


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 750, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setGeometry(QtCore.QRect(10, 960, 1431, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(1160, 840, 261, 31))
        # font = QtGui.QFont()
        # font.setFamily("Bahnschrift")
        # font.setPointSize(16)
        # self.label_5.setFont(font)
        # self.label_5.setObjectName("label_5")

        # MainWindow.setCentralWidget(self.centralwidget)#这一部分的这三个必须注释，不然会报错
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1452, 30))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)#结果显示按钮
        self.pushButton6.setGeometry(QtCore.QRect(600, 750, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")

        self.labelTime = QtWidgets.QLabel(self)#label在最底下有对应的初值
        self.labelTime.setGeometry(QtCore.QRect(400, 820, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.labelTime.setFont(font)
        self.labelTime.setObjectName("labelTime")

        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(380,60,1052.5,20)



        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.upLoadVedio)
        self.pushButton_2.clicked.connect(MainWindow.StartPredict)
        self.pushButton_3.clicked.connect(MainWindow.ChoiseSavePath)
        self.pushButton_4.clicked.connect(MainWindow.SelectPredictModel)
        self.pushButton_5.clicked.connect(MainWindow.SelectFeatureModel)
        self.pushButton6.clicked.connect(MainWindow.openVedio)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "预测模型阈值"))
        self.pushButton.setText(_translate("MainWindow", "上传视频"))
        self.pushButton_4.setText(_translate("MainWindow", "选择预测模型"))
        self.pushButton_5.setText(_translate("MainWindow", "选择特征提取模型"))
        self.pushButton_3.setText(_translate("MainWindow", "选择保存路径"))
        self.pushButton_2.setText(_translate("MainWindow", "开始检测"))
        self.pushButton6.setText(_translate("MainWindow", "结果显示"))
        self.checkBox.setText(_translate("MainWindow", "使用GPU"))
        self.label_4.setText(_translate("MainWindow", "结果文件名"))
        self.label_3.setText(_translate("MainWindow", "默认路径与文件名为："+'C:/Users/'+getpass.getuser()+'/Desktop/PredictResult/result.avi'))
        # self.label_5.setText(_translate("MainWindow", "特征提取模型阈值"))

