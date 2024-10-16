import numpy as np
import cv2
import imutils
import threading

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture('/dev/video0')  
        (self.ret, self.frame) = self.cap.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.cap.release()
        
    def fun(self):
        if self.cap.isOpened(): 
            return True
        else:
            return False
        
    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.ret, self.frame) = self.cap.read()
                           
def gen(camera):
    while True:      
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
              
