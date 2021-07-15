# import pygame as py
# import _thread
# import time
# import tkinter as tk
# from tkinter import *
# import cv2
# from PIL import Image, ImageTk
# import multiprocessing
# class mainWindow():
#     def __init__(self):
#         self.window_width=960
#         self.window_height=720
#         self.image_width=int(self.window_width*0.5)
#         self.image_height=int(self.window_height*0.5)
#         self.imagepos_x=0
#         self.imagepos_y=0
#         self.butpos_x=450
#         self.butpos_y=450
#         self.vc1 = cv2.VideoCapture('D:\\QQ_this\\qq_message\\2689102713\\FileRecv\\cocos电子资源导出教程.mp4')  #读取视频
#         '''布局'''
#         print("shuchu")

    
#     #图像转换，用于在画布中显示
#     def tkImage(self,vc):
#         ref,frame = vc.read()
#         cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         pilImage = Image.fromarray(cvimage)
#         pilImage = pilImage.resize((self.image_width, self.image_height),Image.ANTIALIAS)
#         tkImage =  ImageTk.PhotoImage(image=pilImage)
#         return tkImage
#     #图像的显示与更新
#     def video(self):
#         def video_loop(self):
#             try:
#                 while True:
#                     picture1=self.tkImage(self.vc1)
#                     self.canvas1.create_image(0,0,anchor='nw',image=picture1)  
#                     self.win.update_idletasks()  #最重要的更新是靠这两句来实现
#                     self.win.update()
#             except:
#                 pass
            
#         video_loop()
#         self.win.mainloop()
#         self.vc1.release()
#         cv2.destroyAllWindows()
#     def StartCheck(self):
#         p1 = multiprocessing.Process(target=self.video)
#         p1.start()

# mw = mainWindow()
# win = tk.Tk()
# win.geometry(str(mw.window_width)+'x'+str(mw.window_height))
# canvas1 =Canvas(win,bg='white',width=mw.image_width,height=mw.image_height)
# canvas1.place(x=mw.imagepos_x,y=mw.imagepos_y)
# mw.StartCheck()
import time
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cv2 import *


