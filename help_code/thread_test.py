import threading
from queue import Queue
import time

q = Queue()
q_2 = Queue()

class listener(object):

    def __init__(self):

        thread = threading.Thread(target=self.loop)
        thread_2 = threading.Thread(target=self.loop_2)
        # thread.daemon = True
        thread.start()
        thread_2.start()

    def loop(self):

        for i in range(13):
            q.put(i)

    def loop_2(self):
        start = time.time()

        x = 0
        while True:
            for x in range(10):
                a = time.time() - start
                # a = '{:.2f}'.format(time.time())
                q_2.put(a)
            if x == 5:
                break

class ui(object):

    def __init__(self):
        listener()
        # while True:
        #     item = q.get()
        #     print (item)
        #     if item == 10:
        #         break
        while True:
            item = q.get()
            item_2 = q_2.get()
            print (item,item_2)
            if item == 13:
                break

ui()