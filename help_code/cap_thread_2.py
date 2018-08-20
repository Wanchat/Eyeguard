import cv2
import numpy as np
import threading
from queue import Queue

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap

q = Queue()
q_2 = Queue()

class cv:
    def __init__(self):
        thread = threading.Thread(target=self.run)
        self.cap = cv2.VideoCapture(1)
        thread.start()

    def run(self):
        while True:
            _, self.frame = self.cap.read()
            q.put(self.frame)
            self.i = q_2.get()

    # def show(self):
            cv2.imshow("frame", self.i)

            if cv2.waitKey(1) == 27:
                break
class printTest:
    def __init__(self):
        cv()
        thread_2 = threading.Thread(target=self.ptest)
        thread_2.start()

    def ptest(self):
        while True:
            frame_2 = q.get()
            gray = cv2.cvtColor(frame_2,cv2.COLOR_BGR2GRAY)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame_2,"hello", (10,10),font,0.3,(0,255,0))
            q_2.put(frame_2)
            print(gray)

class Eyeguard_n(QMainWindow):
    def __init__(self):
        super(Eyeguard_n, self).__init__()
        loadUi(
            r'D:\code_python\Eyeguard'
            r'\icon\eyeguade_new.ui', self)


    def closeEvent(self, event):
        self.th.stop()
        QWidget.closeEvent(self, event)

    def initShow_frame(self):
        self.th = Thread(self)
        self.th.changePixmap.connect(self.image_label.setPixmap)
        self.th.start()

if __name__ == '__main__':
    # c = cv()
    # c.run()
    p = printTest()
    p.ptest()
    #
    # app = Qt.Application












