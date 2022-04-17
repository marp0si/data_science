import numpy as np
import cv2
'''
#img=cv2.imread("resim yolu",bayraklar)0=gri 
img=cv2.imread("thumb-1920-1183122.jpg",1)
#cv2.imwrite("dosya yolu", cv2_nesnesi)
cv2.imwrite("thumb-1920-1183122/gri.jpg", img)
#cv2.imshow("pencere adı",cv2_nesnesi)
cv2.imshow("image",img)



cv2.waitKey(0)#klavyeden tuşa basılmasını bekler
cv2.destroyAllWindows()
'''
'''
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("kamera açılamıyor")
while True:
    ret,frame=cap.read()
    if not ret:
        print("kareler yakalanmıyor")
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
'''
