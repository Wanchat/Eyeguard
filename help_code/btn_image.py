from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QDialog,\
    QCheckBox, QMainWindow, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt

class Wmain(QMainWindow):
    def __init__(self):
        super(Wmain, self).__init__()
        loadUi(r'D:\code_python\Eyeguard'
                r'\icon\eyeguade_tab_new.ui', self)

        self.button_start.clicked.connect(self.to_widget)
        # self.button_time_2.clicked.connect(self.dis)
        self.none = True


        self.none = None



    def to_widget(self):
        print("hello")
        self.none =  True
        self.start()
        return self.none
    def dis(self):
        self.none = False
        return self.none

    def start(self):
        vs = WebcamVideoStream().start()
        while True:
            frame = vs.read()

            if self.none ==True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = gray
            else:
                pass

            cv2.imshow('webcam', frame)
            cv2.waitKey(1)
            if cv2.getWindowProperty('webcam', 1) == -1:
                break
        vs.stop()
        cv2.destroyAllWindows()




class WebcamVideoStream :
    def __init__(self, src = 1, width = 640, height = 480) :
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self) :
        if self.started :
            print ("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wmain()
    window.show()
    sys.exit(app.exec_())
