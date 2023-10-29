# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:11:17 2023

@author: PC
"""
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:# kare çıktısını etkinler
            #ReSize
        frame = cv2.resize(frame, None, fx=1 / 3, fy=1 / 3, interpolation=cv2.INTER_AREA)
        cv2.imshow('Frame', frame)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

            
    
        break
