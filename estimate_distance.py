
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
# from angle_degree.detect_angle_lida import line_angle
# import log
# from graphic.text import text
from canculator_angle import Pixel_to_Angle
import math

angle_prediction = Pixel_to_Angle()


def estimate():

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r'C:\Users\Wanch\Google Drive\Thesis\code\angle_degree\shape_predictor_68_face_landmarks.dat')

    # indexes facial landmarks
    (left_eye_Start, left_eye_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (right_eye_Start, right_eye_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in rects:

            # detect & convert numpy
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # extend for eye aspect ratio
            leftEye = shape[left_eye_Start : left_eye_End]
            rightEye = shape[right_eye_Start : right_eye_End]

            right_x_0, right_y_0 = rightEye[0]
            right_x_3, right_y_3 = rightEye[3]

            left_x_0, left_y_0 = leftEye[0]
            left_x_3, left_y_0 = leftEye[3]

            # def  x and y eye center
            right_x = (right_x_3 - right_x_0)/2
            right_y = (right_y_3 - right_y_0)/2

            left_x = (left_x_3 - left_x_0)/2
            left_y = (left_y_0 - left_y_0)/2

            # center eyes right and left
            center_right_x = right_x_0 + right_x
            center_right_y = right_y_0 + right_y
            
            center_left_x = left_x_0 + right_x
            center_left_y = left_y_0 + right_y

            point_center_x =  (center_right_x + center_left_x)/2
            point_center_y = (center_right_y + center_left_y)/2

            # draw vector
            line_AB = cv2.line(frame,(int(point_center_x),240), (int(center_right_x), int(center_right_y)),(0,0,255),1)
            line_AC = cv2.line(frame,(int(point_center_x),240), (int(center_left_x), int(center_left_y)),(0,0,255),1)

            line_BC = cv2.line(frame, (int(center_right_x), int(center_right_y)), (int(center_left_x),int(center_left_y)), (0,0,255), 1)

            line_AD = cv2.line(frame,(int(point_center_x),240), (int(point_center_x), int(point_center_y)),(255,0,0),1)

            circle_A = cv2.circle(frame, (int(point_center_x), 240), 2, (255,255,255), -1)
            circle_B = cv2.circle(frame, (int(center_right_x), int(center_right_y)), 2, (255,255,255), -1)
            circle_C = cv2.circle(frame, (int(center_left_x), int(center_left_y)), 2, (255,255,255), -1)
            circle_D = cv2.circle(frame, (int(point_center_x), int(point_center_y)), 2, (255,255,255), -1)

            circle_E = cv2.circle(frame, (int(center_right_x), int(point_center_y)), 2, (255,255,255), -1)
            circle_F = cv2.circle(frame, (int(center_left_x), int(point_center_y)), 2, (255,255,255), -1)

            line_ED = cv2.line(frame,(int(center_right_x), int(point_center_y)), (int(point_center_x), int(point_center_y)),(0,255,0),1)
            line_FD = cv2.line(frame,(int(center_left_x), int(point_center_y)), (int(point_center_x), int(point_center_y)),(0,255,0),1)

            line_AE = cv2.line(frame, (int(point_center_x), 240),
                               (int(center_right_x), int(point_center_y)),
                               (0, 255, 0), 1)
            line_AF = cv2.line(frame, (int(point_center_x), 240),
                               (int(center_left_x), int(point_center_y)),
                               (0, 255, 0), 1)

            # calc angle
            angle_B = math.atan2(abs(point_center_x - center_right_x), abs(point_center_y - 240)) * 180/math.pi

            #  calc tan
            def tanRounded(x):
                Radiansx = math.radians(x)
                tanx = math.tan(Radiansx) 
                tanRoundedx = round(tanx,2)
                return tanRoundedx 
            
            # estimate distance
            estimate_AD_cm = tanRounded(abs(90-angle_B))*2.6

            point = angle_prediction.px_plus(point_center_y)
            estimate_angle = angle_prediction.px_to_degree(point)

            estimate_distance = tanRounded(abs(90-estimate_angle))*estimate_AD_cm
            # estimate_distance = estimate_AD_cm /  tanRounded(estimate_angle)
            up_or_down = angle_prediction.d_or_e(point_center_y)

            print("{:7.2f}{:7.2f} {}".format(estimate_distance, estimate_angle, up_or_down) )




        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    estimate()
    # print(estimate())