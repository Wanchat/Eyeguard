import cv2
import numpy as np
import threading
from queue import Queue

q = Queue()

# creating threading class
class AnyThread():
    def __init__ (self):
        threading.Thread.__init__(self)

    def run_cam(self):
        # in this class and function we will put our execution test function
        c = Cap()
        return c.run()



class Cap:

    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        # self.threads = []

    def run(self):
        while True:
            _, self.frame = self.cap.read()
            q.get(self.frame)

            # t = threading.Thread(target=self.worker)
            # self.threads.append(t)
            # t.start()
            self.show("frame")

    def show(self,name):
        cv2.imshow(name, self.frame)
        cv2.waitKey(1)

    def dis(self):
        self.cap.release()
        cv2.destroyAllWindows()



    # def worker(self):
    #     """thread worker function"""
    #     print (self.frame)
        # return

def test():
    a = AnyThread()
    print(a.run())



if __name__ == '__main__':
    app = Cap()
    app.run()
    app.show()
    app.dis()