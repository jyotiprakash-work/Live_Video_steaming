import cv2
import imutils
import numpy as np
import time

ds_factor=0.6

#net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #time.sleep(2.0)
        frame = image
        frame = imutils.resize(frame, width=400)
        (h, w) = frame.shape[:2]
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

