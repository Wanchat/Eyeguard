import time
import numpy as np
import os

import threading
from queue import Queue

q = Queue()


class Timewacth:
    def __init__(self):

        self.thread = threading.Thread(target=self.timewacth)

        self.day = 0
        self.hour = 0
        self.minutes = 0
        self.second = 0

    def timewacth(self,face_start):

        while True:
            self.second = time.time() - face_start

            if self.second > 60:
                self.second = 0
                self.minutes += 1

                face_start = time.time()

            if self.minutes > 60:
                self.minutes = 0
                self.hour += 1

            if self.hour > 24:
                self.hour = 0
                self.day += 1


            print("{}: {}: {:.2f}".format(
                self.hour,
                self.minutes,
                self.second))





if __name__ == '__main__':

    t =Timewacth()
    t.timewacth(time.time())