class VideoBox(QWidget):

    VIDEO_TYPE_OFFLINE = 0
    VIDEO_TYPE_REAL_TIME = 1

    STATUS_INIT = 0
    STATUS_PLAYING = 1
    STATUS_PAUSE = 2

    video_url = ""

    def __init__(self, video_url="", video_type=VIDEO_TYPE_OFFLINE, auto_play=False):
        QWidget.__init__(self)
        self.video_url = video_url
        self.video_type = video_type  # 0: offline  1: realTime
        self.auto_play = auto_play
        self.status = self.STATUS_INIT  # 0: init 1:playing 2: pause

        # 组件展示
        self.pictureLabel = QLabel()
        init_image = QPixmap("C:\\Users\\xmj\\Desktop\\tezheng\\train\\3\\13.jpg").scaled(self.width(), self.height())
        self.pictureLabel.setPixmap(init_image)

        self.playButton = QPushButton()
        self.playButton.setEnabled(True)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.switch_video)

        control_box = QHBoxLayout()
        control_box.setContentsMargins(0, 0, 0, 0)
        control_box.addWidget(self.playButton)

        layout = QVBoxLayout()
        layout.addWidget(self.pictureLabel)
        layout.addLayout(control_box)

        self.setLayout(layout)

        # timer 设置
        self.timer = VideoTimer()
        self.timer.timeSignal.signal[str].connect(self.show_video_images)

        # video 初始设置
        self.playCapture = VideoCapture()
        if self.video_url != "":
            self.set_timer_fps()
            if self.auto_play:
                self.switch_video()
            # self.videoWriter = VideoWriter('*.mp4', VideoWriter_fourcc('M', 'J', 'P', 'G'), self.fps, size)

    def reset(self):
        self.timer.stop()
        self.playCapture.release()
        self.status = VideoBox.STATUS_INIT
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_timer_fps(self):
        self.playCapture.open(self.video_url)
        fps = self.playCapture.get(CAP_PROP_FPS)
        self.timer.set_fps(fps)
        self.playCapture.release()

    def set_video(self, url, video_type=VIDEO_TYPE_OFFLINE, auto_play=False):
        self.reset()
        self.video_url = url
        self.video_type = video_type
        self.auto_play = auto_play
        self.set_timer_fps()
        if self.auto_play:
            self.switch_video()

    def play(self):
        if self.video_url == "" or self.video_url is None:
            return
        if not self.playCapture.isOpened():
            self.playCapture.open(self.video_url)
        self.timer.start()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.status = VideoBox.STATUS_PLAYING

    def stop(self):
        if self.video_url == "" or self.video_url is None:
            return
        if self.playCapture.isOpened():
            self.timer.stop()
            if self.video_type is VideoBox.VIDEO_TYPE_REAL_TIME:
                self.playCapture.release()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.status = VideoBox.STATUS_PAUSE

    def re_play(self):
        if self.video_url == "" or self.video_url is None:
            return
        self.playCapture.release()
        self.playCapture.open(self.video_url)
        self.timer.start()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.status = VideoBox.STATUS_PLAYING

    def show_video_images(self):
        if self.playCapture.isOpened():
            success, frame = self.playCapture.read()
            if success:
                height, width = frame.shape[:2]
                if frame.ndim == 3:
                    rgb = cvtColor(frame, COLOR_BGR2RGB)
                elif frame.ndim == 2:
                    rgb = cvtColor(frame, COLOR_GRAY2BGR)

                temp_image = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
                temp_pixmap = QPixmap.fromImage(temp_image)
                self.pictureLabel.setPixmap(temp_pixmap)
            else:
                print("read failed, no frame data")
                success, frame = self.playCapture.read()
                if not success and self.video_type is VideoBox.VIDEO_TYPE_OFFLINE:
                    print("play finished")  # 判断本地文件播放完毕
                    self.reset()
                    self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
                return
        else:
            print("open file or capturing device error, init again")
            self.reset()

    def switch_video(self):
        if self.video_url == "" or self.video_url is None:
            return
        if self.status is VideoBox.STATUS_INIT:
            self.playCapture.open(self.video_url)
            self.timer.start()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        elif self.status is VideoBox.STATUS_PLAYING:
            self.timer.stop()
            if self.video_type is VideoBox.VIDEO_TYPE_REAL_TIME:
                self.playCapture.release()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        elif self.status is VideoBox.STATUS_PAUSE:
            if self.video_type is VideoBox.VIDEO_TYPE_REAL_TIME:
                self.playCapture.open(self.video_url)
            self.timer.start()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        self.status = (VideoBox.STATUS_PLAYING,
                       VideoBox.STATUS_PAUSE,
                       VideoBox.STATUS_PLAYING)[self.status]


class Communicate(QObject):

    signal = pyqtSignal(str)


class VideoTimer(QThread):

    def __init__(self, frequent=20):
        QThread.__init__(self)
        self.stopped = False
        self.frequent = frequent
        self.timeSignal = Communicate()
        self.mutex = QMutex()

    def run(self):
        with QMutexLocker(self.mutex):
            self.stopped = False
        while True:
            if self.stopped:
                return
            self.timeSignal.signal.emit("1")
            time.sleep(1 / self.frequent)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    def is_stopped(self):
        with QMutexLocker(self.mutex):
            return self.stopped

    def set_fps(self, fps):
        self.frequent = fps


if __name__ == "__main__":
    mapp = QApplication(sys.argv)
    mw = VideoBox()
    mw.set_video("D:\\QQ_this\\qq_message\\2689102713\\FileRecv\\cocos电子资源导出教程.mp4", VideoBox.VIDEO_TYPE_OFFLINE, False)
    mw.show()
    sys.exit(mapp.exec_())
