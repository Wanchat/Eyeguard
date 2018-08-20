from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog,\
    QCheckBox, QMainWindow, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt

import  sys
import cv2, numpy as np

from threading import Thread, Lock
from queue import Queue

from extend_eye import Extand_eyes
from extend_face_haar import Extend_face_haar

from blink import Blink
from distance_angle import Angle, Distance
# from detect_age_new import Age
# from detect_sex_new import Sex
from detect_brightness import Brightness

# self.button_time_2.clicked[bool].connect(
#     lambda click: self.h() if click else self.w())

class Wmain(QMainWindow):
    def __init__(self):
        super(Wmain, self).__init__()
        loadUi(r'D:\code_python\Eyeguard'
                r'\icon\eyeguade_tab_new.ui', self)

        self.call()
        self.button_connnet()
        self.object_hide()
        self.import_class_factors()

    def import_class_factors(self):
        self.blink_class = Blink()
        self.angle_class = Angle()
        self.distance_class = Distance()
        # self.sex_class = Sex()
        # self.age_class = Age()
        self.bright_class = Brightness()
        self.extend_eye_point = Extand_eyes()
        self.extend_faceHaar = Extend_face_haar()

    def call(self):
        self.call_time = None
        self.call_blink = None
        self.call_angle = None
        self.call_distance = None
        self.call_sex = None
        self.call_age = None
        self.call_bright = None

    def button_connnet(self):
        self.button_start.clicked.connect(self.start_wabcam_widget)

        self.button_time_2.setCheckable(True)
        self.button_blink_2.setCheckable(True)
        self.button_angle_2.setCheckable(True)
        self.button_distance_2.setCheckable(True)
        self.button_sex_2.setCheckable(True)
        self.button_age_2.setCheckable(True)
        self.button_bright_2.setCheckable(True)

        self.button_time_2.clicked[bool].connect(self.clicked_time)
        self.button_blink_2.clicked[bool].connect(self.clicked_blink)
        self.button_angle_2.clicked[bool].connect(self.clicked_angle)
        self.button_distance_2.clicked[bool].connect(self.clicked_distance)
        self.button_sex_2.clicked[bool].connect(self.clicked_sex)
        self.button_age_2.clicked[bool].connect(self.clicked_age)
        self.button_bright_2.clicked[bool].connect(self.clicked_bright)

    def object_hide(self):
        self.widget.hide()
        self.widget_2.hide()
        self.label_time.hide()
        self.label_blink.hide()
        self.label_angle.hide()
        self.label_distance.hide()
        self.label_sex.hide()
        self.label_age.hide()
        self.label_brightness.hide()


    def clicked_time(self, ok_time):
        if ok_time:
            self.call_time = True
        else:
            self.call_time = False

    def clicked_blink(self, ok_blink):
        if ok_blink:
            self.call_blink = True
        else:
            self.call_blink = False

    def clicked_angle(self, ok_angle):
        if ok_angle:
            self.call_angle = True
        else:
            self.call_angle = False

    def clicked_distance(self, ok_distance):
        if ok_distance:
            self.call_distance = True
        else:
            self.call_distance = False

    def clicked_sex(self, ok_sex):
        if ok_sex:
            self.call_sex = True
        else:
            self.call_sex = False

    def clicked_age(self, ok_age):
        if ok_age:
            self.call_age = True
        else:
            self.call_age = False

    def clicked_bright(self, ok_bright):
        if ok_bright:
            self.call_bright = True
        else:
            self.call_bright = False



# class method
    def time_def(self):
        pass

    def blink_def(self):

        self.blink = self.blink_class.earAvg(self.leftEye, self.rightEye)
        self.label_blink.show()

        text_blink = "Blink: {} EAR: {:.2f} Frame: {}".format(
            self.blink[0], self.blink[1], self.blink[2] )

        self.label_blink.setText(text_blink )
        return self.blink

    def angle_def(self):

        self.angle = self.angle_class.estimate_angle(self.point_center_y)
        text_angle = "Angle: {:.2f}".format(
            self.angle)

        self.label_angle.show()

        self.label_angle.setText(text_angle)
        return self.angle

    def distance_def(self):

        self.angle_distance = self.angle_class.estimate_angle(
            self.point_center_y)

        self.distance = self.distance_class.estimate_distance(
            self.angle_distance, self.point_center_x,
            self.point_center_y,self.center_right_x)

        text_distance = "Distance: {:.2f}".format(
            self.distance)

        self.label_distance.show()

        self.label_distance.setText(text_distance)

        return  self.distance

    def sex_def(self):
        try:
            self.sex = self.sex_class.estimate_sex(self.face_window)
            text_sex = "Sex: {} Score: {:.2f}".format(
                self.sex[0], self.sex[1])

            self.label_sex.show()

            self.label_sex.setText(text_sex)

            return self.sex
        except:
            pass

    def age_def(self):
        try:
            self.age = self.age_class.estimate_age(self.face_window)
            text_age = "Age: {} Score: {:.2f}".format(
                self.age[0], self.age[1])

            self.label_age.show()

            self.label_age.setText(text_age)

            return self.age
        except:
            pass

    def brightness_def(self):
        self.array = self.bright_class.array_gray(self.gray)
        self.bright_if = self.bright_class.brightness(self.array)
        self.screen_change = self.bright_class.change_screen(self.bright_if)

        text_bright = "Screen change: {} Brightness: {}".format(
            self.bright_if, self.array)
        self.label_brightness.show()

        self.label_brightness.setText(text_bright)

    def start_wabcam_widget(self):
        self.button_start.hide()
        self.widget.show()
        self.widget_2.show()
        self.start()


    def start(self):

        vs = WebcamVideoStream().start()

        while True:
            self.frame = vs.read() #<--frame loop

            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY) #<--gray

            self.eye_point = self.extend_eye_point.extend(
                self.gray)#<--extend_eye

            try:
                self.center_right_x = self.eye_point["center_right_x"]
                self.center_right_y = self.eye_point["center_right_y"]
                self.center_left_x = self.eye_point["center_left_x"]
                self.center_left_y = self.eye_point["center_left_y"]
                self.point_center_x = self.eye_point["point_center_x"]
                self.point_center_y = self.eye_point["point_center_y"]
                self.rightEye = self.eye_point["rightEye"]
                self.leftEye = self.eye_point["leftEye"]

            except:
                pass

            try:
                self.xywh = self.extend_faceHaar.extend_face(self.gray)
                self.face_window = self.extend_faceHaar.window_face(
                    self.xywh, self.frame) #<-- extend face window

            except:
                pass

            if self.call_time == True:
                self.time_def()
            else:
                self.label_time.hide()

            if self.call_blink == True:
                self.blink_def()
            else:
                self.label_blink.hide()

            if self.call_angle == True:
                self.angle_def()
            else:
                self.label_angle.hide()

            if self.call_distance == True:
                self.distance_def()
            else:
                self.label_distance.hide()

            if self.call_sex == True:
                self.sex_def()
            else:
                self.label_sex.hide()

            if self.call_age == True:
                self.age_def()
            else:
                self.label_age.hide()

            if self.call_bright == True:
                self.brightness_def()
            else:
                self.label_brightness.hide()

            cv2.imshow('webcam', self.frame) #<--show image
            cv2.waitKey(1)

            if cv2.getWindowProperty('webcam', 1) == -1:
                break

        vs.stop()
        cv2.destroyAllWindows()



class WebcamVideoStream :
    def __init__(self, src = 0, width = 640, height = 480) :
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self) :
        if self.started :
            print ("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wmain()
    window.show()
    sys.exit(app.exec_())
