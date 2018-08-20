
import os
import sys

import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import   QBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt


from style import Style


class Pop_alert_age(QWidget):

    def __init__(self, x):
        super().__init__()

        self.x = "You is age {} !".format(x)

        self.stylegui = Style()
        self.style = self.stylegui.initgui()
        self.setStyleSheet(self.style)

        self.title = 'CHANGE SCREEN'

        self.screen_wide, self.screen_high = pyautogui.size()
        self.screen_wide_c = self.screen_wide / 2
        self.screen_high_c = self.screen_high / 2

        self.width = 480
        self.height = 200

        self.left = self.screen_wide_c - (self.width / 2)
        self.top = self.screen_high_c - (self.height / 2)

        self.bt_width = 100
        self.bt_hight = 30
        self.bt_width_c = self.bt_width / 2

        self.pop_center_w = self.width / 2

        self.lb_1_width = 460
        self.lb_1_hight = 40

        self.lb_1_top = 80
        self.lb_1_left = 10

        self.lb_2_top = 40
        self.lb_2_left = 10

        self.text = "Do you want to change the screen?"

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.setWindowIcon(QIcon(
            r'D:\code_python\Eyeguard\data\icon_eyeguard.png'))

        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.setGeometry(self.left, self.top, self.width, self.height)

        label_1 = QLabel(self.text, self)
        label_1.setStyleSheet(
            "font-size: 20px;"
        )
        label_1.setAlignment(Qt.AlignCenter)

        label_1.resize(self.lb_1_width, self.lb_1_hight)
        label_1.move(self.lb_1_left, self.lb_1_top)

        label_2 = QLabel(self.x, self)
        label_2.resize(self.lb_1_width, self.lb_1_hight)
        label_2.move(self.lb_2_left, self.lb_2_top)

        label_2.setAlignment(Qt.AlignCenter)

        label_2.setStyleSheet(
            "font-size: 30px; color:#00bfff;"
        )

        bt_ok = QPushButton('OK', self)
        bt_cancel = QPushButton('CANCEL', self)

        bt_ok.resize(self.bt_width, self.bt_hight)
        bt_cancel.resize(self.bt_width, self.bt_hight)

        bt_ok.move(130, 140)
        bt_cancel.move(250, 140)

        bt_ok.clicked.connect(self.open_display)
        bt_cancel.clicked.connect(self.exit_popup)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.show()

    @pyqtSlot()
    def open_display(self):
        os.system("start ms-settings:display")
        sys.exit()

    def exit_popup(self):
        sys.exit()


class Pop_alert_all(QWidget):
    def __init__(self,
                 value_time = '',
                 value_blink = '',
                 value_angle = '',
                 value_distance = ''
                 ):
        super().__init__()

        self.value_time = value_time
        self.value_blink = value_blink
        self.value_angle = value_angle
        self.value_distance = value_distance

        self.stylegui = Style()
        self.style = self.stylegui.initgui()
        self.setStyleSheet(self.style)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.screen_wide, self.screen_high = pyautogui.size()

        self.width = 300
        self.height = 120
        self.left = self.screen_wide - self.width
        self.top = 0

        self.lb_1_left = 95
        self.lb_1_top =  25
        self.lb_1_width = 190
        self.lb_1_height = 80

        self.setGUI()

    def setGUI(self):
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height,)

        label_1 = QLabel(self)
        label_1.resize(self.lb_1_width, self.lb_1_height)
        label_1.move(self.lb_1_left, self.lb_1_top)

        label_1.setStyleSheet("""
        
            font-size:13px;
        
        """)

        if self.value_blink != '':
            self.value_blink = '\n{}'.format(self.value_blink)

        if self.value_angle != '':
            self.value_angle = '\n{}'.format(self.value_angle)

        if self.value_distance != '':
            self.value_distance = '\n{}'.format(self.value_distance)

        label_1.setText('{}{}{}{}'.format(self.value_time,
                                                   self.value_blink,
                                                   self.value_angle,
                                                   self.value_distance))

        label_image = QLabel(self)
        label_image.setGeometry(15,25,70,70)
        label_image.setStyleSheet("""
            border: 1px solid  black;
            border-image: url(logo_eyeguard.svg);
            background-color: transparent;
             
        """)

        bt_close = QPushButton(self)

        bt_close.setStyleSheet("""
            border-image: url(icon_close.png);
            background-color: transparent;
            border-radius: 0px;

        
        """)

        bt_close.resize(10,10)
        bt_close.move(self.width-20,10)

        bt_close.clicked.connect(self.popup_close)

        self.show()

    def popup_close(self):
        sys.exit()


if __name__ == '__main__':

    # def chage_screen_age(age):
    #
    #     if age == "older40":
    #         app = QApplication(sys.argv)
    #         alert = Pop_alert_age(age)
    #         sys.exit(app.exec_())
    #     else:
    #         pass
    def popup_show(popup_time):
        if popup_time[1] == True:
            app = QApplication(sys.argv)
            alert_all = Pop_alert_all(value_time= popup_time[0])
            sys.exit(app.exec_())

    time = (20, True)
    popup_show(time)

    # app = QApplication(sys.argv)
    # alert_all = Pop_alert_all(value_time = 'time',
    #                           value_blink ='blink',
    #                           value_angle = 'angle',
    #                           value_distance='distance')
    # sys.exit(app.exec_())

    # chage_screen_age("older40")

