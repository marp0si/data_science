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
'''
#cv2.resize("girdi",çıktı_boyutu[,çıktı[,yatay_boyutlandırma[,dikey_boyutlandırma[,interpolasyon]]]])
src=cv2.imread("thumb-1920-1183122.jpg",1)
genişlik=src.shape[1]
yükseklik=src.shape[0]
dimension=(int(genişlik/2),int(yükseklik/2))

dst=cv2.resize(src,dimension)
cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
#cv2.warpAffine(girdi_resmi,m(matrixler),çıktı_boyut[,çıktı[,bayraklar[,çerçeve_modu[,çerçevedeğeri]]]])
src=cv2.imread("thumb-1920-1183122.jpg",1)
gen,yük,kanal=src.shape
merkez=(yük//2,gen//2)
M=cv2.getRotationMatrix2D(merkez, -45, 1.0)
cıktı=cv2.warpAffine(src,M,(gen,yük))
cv2.imshow("girdi",src)
cv2.imshow("çıktı",cıktı)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
#cv2.gaussianblur(src,KSize,sigmaX)
src=cv2.imread("thumb-1920-1183122.jpg",1)
src=cv2.resize(src,(800,600))
blured=cv2.GaussianBlur(src,(15,15),0)
cv2.imshow("src",src)
cv2.imshow("blured",blured)
cv2.waitKey()
cv2.destroyAllWindows()
'''
