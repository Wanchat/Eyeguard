import cv2
import sys
import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
# from brightness import Brightness
# from extend_eye import Extand_eyes
# from extend_face_haar import Extend_face_haar
# from detect_sex_new import Sex
# from detect_age_new import Age
# from distance_angle import Angle, Distance
# from blink import Blink


class EyeguardNew(QWidget):

    def __init__(self):

        super(EyeguardNew, self).__init__()
        loadUi(r'D:\code_python\Eyeguard\help_code\untitled_widget.ui', self)
        self.capture = cv2.VideoCapture(0)
        self.startButton.clicked.connect(self.start)
        self.image = None


    # webcam start
    def start(self):

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.frame)
        self.timer.start(1)

    # frame
    def frame(self):
        ret, self.image = self.capture.read()


        self.displayImage(self.image, 1)

    # display screen
    def displayImage(self, img: np.ndarray, window=1):
        height, width, colors = img.shape
        bytesPerLine = 3 * width
        qformat = QImage.Format_RGB888
        outImage = QImage(img.data,
                          width, 
                          height,
                          bytesPerLine,
                          qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.label.setPixmap(QPixmap.fromImage(outImage))
            self.label.setScaledContents(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EyeguardNew()
    # window.setWindowFlags(Qt.CustomizeWindowHint)
    window.show()
    sys.exit(app.exec_())
