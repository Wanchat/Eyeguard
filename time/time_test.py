import time
import numpy as np

def time_test():
    start = time.time()
    while True:
        number = int(input("input number: "))
        if number != 0:
            pass
        else:
            stop = time.time() - start
            print("{:.2f}".format(stop))
            break

class Timewacth:

    def __init__(self, face_start):
        self.face_start = face_start

    def timewacth(self):
        day = 0
        hour = 0
        minutes = 0
        second = 0

        while True:
            second = time.time() - self.face_start

            if second >= 60:
                minutes += 1
                second = 0

            if minutes >= 60:
                hour += 1
                minutes = 0

            if hour >= 24:
                day += 1
                hour = 0

            # return hour, minutes
            print("{}:{}:{:.2f}".format(hour, minutes, second))

    def minutes(self, time_min):
        return time_min / 60

    def hour(self, time_hour):
        return time_hour / 60

    def day(self, time_day):
        return time_day / 24

    def __str__(self):
        return self.timewacth()

if __name__ == '__main__':


    a = Timewacth(100)
    ab = a.timealerd(60)

