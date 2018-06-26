
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
from canculator_angle import Pixel_to_Angle
import math
import numpy as np
import cv2


cap = cv2.VideoCapture(0)


def image_frame():

    while True:
        success, frame = cap.read()

        

        cv2.imshow("Frame", frame)
        cv2.waitkey(1)

        # return frame



if __name__ == '__main__':
    image_frame()
    # print(estimate()) 
  

    cap.release()
    cv2.destroyAllWindows()