import cv2
import numpy as np
from extend_face_haar import Extend_face_haar
import time


class Time_detect:

    def __init__(self):

        self.day = 0
        self.hour = 0
        self.minutes = 0
        self.second = 0
        self.hour_not_face = 0
        self.minutes_not_face = 0
        self.second_not_face = 0

        self.start = time.time()
        self.start_not_face = time.time()

        self.alert_time_1 = False
        self.alert_time_2 = False
        self.alert_time_3 = False
        self.alert_time_4 = False

        self.time_reset = 5


    def time_detection(self, xywh):

        if xywh!= None:

            self.second = time.time() - self.start

            if self.second >= 60:
                self.minutes += 1
                self.second = 0

                self.start = time.time()

            if self.minutes >= 60:
                self.hour += 1
                self.minutes = 0

            if self.hour >= 24:
                self.day += 1
                self.hour = 0

            self.start_not_face = time.time()

        else:
            self.second_not_face =  time.time() -  self.start_not_face

            if self.second_not_face >= 60:
                self.minutes_not_face += 1
                self.second_not_face = 0

                self.start_not_face = time.time()

            if self.minutes_not_face >= 60:
                self.hour_not_face += 1
                self.minutes_not_face = 0

            if self.hour_not_face >= 24:
                self.day_not_face += 1
                self.hour_not_face = 0

        if self.second_not_face > self.time_reset:
            self.start = time.time()

        print('{}: {}: {:.2f} >> {}: {}: {:.2f}'.format(
            self.hour,
            self.minutes,
            self.second,
            self.hour_not_face,
            self.minutes_not_face,
            self.second_not_face))

    def alert_minutes(self):

        if 200 <= self.minutes * 10 + self.second < 230:
            self.alert_time_1 = True

        elif 400 <= self.minutes * 10 + self.second < 430:
            self.alert_time_2 = True

        elif 590 <= self.minutes * 10 + self.second < 620:
            self.alert_time_3 = True

        else:
            pass

        return {'alert_1':self.alert_time_1,
                'alert_2':self.alert_time_2,
                'alert_3':self.alert_time_3,
                }

    def alert_hour(self):

        if 200 <= self.hour * 100 + self.minutes < 215:
            self.alert_time_4 = True
        elif 400 <= self.hour * 100 + self.minutes < 415:
            self.alert_time_4 = True
        elif 800 <= self.hour * 100 + self.minutes < 815:
            self.alert_time_4 = True
        elif 1000 <= self.hour * 100 + self.minutes < 1015:
            self.alert_time_4 = True
        elif 1200 <= self.hour * 100 + self.minutes < 1215:
            self.alert_time_4 = True
        elif 1400 <= self.hour * 100 + self.minutes < 1415:
            self.alert_time_4 = True
        elif 1600 <= self.hour * 100 + self.minutes < 1615:
            self.alert_time_4 = True
        elif 1800 <= self.hour * 100 + self.minutes < 1815:
            self.alert_time_4 = True
        elif 2000 <= self.hour * 100 + self.minutes < 2015:
            self.alert_time_4 = True
        elif 2200 <= self.hour * 100 + self.minutes < 2215:
            self.alert_time_4 = True
        elif 2344 <= self.hour * 100 + self.minutes < 2359:
            self.alert_time_4 = True
        else:
            pass

        return {'alert_4':self.alert_4}


if __name__ == '__main__':

    cap = cv2.VideoCapture(1)

    start = time.time()

    day = 0
    hour = 0
    minutes = 0
    second = 0

    ex = Extend_face_haar()

    t =  Time_detect()

    while True:

        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        xywh = ex.extend_face(gray)

        time_1 = t.time_detection(xywh)
        time_2 = t.alert_minutes()
        # time_3 = t.alert_hour()

        print(time_2)

        cv2.imshow("frame", frame)
        cv2.waitKey(1)

        if cv2.getWindowProperty('frame', 1) == -1:
            break

    cap.release()
    cv2.destroyAllWindows()



