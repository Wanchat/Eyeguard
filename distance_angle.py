from math_eyeguarde import Math_eyeguarde
import math
from canculator_angle import Pixel_to_Angle
from extend_eye import Extand_eyes
import cv2

import sys
from PyQt5.QtWidgets import QApplication, QWidget

import threading
from queue import Queue

q = Queue()
q_2 = Queue()

class Angle:
    def __init__(self):

        self.angle_prediction = Pixel_to_Angle()

# cale angle camera
    def estimate_angle(self, point_center_y):

        self.point = self.angle_prediction.px_plus(point_center_y)
        self.estimate_angle_new = self.angle_prediction.px_to_degree(self.point)

        return self.estimate_angle_new

    def alert_angle(self, angle):

        if 8 < angle <= 12:
            return True
        else:
            return False

class Distance():

    def __init__(self):
        self.math_eye = Math_eyeguarde()

# estimate_distance
    def estimate_distance(self, estimate_angle,
                            point_center_x,
                            point_center_y,
                            center_right_x,
                            est=2.6):
        # calc angle B
        self.angle_B = math.atan2(abs(point_center_x - center_right_x),
                                  abs(point_center_y - 240))*180/math.pi
        # cale line Ad cm
        self.line_AD = self.math_eye.tanRounded(abs(90 - self.angle_B))*est
        # cale distance
        self.estimate_distance_new = self.math_eye.tanRounded(
                                        abs(90 - estimate_angle))*self.line_AD

        return self.estimate_distance_new

    def alert_distance(self, distance):

        if 50 < distance <= 80:
            return True
        else:
            return False


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

    extand_eyes_class = Extand_eyes()
    angle_class = Angle()
    distance_class = Distance()

    cap = cv2.VideoCapture(0)

    def play():
        frame_False = 0

        while True:
            success, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image = extand_eyes_class.extend(gray)

            try:
                point_center_x = image["point_center_x"]
                point_center_y = image["point_center_y"]
                center_right_x = image["center_right_x"]

                angle = angle_class.estimate_angle(point_center_y)
                distance = distance_class.estimate_distance(angle,
                                                        point_center_x,
                                                        point_center_y,
                                                        center_right_x)

                d = distance_class.alert_distance(distance)

                print("distance:{:.2f} angle:{:.2f} {}".format(distance, angle, d))

                # q.put(d)



            except:
                pass

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    play()


    # thread = threading.Thread(target=play())
    # thread.start()

    # while True:
    #     item = q.get()
    #     ex = App()
    #     print(item)

        # if item == False:
        #
        #     ex.show()
        #     sys.exit(app.exec_())

