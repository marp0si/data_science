# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:47:55 2023

@author: sino
"""
import cv2

import cv2
import numpy as np
kamera=cv2.VideoCapture(0) # 0 numaralı kayıtlı kamerayı alma
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #­ Kamera Boyutlandırma
#kamera=cv2.VideoCapture('smile.mp4') bir videoyu oynatmak için bu şekilde de kullanılabilir.
while True:
    ret,goruntu=kamera.read() # kamera okumayı başlatma
    cizgili = np.copy(goruntu)
    griGoruntu = cv2.cvtColor(cizgili, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Gri Goruntu',griGoruntu) # görüntüyü gösterme
    bulurlu = cv2.GaussianBlur(griGoruntu, (7,7), 0)
    cv2.imshow('Bulurlu',bulurlu) # görüntüyü gösterme
    canny = cv2.Canny(bulurlu, 50,100)
    cv2.imshow('Canny',canny) # görüntüyü gösterme
    cv2.imshow('Normal Goruntu',goruntu) # görüntüyü gösterme
    if cv2.waitKey(25) & 0xFF ==ord('t'): # t tuşuna basılınca durdur.
        break
kamera.release() # kamerayı serbest bırak.
cv2.destroyAllWindows() # açılan pencereleri kapat.<code></code>
 
            
