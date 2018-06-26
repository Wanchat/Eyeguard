import cv2
import sys
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap


class Test_qt(QDialog):

    def __init__(self):
        super(Test_qt,self).__init__()
        loadUi('test_qyqt.ui', self)

        self.image = None
        self.startButton.clicked.connect(self.start_webcam)
        self.stopButton.clicked.connect(self.stop_webcam)
        self.capture = cv2.VideoCapture(0)

    def start_webcam(self):
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        ret, self.image = self.capture.read()
        # self.image = cv2.flip(self.image,1)

        self.image_camera(self.image)

        self.displayImage(self.image,1)

    def stop_webcam(self):
        self.timer.stop()

    def displayImage(self, img: np.ndarray, window = 1):
       
        height, width, colors = img.shape
        bytesPerLine = 3 * width
        qformat = QImage.Format_RGB888

        outImage = QImage(img.data, width, height, bytesPerLine, qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imageLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imageLabel.setScaledContents(True)
    
    def image_camera(self,img):
        img = self.image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img[0:20,0:20] = 0

        print(img)
    #     return img

    # def __str__(self):
    #     return self.image_camera()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Test_qt()
    window.setWindowTitle("test")
    window.show()
    sys.exit(app.exec_())