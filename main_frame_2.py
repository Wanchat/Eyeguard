import cv2
import sys
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
import threading
from queue import Queue

q = Queue()
q_2 = Queue()

class Eyeguard_n(QMainWindow):
    def __init__(self):
        super(Eyeguard_n, self).__init__()
        loadUi(
            r'D:\code_python\Eyeguard'
            r'\icon\eyeguade_new.ui', self)

        self.initUI()
        self.button()

    def initUI(self):
        self.th = Thread()
        self.th.changePixmap.connect(self.image_label.setPixmap)
        self.th.start()

    def button(self):
        self.button_time_2.hide()
        self.button_blink_2.hide()
        self.button_angle_2.hide()
        self.button_distance_2.hide()
        self.button_sex_2.hide()
        self.button_age_2.hide()
        self.button_bright_2.hide()
        self.button_menu_2.hide()
        self.label.hide()
        self.widget_menu.hide()


    def closeEvent(self, event):
        self.th.stop()
        QWidget.closeEvent(self, event)


def test():
    print("a")



class Thread(QThread, QMainWindow):

    changePixmap = pyqtSignal(QPixmap)

    def __init__(self):
        super(Thread, self).__init__()
        self.cap = cv2.VideoCapture(1)


    def run(self):

        while self.isRunning:
            _, self.frame = self.cap.read()
            self.out_qt()


# out display pyqt
    def out_qt(self):

        rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data,
                                   rgbImage.shape[1],
                                   rgbImage.shape[0],
                                   QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(
            convertToQtFormat)
        p = convertToQtFormat.scaled(
            640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)


    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Eyeguard_n()
    window.show()
    sys.exit(app.exec_())