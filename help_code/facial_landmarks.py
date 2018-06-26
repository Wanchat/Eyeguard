from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
import numpy as np


def face_landmakes():

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r'C:\Users\Wanch\Google Drive\Thesis\code\help_code\shape_predictor_68_face_landmarks.dat')

    # # indexes facial landmarks
    # (l_Start, l_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    # (r_Start, r_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in  rects:

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)



            for (x,y) in shape:
                cv2.circle(frame,( x, y), 1, (0, 0, 255), -1)

        cv2.imshow("Frame", frame)
        # if cv2.waitKey(1) and stop == "q":
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    face_landmakes()