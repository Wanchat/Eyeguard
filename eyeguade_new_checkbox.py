import cv2
import sys
import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap

from extend_eye import Extand_eyes
from extend_face_haar import Extend_face_haar

from blink import Blink
from distance_angle import Angle, Distance
from detect_age_new import Age
from detect_sex_new import Sex
from brightness import Brightness


class EyeguardNew(QDialog):

    def __init__(self):

        super(EyeguardNew,self).__init__()
        loadUi(r'D:\code_python\Eyeguard\icon\eyeguade_speed.ui', self)
        self.capture = cv2.VideoCapture(1)
        self.pushButton_start.clicked.connect(self.start)
        # self.pushButton_closs.clicked.connect(self.bt_close)

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
        self.blink_class = Blink()
        self.angle_class = Angle()
        self.distance_class = Distance()
        self.sex_class = Sex()
        self.age_class = Age()
        self.bright_class = Brightness()
        self.extend_eye_point = Extand_eyes()
        self.extend_faceHaar = Extend_face_haar()
        
        # buttom
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_close.clicked.connect(self.bt_close)

        self.pushButton_menu.hide()
        self.pushButton_menu_2.hide()
        self.pushButton_menu.clicked.connect(self.clicked_menu)
        self.pushButton_menu_2.clicked.connect(self.clicked_menu_close)

        self.checkBox_time.stateChanged.connect(self.clicked_time)
        self.checkBox_blink.stateChanged.connect(self.clicked_blink)
        self.checkBox_angle.stateChanged.connect(self.clicked_angle)
        self.checkBox_distance.stateChanged.connect(self.clicked_distance)
        self.checkBox_sex.stateChanged.connect(self.clicked_sex)
        self.checkBox_age.stateChanged.connect(self.clicked_age)
        self.checkBox_bright.stateChanged.connect(self.clicked_bright)
        self.widget_menu.hide()

        self.center_right_x = None
        self.center_right_y = None
        self.center_left_x = None
        self.center_left_y = None
        self.point_center_x = None
        self.point_center_y = None
        self.rightEye = None
        self.leftEye = None
        self.xywh = None
        self.face_window = None


        # webcam start
    def start(self):
        self.pushButton_menu.show()
        self.pushButton_start.hide()
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.frame)
        self.timer.start(0.0001)

    # frame______________
    def frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image, 1)

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

        # gray image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # extend_eye function
        self.eye_point = self.extend_eye_point.extend(self.gray)

        if self.eye_point == None:
            pass
        else:
            self.center_right_x = self.eye_point["center_right_x"]
            self.center_right_y = self.eye_point["center_right_y"]
            self.center_left_x = self.eye_point["center_left_x"]
            self.center_left_y = self.eye_point["center_left_y"]
            self.point_center_x = self.eye_point["point_center_x"]
            self.point_center_y = self.eye_point["point_center_y"]
            self.rightEye = self.eye_point["rightEye"]
            self.leftEye = self.eye_point["leftEye"]

        # # extend face window
        self.xywh = self.extend_faceHaar.extend_face(self.gray)
        self.face_window = self.extend_faceHaar.window_face(
            self.xywh, self.image)


        # display window qt
        # self.displayImage(self.image,1)

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

    def clicked_menu(self):
        self.widget_menu.show()
        self.pushButton_menu.hide()
        self.pushButton_menu_2.show()

    def clicked_menu_close(self):
        self.widget_menu.hide()
        self.pushButton_menu.show()
        self.pushButton_menu_2.hide()

# class method
    def time_def(self):
        pass

    def blink_def(self):

        self.blink = self.blink_class.earAvg(self.leftEye, self.rightEye)
        print(self.blink)
        return self.blink

    def angle_def(self):

        self.angle = self.angle_class.estimate_angle(self.point_center_y )
        print(self.angle)
        return self.angle


    def distance_def(self):

        self.angle_distance = self.angle_class.estimate_angle(self.point_center_y)
        self.distance = self.distance_class.estimate_distance(
            self.angle_distance, self.point_center_x,
            self.point_center_y,self.center_right_x)

        print(self.distance)
        return  self.distance

    def sex_def(self):
        try:
            self.sex = self.sex_class.estimate_sex(self.face_window)
            print(self.sex)
            return self.sex
        except:
            pass

    def age_def(self):
        try:
            self.age = self.age_class.estimate_age(self.face_window)
            print(self.age)
            return self.age
        except:
            pass

    def brightness_def(self):
        self.v_c = self.bright_class.brightness(self.gray)
        self.s_b = self.bright_class.change_screen(self.v_c)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(self.image, "brightness: {}".format(self.v_c), (15,30),font, 0.5, (0,255,0), 0)

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
    
    def bt_close(self):
        sys.exit(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EyeguardNew()
    # window.setWindowFlags(Qt.CustomizeWindowHint)
    window.show()
    sys.exit(app.exec_())
