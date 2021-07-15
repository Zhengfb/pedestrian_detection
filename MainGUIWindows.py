import multiprocessing
from multiprocessing import freeze_support
import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from people_check_gui.mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
import cv2
import os
import getpass
import threading
import paddle
from PredictVedio import StartPredictNow
class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self,):
        super(mywindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Check')
        self.vedioFileType = None
        self.selectVedioPath = None#选择的视频地址
        self.videoStream = None
        # 帧速
        self.frameRate = None
        self.save_dir = 'C:/Users/'+getpass.getuser()+'/Desktop/PredictResult'
        self.svp = self.save_dir
        print("路径   ",os.getcwd())
        self.selectPredictModelPath = os.path.join(os.getcwd(),'resources/model/detection/yolov3_darknet')
        self.selectFeatureModelPath = os.path.join(os.getcwd(),'resources/model/embedding')
        self.videoName = 'result.avi'
        # self.isStart = True#判断是否该启动一个线程
        self.testPredictTime = 0
        self.frameNumber = 0
        self.timer = QBasicTimer()
        self.step = 0
        self.allTime = 0
    def upLoadVedio(self):
        try:
            self.selectVedioPath, self.vedioFileType = QFileDialog.getOpenFileName(None, "选取文件", "./",
                                                            "All Files (*);;*.mp4;;*.avi")  # 设置文件扩展名过滤,注意用双分号间隔
            VedioNameString = self.selectVedioPath.split('.')
            self.selectVedioPath = self.selectVedioPath
            if VedioNameString[-1]=="mp4" or VedioNameString[-1]=="avi":
                print("文件对了")
                self.pushButton6.setText('播放原视频')
                self.svp = self.selectVedioPath
                video_cap = cv2.VideoCapture(self.selectVedioPath)

                frame_count = 0
                while (True):
                    ret, frame = video_cap.read()
                    if ret is False:
                        break
                    frame_count = frame_count + 1
                video_cap.release()
                self.frameNumber = frame_count
                print('视频帧数：',self.frameNumber)
                QtWidgets.QMessageBox.information(self, "成功", "视频上传成功", QtWidgets.QMessageBox.Ok)
            else:
                self.vedioFileType = None
                self.selectVedioPath = None
                print("文件错了")
                QtWidgets.QMessageBox.warning(self, "警告", "请上传视频或选择正确的文件类型(.mp4/.avi)", QtWidgets.QMessageBox.Cancel)
        except:
            pass

    def openVedio(self):
        # self.isStart = True;
        self.videoStream = cv2.VideoCapture(self.svp)
        # 帧速
        self.frameRate = self.videoStream.get(cv2.CAP_PROP_FPS)

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
            self.save_dir = self.save_dir
            print("save dir: ",self.save_dir)
        except:
            self.save_dir = 'C:/Users/Default/Downloads/result.avi'
            pass
    def SelectPredictModel(self):
        try:
            self.selectPredictModelPath = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
            print("save dir: ", self.selectPredictModelPath)
        except:
            self.selectPredictModelPath = os.path.join(os.getcwd(),'resources/model/detection/yolov3_darknet')
            pass
    def SelectFeatureModel(self):
        try:
            self.selectFeatureModelPath = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
            print("save dir: ", self.selectFeatureModelPath)
        except:
            self.selectFeatureModelPath = os.path.join(os.getcwd(),'resources/model/embedding')
            pass
    # def OpenPredictThread(self):
    #     self.label_2.setText("正在检测")
    #     self.pushButton_2.setEnabled(False)#预测视频按钮此时不可点击
    #     self.

    def StartPredict(self):
        self.testPredictTime=0
        if self.selectVedioPath == None:
            print("请选择视频文件")
            QtWidgets.QMessageBox.warning(self, "警告", "请先选择视频", QtWidgets.QMessageBox.Cancel)
        else:
            try:
                self.pushButton6.setText("预测结果显示")
                print(self.selectVedioPath)
                print("开始预测")
                s = self.lineEdit_2.text().split(" ")
                for item in s:
                    if len(item)!=0:
                        self.videoName = item
                threadhold = float(self.textEdit.text())#获取阈值
                usGPU = self.checkBox.isChecked()
                _translate = QtCore.QCoreApplication.translate
                self.svp = os.path.join(self.save_dir,self.videoName)
                self.label_3.setText(_translate("MainWindow", "结果文件保存在："+self.svp))
                if self.testPredictTime == 0:
                    people_number,onesecond = StartPredictNow(self.selectVedioPath,threadhold,usGPU,self.save_dir,self.videoName,self.selectPredictModelPath,self.selectFeatureModelPath,self.testPredictTime)
                    self.testPredictTime +=1
                    print('一张图片预测时间',onesecond)
                    self.allTime = onesecond*self.frameNumber/1000
                    print("\n预估时间为：",self.allTime)
                # if self.isStart:
                self.predictThread = threading.Thread(target=StartPredictNow,
                                                       args=[self.selectVedioPath, threadhold, usGPU, self.save_dir,
                                                             self.videoName, self.selectPredictModelPath,
                                                             self.selectFeatureModelPath,self.testPredictTime])
                    # self.isStart = False
                self.predictThread.start()
                self.labelTime.setText('预估时间: {:.2f} 秒'.format(self.allTime))
                self.label_2.setText("视频输出窗口\n 默认路径均已填写完毕，只需选择所需要预测的视频")
                self.selectVedioPath = None
                if self.timer.isActive():
                    # 停止
                    self.timer.stop()
                # 判断数字是否大于100
                elif self.step >= 100:
                    self.step = 0
                    # 把进度条赋值给
                    self.pbar.setValue(self.step)
                else:
                    self.timer.start(100, self)
            except ValueError as v:
                if usGPU:
                    QtWidgets.QMessageBox.warning(self, "警告", "未在该机器上检测出可用GPU,请不要使用GPU", QtWidgets.QMessageBox.Cancel)
                    self.checkBox.setChecked(False)
                else:
                    QtWidgets.QMessageBox.warning(self, "警告", "出现未知错误", QtWidgets.QMessageBox.Cancel)

            # QtWidgets.QApplication.processEvents()
    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            # 停止进度条
            self.timer.stop()
            self.labelTime.setText('可以显示结果')
            self.pushButton6.setText("预测结果显示")
            return

        if self.predictThread.is_alive() and self.step<=90:
           self.step = self.step + 1
        elif not self.predictThread.is_alive():
            self.step = self.step + 1
        # 把进度条赋值给
        self.pbar.setValue(self.step)

if __name__ == "__main__":
    import traceback

    try:
        multiprocessing.freeze_support()
        app = QtWidgets.QApplication(sys.argv)
        ui = mywindow()
        ui.show()
        sys.exit(app.exec_())
    except Exception as e:
        traceback.print_exc()
