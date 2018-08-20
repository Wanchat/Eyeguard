import wmi
import cv2
import numpy as np

class Brightness:

    def array_gray(self, image):
        self.avg_gray = np.average(image)
        self.avg_gray = round(self.avg_gray)
        return self.avg_gray

    def brightness(self, image_gray):
        self.var_brightness = 100

        # max light is 255
        if 200 > self.avg_gray >= 140:
            self.var_brightness = 90
        elif 140 > self.avg_gray >= 100:
            self.var_brightness = 80
        elif 100 > self.avg_gray >= 60:
            self.var_brightness = 70
        elif 60 > self.avg_gray >= 50:
            self.var_brightness = 60
        elif 50 > self.avg_gray >= 40:
            self.var_brightness = 50
        elif 40 > self.avg_gray >= 30:
            self.var_brightness = 40
        elif 30 > self.avg_gray >= 0:
            self.var_brightness = 30
        else:
            self.var_brightness = 100
        
        return self.var_brightness

    def change_screen(self,v_brightness):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[
            0].WmiSetBrightness(v_brightness, 1)

if __name__ == '__main__':
    c = Brightness()

    cap = cv2.VideoCapture(0)   

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        array = c.array_gray(gray)
        bright_if = c.brightness(array)
        screen_change = c.change_screen(bright_if)

        print("bright: {} screeen: {}".format(bright_if, array))

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()