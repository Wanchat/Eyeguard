import cv2
import sys
import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from brightness import Brightness


class EyeguardNew(QDialog):

    def __init__(self):

        super(EyeguardNew,self).__init__()
        loadUi(r'D:\code_python\Eyeguard\icon\eyeguade.ui', self)
        self.capture = cv2.VideoCapture(1)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_closs.clicked.connect(self.bt_close)

        # args
        self.image = None
        self.gray = None
        self.call_time = None
        self.call_blink = None
        self.call_angle = None
        self.call_distance = None
        self.call_sex = None
        self.call_age = None
        self.call_bright = None

        # import class
        # self.time_class = Time_new()
        # self.blink_class = Blink()
        # self.angle_class = Angle()
        # self.distance_class = Distance()
        # self.sex_class = Sex()
        # self.age_class = Age()
        self.bright_class = Brightness()
        
        # buttom
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
        self.pushButton_menu.hide()

        self.widget_bar.hide()


    # webcam start
    def start(self):
        self.pushButton_menu.show()
        self.pushButton_start.hide()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.frame)
        self.timer.start(1)

    # frame______________
    def frame(self):
        ret, self.image = self.capture.read()

        if self.call_time == True:
            self.time_def()
        elif self.call_blink == True:
            self.angle_def()
        elif self.call_angle == True:
            self.angle_def()
        elif self.call_distance == True:
            self.distance_def()
        elif self.call_sex == True:
            self.sex_def()
        elif self.call_age == True:
            self.age_def()
        elif self.call_bright == True:
            self.brightness_def()
        else:
            pass

        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #gray image
        self.displayImage(self.image,1) # display window qt

    # clicked
    def clicked_time(self, ok_time):
        if ok_time :
            self.call_time = True
        else:
            self.call_time = False
        return self.call_time

    def clicked_blink(self, ok_blink):
        if ok_blink :
            self.call_blink = True
        else:
            self.call_blink = False
        return self.call_blink

    def clicked_angle(self, ok_angle):
        if ok_angle :
            self.call_angle = True
        else:
            self.call_angle = False
        return self.call_angle
        
    def clicked_distance(self, ok_distance):
        if ok_distance :
            self.call_distance = True
        else:
            self.call_distance = False
        return self.call_distance

    def clicked_sex(self, ok_sex):
        if ok_sex :
            self.call_sex = True
        else:
            self.call_sex = False
        return self.call_sex

    def clicked_age(self, ok_age):
        if ok_age :
            self.call_age = True
        else:
            self.call_age = False
        return self.call_age

    def clicked_bright(self, ok_bright):
        if ok_bright :
            self.call_bright = True
        else:
            self.call_bright = False
        return self.call_bright

    # class method
    def time_def(self):
        pass
    def blink_def(self):
        pass
    def angle_def(self):
        pass
    def distance_def(self):
        pass
    def sex_def(self):
        pass
    def age_def(self):
        pass
    def brightness_def(self):
        self.v_c = self.bright_class.brightness(self.gray)
        self.s_b = self.bright_class.change_screen(self.v_c)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(self.image,
                    "brightness: {}".format(self.v_c),
                    (15,30),font, 0.5, (0,255,0), 0)

    # display screen
    def displayImage(self, img: np.ndarray, window = 1):
        height, width, colors = img.shape
        bytesPerLine = 3 * width
        qformat = QImage.Format_RGB888
        outImage = QImage(img.data, width, height, bytesPerLine, qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.label_image.setPixmap(QPixmap.fromImage(outImage))
            self.label_image.setScaledContents(True)


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
        self.call_time = True
        return  self.call_time

    def bt_time_close(self):
        self.active_button(self.pushButton_time, self.pushButton_time_2)
        self.call_time = False
        return self.call_time

    def bt_blink_active (self):
        self.active_button(self.pushButton_blink_2, self.pushButton_blink)
        self.call_blink = True
        return self.call_blink

    def bt_blink_close(self):
        self.active_button(self.pushButton_blink, self.pushButton_blink_2)
        self.call_blink = False
        return self.call_blink

    def bt_angle_active (self):
        self.active_button(self.pushButton_angle_2, self.pushButton_angle)
        self.call_angle = True
        return self.call_angle
    def bt_angle_close(self):
        self.active_button(self.pushButton_angle, self.pushButton_angle_2)
        self.call_angle = False
        return self.call_angle

    def bt_distance_active (self):
        self.active_button(self.pushButton_distance_2, self.pushButton_distance)
        self.call_distance = True
        return self.call_distance

    def bt_distance_close(self):
        self.active_button(self.pushButton_distance, self.pushButton_distance_2)
        self.call_distance = False
        return self.call_distance

    def bt_sex_active (self):
        self.active_button(self.pushButton_sex_2, self.pushButton_sex)
        self.call_sex = True
        return self.call_sex

    def bt_sex_close(self):
        self.active_button(self.pushButton_sex, self.pushButton_sex_2)
        self.call_sex = False
        return self.call_sex

    def bt_age_active (self):
        self.active_button(self.pushButton_age_2, self.pushButton_age)
        self.call_age = True
        return self.call_age

    def bt_age_close(self):
        self.active_button(self.pushButton_age, self.pushButton_age_2)
        self.call_age = False
        return self.call_age

    def bt_bright_active (self):
        self.active_button(self.pushButton_bright_2, self.pushButton_bright)
        self.call_bright = True
        return self.call_bright

    def bt_bright_close(self):
        self.active_button(self.pushButton_bright, self.pushButton_bright_2)
        self.call_bright = False
        return self.call_bright

    def bt_close(self):
        sys.exit(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EyeguardNew()
    window.show()
    sys.exit(app.exec_())
