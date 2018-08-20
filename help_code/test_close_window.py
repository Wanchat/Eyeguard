import cv2, numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    if cv2.getWindowProperty('frame', 1) == -1:
        break

cap.release()
cv2.destroyAllWindows()