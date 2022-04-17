import numpy as np
import cv2
#img=cv2.imread("resim yolu",bayraklar)0=gri 
img=cv2.imread("thumb-1920-1183122.jpg",0)
#cv2.imshow("pencere adı",cv2_nesnesi)
cv2.imshow("image",img)
cv2.waitKey(0)#klavyeden tuşa basılmasını bekler
cv2.destroyAllWindows()
#cv2.imwrite("dosya yolu", cv2_nesnesi)
cv2.imwrite("thumb-1920-1183122.jpg", img)

