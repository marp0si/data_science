# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:47:55 2023

@author: sino
"""
import cv2

def closeAll(): 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def video(cap):
    cap = cv2.VideoCapture(video_path)
    '''cap = cv2.VideoCapture(2)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))'''
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:# kare çıktısını etkinler
            #ReSize
            frame = cv2.resize(frame, None, fx=1 / 3, fy=1 / 3, interpolation=cv2.INTER_AREA)
            cv2.imshow('Frame', frame)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            closeAll()
            break
    pass
image_path = "dsadas.jpg"
image = cv2.imread(image_path)
video_path = "../assets/video.mp4"
cap = cv2.VideoCapture(video_path)

'''
cv2.imshow("Image", image)
#filtre
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", new_image)
'''

'''
#kayıt 
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite("dsadas_filtre.jpg", new_image)
'''

# video yakalama
video_path = "kaede-to-suzu-the-animation-episode-1.mp4"
video(video_path)

'''
#kamera yakala
video_path = "0"# veya -1
video(video_path)
'''