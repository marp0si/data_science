import numpy as np
import cv2
import imageio
'''
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascade+'./haarcascade_frontalface_default.xml')

def detect(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.regtangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    return
0
mimage=imageio.imread("face.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=detect(frame=image)
imageio.imwrite("output.jpg",image)
'''
import sys

#Haar cascade classifier yukle
face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


img = cv2.imread("face.jpg") #dosyayi oku
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #siyah-beyaz yap

#yuzleri bul
faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize = (130,130))

#yuzleri isaretle
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #gozleri bul

cv2.imshow('img',img) #ekranda
cv2.imwrite("output_detected.jpg", img) #kaydet
cv2.waitKey(0) #tusa basinca cik
cv2.destroyAllWindows()