import cv2
import sys
import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from brightness import Brightness

class Test:
    def test(self):
        return 'hello'

class EyeguardNew(QDialog):

    def __init__(self):

        super(EyeguardNew,self).__init__()
        loadUi(r'D:\code_python\Eyeguard\icon\eyeguade.ui', self)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_closs.clicked.connect(self.bt_close)

        self.pushButton_menu.clicked.connect(self.bt_menu_active)
        self.pushButton_menu_active.clicked.connect(self.bt_menu_close)
        self.pushButton_time.clicked.connect(self.bt_time_active)
        self.pushButton_time_2.clicked.connect(self.bt_time_close)
        self.pushButton_blink.clicked.connect(self.bt_blink_active)
        self.pushButton_blink_2.clicked.connect(self.bt_blink_close)
        self.pushButton_angle.clicked.connect(self.bt_angle_active)
        self.pushButton_angle_2.clicked.connect(self.bt_angle_close)
        self.pushButton_distance.clicked.connect(self.bt_distance_active)
        self.pushButton_distance_2.clicked.connect(self.bt_distance_close)
        self.pushButton_sex.clicked.connect(self.bt_sex_active)
        self.pushButton_sex_2.clicked.connect(self.bt_sex_close)
        self.pushButton_age.clicked.connect(self.bt_age_active)
        self.pushButton_age_2.clicked.connect(self.bt_age_close)
        self.pushButton_bright.clicked.connect(self.bt_bright_active)
        self.pushButton_bright_2.clicked.connect(self.bt_bright_close)


        self.pushButton_menu_active.hide()
        self.pushButton_time_2.hide()
        self.pushButton_blink_2.hide()
        self.pushButton_angle_2.hide()
        self.pushButton_distance_2.hide()
        self.pushButton_sex_2.hide()
        self.pushButton_age_2.hide()
        self.pushButton_bright_2.hide()

        self.widget_bar.hide()

#  start
    def start(self):
        self.pushButton_start.hide()
        self.pushButton_menu.show()

# button active
    def active_button(self, show, hide):
        show.show()
        hide.hide()

    def bt_menu_active (self):
        self.widget_bar.show()
        self.active_button(self.pushButton_menu_active, self.pushButton_menu)

    def bt_menu_close(self):
        self.widget_bar.hide()
        self.active_button(self.pushButton_menu, self.pushButton_menu_active)

    def bt_time_active (self):
        self.active_button(self.pushButton_time_2, self.pushButton_time)

    def bt_time_close(self):
        self.active_button(self.pushButton_time, self.pushButton_time_2)

    def bt_blink_active (self):
        self.active_button(self.pushButton_blink_2, self.pushButton_blink)

    def bt_blink_close(self):
        self.active_button(self.pushButton_blink, self.pushButton_blink_2)

    def bt_angle_active (self):
        self.active_button(self.pushButton_angle_2, self.pushButton_angle)

    def bt_angle_close(self):
        self.active_button(self.pushButton_angle, self.pushButton_angle_2)

    def bt_distance_active (self):
        self.active_button(self.pushButton_distance_2, self.pushButton_distance)

    def bt_distance_close(self):
        self.active_button(self.pushButton_distance, self.pushButton_distance_2)

    def bt_sex_active (self):
        self.active_button(self.pushButton_sex_2, self.pushButton_sex)

    def bt_sex_close(self):
        self.active_button(self.pushButton_sex, self.pushButton_sex_2)

    def bt_age_active (self):
        self.active_button(self.pushButton_age_2, self.pushButton_age)

    def bt_age_close(self):
        self.active_button(self.pushButton_age, self.pushButton_age_2)

    def bt_bright_active (self):
        self.active_button(self.pushButton_bright_2, self.pushButton_bright)

    def bt_bright_close(self):
        self.active_button(self.pushButton_bright, self.pushButton_bright_2)

    def bt_close(self):
        sys.exit(0)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = EyeguardNew()
    window.show()
    sys.exit(app.exec_())