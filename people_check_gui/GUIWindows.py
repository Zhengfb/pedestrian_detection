import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QDate,QDateTime,QTime,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import QUrl
import PyQt5.QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
import cv2
import os
from PredictVedio import StartPredictNow
class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self,):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Check')
        self.VedioFileType = None
        self.SelectVedioPath = None#选择的视频地址
        self.videoStream = None
        # 帧速
        self.frameRate = None
        self.save_dir = 'C:/Users/Default/Downloads/result.avi'
        self.SelectPredictModelPath = '../model\\detection\\pedestrian_yolov3_darknet'
        self.SelectFeatureModelPath = '../model\\embedding'
        self.VideoName = 'result.avi'
    def upLoadVedio(self):
        try:
            self.SelectVedioPath, self.VedioFileType = QFileDialog.getOpenFileName(None, "选取文件", "./",
                                                            "All Files (*);;*.mp4;;*.avi")  # 设置文件扩展名过滤,注意用双分号间隔
            VedioNameString = self.SelectVedioPath.split('.')
            if VedioNameString[-1]=="mp4" or VedioNameString[-1]=="avi":
                print("文件对了")
            else:
                self.VedioFileType = None
                self.SelectVedioPath = None
                print("文件错了")
        except:
            pass

    def openVedio(self):
        while self.videoStream.isOpened():
            ret, frame = self.videoStream.read()
            if not ret:
                break
            image_height, image_width, image_depth = frame.shape
            QFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            QFrame = QImage(QFrame.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                            image_width * image_depth,
                            QImage.Format_RGB888)

            self.label_2.setPixmap(QPixmap.fromImage(QFrame))
            self.label_2.setScaledContents(True)
            cv2.waitKey(int(1000 / self.frameRate))
        self.videoStream.release()
    def ChoiseSavePath(self):
        try:
            self.save_dir = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
            print("save dir: ",self.save_dir)
        except:
            self.save_dir = 'C:/Users/Default/Downloads/result.avi'
            pass
    def SelectPredictModel(self):
        try:
            self.SelectPredictModelPath = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
            print("save dir: ", self.save_dir)
        except:
            self.SelectPredictModelPath = '../model\\detection\\pedestrian_yolov3_darknet'
            pass
    def SelectFeatureModel(self):
        try:
            self.SelectFeatureModelPath = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
            print("save dir: ", self.save_dir)
        except:
            self.SelectFeatureModelPath = '../model\\embedding'
            pass

    def StartPredict(self):
        if self.SelectVedioPath == None:
            print("请选择视频文件")
        else:
            print(self.SelectVedioPath)
            print("开始预测")
            s = self.lineEdit_2.text().split(" ")
            for item in s:
                if len(item)!=0:
                    self.VideoName = item
            threadhold = float(self.textEdit.text())#获取阈值
            usGPU = self.checkBox.isChecked()
            _translate = QtCore.QCoreApplication.translate
            svp = os.path.join(self.save_dir,self.VideoName)
            self.label_3.setText(_translate("MainWindow", "文件所在位置："+svp))
            people_number = StartPredictNow(self.SelectVedioPath,threadhold,usGPU,self.save_dir,self.VideoName,self.SelectPredictModelPath,self.SelectFeatureModelPath)
            print("预测结束")
            self.videoStream = cv2.VideoCapture(svp)
            # 帧速
            self.frameRate = self.videoStream.get(cv2.CAP_PROP_FPS)
            self.openVedio()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
