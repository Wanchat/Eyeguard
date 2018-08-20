import dlib
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import os
import sys

import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Age:

    def __init__(self, model=r"D:\code_python\Eyguard_cnn\age\age_50.model"):

        self.madel_age = load_model(model)
        self.alert = False
        self.frame = 0

    def gui_alert_age(self):
        pass

    def estimate_age(self, window_face):

        self.window_face = cv2.resize(window_face, (28, 28))
        self.window_face = window_face.astype("float") / 255.0
        self.window_face = img_to_array(self.window_face)
        self.window_face = np.expand_dims(self.window_face, axis=0)

        (self.under, self.older) = self.madel_age.predict(self.window_face)[0]

        self.label_age = "older40" if self.older > self.under else "under40"
        self.score_age = self.older if self.older > self.under else self.under

        return self.label_age, self.score_age

    def chage_screen(self, age):

        if age != None:
            self.frame += 1

        else:
            if self.frame == 10:

                if age == "older40":
                    pass
                    # alert show
                else:
                    pass

        if self.alert == True:
            os.system("start ms-settings:display")
        else:
            pass


class pip_alert_age(QWidget):

    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setGeometry()

        text = "You want to change screen display !"

        lb_1 =QLabel(text)
        lb_1.setAlignment(Qt.AlignHCenter)

        bt_ok = QPushButton("OK")
        bt_cancel = QPushButton("CANCEL")

        horizon_box_1 = QHBoxLayout()
        horizon_box_1.addWidget(lb_1)

        horizon_box_2 = QHBoxLayout()
        horizon_box_2.addWidget(bt_ok)
        horizon_box_2.addWidget(bt_cancel)

        self.vertical_box = QVBoxLayout()
        self.vertical_box.addLayout(horizon_box_1)
        self.vertical_box.addLayout(horizon_box_2)


        self.setLayout(self.vertical_box)

        self.setWindowTitle("EYEGUARD AGE")
        self.setGeometry(500, 360, 20, 20)


    @pyqtSlot()
    def open_display(self):
        os.system("start ms-settings:display")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pip_alert_age()
    ex.show()
    sys.exit(app.exec_())