# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 1059)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 840, 211, 31))
        font = QtGui.QFont()
        font.setFamily("AMS")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 790, 131, 31))
        font = QtGui.QFont()
        font.setFamily("AMS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 1011, 621))
        font = QtGui.QFont()
        font.setFamily("AMS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AMS")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(36, 36))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AMS")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 890, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(36, 36))
        self.checkBox.setObjectName("checkBox")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 30))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.upLoadVedio)
        self.pushButton_2.clicked.connect(MainWindow.StartPredict)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "阈值"))
        self.pushButton.setText(_translate("MainWindow", "上传视频"))
        self.pushButton_2.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_3.setText(_translate("MainWindow", "选择保存路径"))
        self.checkBox.setText(_translate("MainWindow", "使用GPU"))
        self.label_4.setText(_translate("MainWindow", "结果文件名"))
        self.label_3.setText(_translate("MainWindow", "默认路径与文件名为：C:/Users/Default/Downloads/result.avi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

