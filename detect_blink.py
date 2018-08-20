import cv2
from extend_eye import Extand_eyes
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import imutils
import time

from popup import Pop_alert_all
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget

class Blink_cnn:

    def __init__(self, model_blink):

        self.model_blink = load_model(model_blink)
        self.window_right = None
        self.window_left = None
        self.closedeyes_right = None
        self.openeyes_right = None
        self.closedeyes_left = None
        self.openeyes_left = None
        self.label = None
        self.label_2 = None
        self.eye_predict = None

    def extend_eyes(self, image, rightEye, leftEye):

        self.image = image
        self.rightEye = rightEye
        self.leftEye = leftEye

        self.right_0_x, self.right_0_y = self.rightEye[0]
        self.right_1_x, self.right_1_y = self.rightEye[1]
        self.right_3_x, self.right_3_y = self.rightEye[3]
        self.right_4_x, self.right_4_y = self.rightEye[4]

        self.left_0_x, self.left_0_y = self.leftEye[0]
        self.left_1_x, self.left_1_y = self.leftEye[1]
        self.left_3_x, self.left_3_y = self.leftEye[3]
        self.left_4_x, self.left_4_y = self.leftEye[4]

        self.window_right = self.image[
                       self.right_1_y - 5: self.right_4_y + 5,
                       self.right_0_x - 5: self.right_3_x + 5]

        self.window_left = self.image[
                      self.left_1_y - 5: self.left_4_y + 5,
                      self.left_0_x - 5: self.left_3_x + 5]

        return  self.window_right, self.window_left

    def pre_process(self, window_eye):

        self.window_right_pre = cv2.resize(window_eye[0], (28, 28))
        self.window_right_pre = self.window_right_pre.astype("float") / 255.0
        self.window_right_pre = img_to_array(self.window_right_pre)
        self.window_right_pre = np.expand_dims(self.window_right_pre, axis=0)

        self.window_left_pre = cv2.resize(window_eye[1], (28, 28))
        self.window_left_pre = self.window_left_pre.astype("float") / 255.0
        self.window_left_pre = img_to_array(self.window_left_pre)
        self.window_left_pre = np.expand_dims(self.window_left_pre, axis=0)

        return self.window_right_pre, self.window_left_pre

    def classify_blink(self, window_pre):

        (self.closedeyes_right,self.openeyes_right) = \
            self.model_blink.predict(window_pre[0])[0]

        (self.closedeyes_left,self.openeyes_left) = \
            self.model_blink.predict(window_pre[1])[0]

        if self.openeyes_right > self.closedeyes_right:
            self.label = "openeyes_right"
            self.score = self.openeyes_right
        else:
            self.label = "closedeyes_right"
            self.score = self.closedeyes_right

        if self.openeyes_left > self.closedeyes_left:
            self.label_2 = "openeyes_left"
            self.score_2 = self.openeyes_left
        else:
            self.label_2 = "closedeyes_left"
            self.score_2 = self.closedeyes_left


        # self.label = "openeyes_right" if self.openeyes_right > \
        #                                     self.closedeyes_right \
        #                                     else "closedeyes_right"
        #
        # self.score = self.openeyes_right if self.openeyes_right > \
        #                                     self.closedeyes_right \
        #                                     else self.closedeyes_right
        #
        # self.label_2 = "openeyes_left" if self.openeyes_left > \
        #                                     self.closedeyes_left \
        #                                     else "closedeyes_left"
        #
        # self.score_2 = self.openeyes_left if self.openeyes_left > \
        #                                     self.closedeyes_left \
        #                                     else self.closedeyes_left



        if self.label == "openeyes_right" and self.label_2 == "openeyes_left":
                self.eye_predict = "openeyes"
        else:
            self.eye_predict = "closedeyes"

        return self.eye_predict

class Blinking:

    def __init__(self, blink_frame = 3):

        self.blink_frame = blink_frame
        self.blink_counter_frame = 0
        self.blink_total = 0
        self.blink_alert = False
        self.alert_count = 0

    def predict_eye_blinking(self, eye_predict, time_blinking, blink_min = 20):

        self.eye = eye_predict
        self.time_blinking = time_blinking
        self.blink_min = blink_min

        if self.eye == "closedeyes":
            self.blink_counter_frame += 1

        else:
            if self.blink_counter_frame >= self.blink_frame:
                self.blink_total += 1

            self.blink_counter_frame = 0

        if self.time_blinking[2] > 59:

            if self.blink_total < self.blink_min:
                self.blink_alert = True

        if self.time_blinking[2] > 59:
            self.blink_total = 0

        if self.blink_alert == True:
            self.alert_count += 1

        if self.alert_count > 120:
            self.blink_alert = False
            self.alert_count = 0

        return {'blink':self.blink_total,
                'frame':self.blink_counter_frame,
                'alert':self.blink_alert}

class Time_blinking:

    def __init__(self):

        self.time_start = time.time()
        self.day = 0
        self.hour = 0
        self.minutes = 0
        self.second = 0

    def time_count(self):

        self.second = time.time() - self.time_start

        if self.second >= 60:
            self.minutes += 1
            self.second = 0
            self.time_start = time.time()

        if self.minutes >= 60:
            self.hour += 1
            self.minutes = 0

        if self.hour >= 24:
            self.day += 1
            self.hour = 0

        return  self.hour, self.minutes, self.second

class Change_blink_min:

    def __init__(self, sex):
        self.sex = sex

    def change_blink_min(self):
        if self.sex == "woman":
            return 28
        else:
            return 20


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()






if __name__ == '__main__':

    app = QApplication(sys.argv)



    model_path = r"D:\code_python\Eyguard_cnn\blink\blink.model"

    time_blinking = Time_blinking()
    extend_eye_point = Extand_eyes()

    blink_cnn = Blink_cnn(model_path)

    blinking = Blinking()

    cap = cv2.VideoCapture(0)

    frame_1 = 0

    while True:

        _, frame = cap.read()



        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eye_point = extend_eye_point.extend(gray)
        time_count = time_blinking.time_count()

        try:

            rightEye = eye_point["rightEye"]
            leftEye = eye_point["leftEye"]

            blink_extend = blink_cnn.extend_eyes(frame, rightEye, leftEye)

            blink_pre = blink_cnn.pre_process(blink_extend)

            blink_classify = blink_cnn.classify_blink(blink_pre)

            blink_count = blinking.predict_eye_blinking(blink_classify,
                                                        time_count)

            print(blink_count, time_count)

            if  blink_count["alert"] == True:
                frame_1 += 1
            else:
                if frame_1 == 1:
                # app = QApplication(sys.argv)

                    ex = App()
                    ex.show()
                    sys.exit(app.exec_())

                else:
                    pass


        except:
            pass

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
