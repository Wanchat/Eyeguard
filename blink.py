from scipy.spatial import distance as dist
import numpy as np
import cv2
import dlib
from imutils import face_utils

class Blink:
    def __init__(self):
        self.Blink_counter_frame = 0
        self.Blink_total = 0
        self.ear_avg = 0


#EAR function
    def eye_aspect_ratio(self, eye):
        self.p2_p6 = dist.euclidean(eye[1], eye[5])
        self.p3_p5 = dist.euclidean(eye[2], eye[4])
        self.p1_p4 = dist.euclidean(eye[0], eye[3])
        self.ear = (self.p2_p6 + self.p3_p5) / (2.0 * self.p1_p4)
        return self.ear

#EAR Avg
    def earAvg(self, leftEye, rightEye, Blink_less = 0.25, Blink_frame = 3):
        self.ear_left = self.eye_aspect_ratio(leftEye)
        self.ear_right = self.eye_aspect_ratio(rightEye)
        self.ear_avg = (self.ear_left + self.ear_right) / 2.0

        if self.ear_avg < Blink_less:
            self.Blink_counter_frame += 1

        else:
            if self.Blink_counter_frame >= Blink_frame:
                self.Blink_total += 1
            self.Blink_counter_frame = 0

        return self.Blink_total, self.ear_avg, self.Blink_counter_frame

if __name__ == '__main__':

    blink_class = BLink()
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        r"D:\code_python\Eyeguard\data\shape_predictor_68_face_landmarks.dat")
    # indexes facial landmarks
    (l_Start, l_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (r_Start, r_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    cap = cv2.VideoCapture(1)

    while True:
        success, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in rects:
            # detect & convert np
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # extend for def eye aspect ratio
            leftEye = shape[l_Start:l_End]
            rightEye = shape[r_Start:r_End]

            blinks = blink_class.earAvg(leftEye,rightEye)

            print("Blink:{} EAR:{}".format(blinks[0],blinks[1]))

            # draw
            for (x, y) in (rightEye):
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            for (x, y) in (leftEye):
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            cv2.putText(frame, "Blinks: {}".format(blinks[0]), (190, 460),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

            cv2.putText(frame, "EAR: {:.2f}".format(blinks[1]), (310, 460),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()