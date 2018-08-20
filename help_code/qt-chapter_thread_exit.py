import sys
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.uic import loadUi

import datetime


class App(QWidget):
    def __init__(self):
        super(App,self).__init__()
        loadUi(r'D:\code_python\Eyeguard\help_code\untitled_widget.ui', self)
        # self.startButton.clicked.connect(self.initUI)
        self.initUI()

    def initUI(self):

        self.th = Thread(self)
        self.th.changePixmap.connect(self.label.setPixmap)
        self.th.start()

    def closeEvent(self, event):
        self.th.stop()
        QWidget.closeEvent(self, event)

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    changeLabel = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self.isRunning:
            ret, frame = cap.read()
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data,
                                       rgbImage.shape[1],
                                       rgbImage.shape[0],
                                       QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            now = datetime.datetime.now()
            sec = now.second
            self.changeLabel.emit(str(sec))

    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())