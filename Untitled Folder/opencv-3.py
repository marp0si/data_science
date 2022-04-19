import numpy as np
import cv2
import imageio

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascade+'./haarcascade_frontalface_default.xml')

def detect(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.regtangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    return

image=imageio.imread("face.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=detect(frame=image)
imageio.imwrite("output.jpg",image)