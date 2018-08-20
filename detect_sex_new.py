import dlib
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np


class Sex:
    def __init__(self, model=r"D:\code_python\Eyguard_cnn\sex\sex_25.model"):
        self.madel_age = load_model(model)

    def estimate_sex(self, window_face):
        self.window_face = cv2.resize(window_face, (28, 28))
        self.window_face = self.window_face.astype("float") / 255.0
        self.window_face = img_to_array(self.window_face)
        self.window_face = np.expand_dims(self.window_face, axis=0)

        (self.man, self.woman) = self.madel_age.predict(self.window_face)[0]

        self.label_sex = "woman" if self.woman > self.man else "man"
        self.score_sex = self.woman if self.woman > self.man else self.man
        return self.label_sex, self.score_sex

if __name__ == '__main__':
    face_detect = cv2.CascadeClassifier(
        r"D:\code_python\data\haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(1)

    sex_class = Sex()
    while True:
        _, frame = cap.read()
        orig_frame = frame.copy()
        gray = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2GRAY)
        face = face_detect.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in face:
            cv2.rectangle(orig_frame, (x, y), (x + w, y + h), (255, 255, 255),
                          2)

            face_n = orig_frame[y:y + h, x:x + w]
            try:
                sex1 = sex_class.estimate_sex(face_n)
                print(sex1)
            except:
                pass


        cv2.imshow("Frame", orig_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()