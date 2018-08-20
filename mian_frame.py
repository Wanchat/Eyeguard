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



        self.initShow_frame()
        self.call_event()
        self.button_clink()
        self.button_hide()

    def closeEvent(self, event):
        self.th.stop()
        QWidget.closeEvent(self, event)

    def initShow_frame(self):
        self.th = Thread(self)
        self.th.changePixmap.connect(self.image_label.setPixmap)
        self.th.start()

    def call_event(self):
        self.call_time = None
        self.call_blink = None
        self.call_angle = None
        self.call_distance = None
        self.call_sex = None
        self.call_age = None
        self.call_bright = None

    def button_clink(self):
        self.button_menu.clicked.connect(self.bt_menu_active)
        self.button_menu_2.clicked.connect(self.bt_menu_close)
        self.button_time.clicked.connect(self.bt_time_active)
        self.button_time_2.clicked.connect(self.bt_time_close)
        self.button_blink.clicked.connect(self.bt_blink_active)
        self.button_blink_2.clicked.connect(self.bt_blink_close)
        self.button_angle.clicked.connect(self.bt_angle_active)
        self.button_angle_2.clicked.connect(self.bt_angle_close)
        self.button_distance.clicked.connect(self.bt_distance_active)
        self.button_distance_2.clicked.connect(self.bt_distance_close)
        self.button_sex.clicked.connect(self.bt_sex_active)
        self.button_sex_2.clicked.connect(self.bt_sex_close)
        self.button_age.clicked.connect(self.bt_age_active)
        self.button_age_2.clicked.connect(self.bt_age_close)
        self.button_bright.clicked.connect(self.bt_bright_active)
        self.button_bright_2.clicked.connect(self.bt_bright_close)

    def button_hide(self):
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





# class btn_action(Eyeguard_n):
#     def __init__(self):
#         super(btn_action,self).__init__()


    def active_button(self, show, hide):
        show.show()
        hide.hide()

    def bt_menu_active(self):
        self.widget_menu.show()
        self.active_button(self.button_menu_2, self.button_menu)


    def bt_menu_close(self):
        self.widget_menu.hide()
        self.active_button(self.button_menu, self.button_menu_2)


    def bt_time_active(self):
        self.active_button(self.button_time_2, self.button_time)
        self.call_time = True
        return self.call_time


    def bt_time_close(self):
        self.active_button(self.button_time, self.button_time_2)
        self.call_time = False
        return self.call_time


    def bt_blink_active(self):
        self.active_button(self.button_blink_2, self.button_blink)


    def bt_blink_close(self):
        self.active_button(self.button_blink, self.button_blink_2)


    def bt_angle_active(self):
        self.active_button(self.button_angle_2, self.button_angle)


    def bt_angle_close(self):
        self.active_button(self.button_angle, self.button_angle_2)


    def bt_distance_active(self):
        self.active_button(self.button_distance_2, self.button_distance)


    def bt_distance_close(self):
        self.active_button(self.button_distance, self.button_distance_2)


    def bt_sex_active(self):
        self.active_button(self.button_sex_2, self.button_sex)


    def bt_sex_close(self):
        self.active_button(self.button_sex, self.button_sex_2)


    def bt_age_active(self):
        self.active_button(self.button_age_2, self.button_age)


    def bt_age_close(self):
        self.active_button(self.button_age, self.button_age_2)


    def bt_bright_active(self):
        self.active_button(self.button_bright_2, self.button_bright)


    def bt_bright_close(self):
        self.active_button(self.button_bright, self.button_bright_2)



class Thread(QThread, Eyeguard_n):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True
        self.cap = cv2.VideoCapture(1)
        self.call_time = None


    def run(self):
        while self.isRunning:
            _, self.frame = self.cap.read()
            # if self.isRunning == True:
            #     self.call_time = "yessss"
            # else:
            #     self.call_time = "nooooo"
            # print(self.t)
            # self.frame = q_2.get()
            print(self.call_time)
            self.out_qt()

    # out display pyqt
    def out_qt(self):


        rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data,
                                   rgbImage.shape[1],
                                   rgbImage.shape[0],
                                   QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)

            # self.test()

    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Eyeguard_n()
    window.show()
    sys.exit(app.exec_())