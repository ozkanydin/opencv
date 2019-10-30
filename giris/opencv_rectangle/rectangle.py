import cv2
import numpy as np

img = cv2.imread('deneme.jpg')
cv2.rectangle(resim,(50,200),(150,20),[255,0,0])
#rectangle değer olarak aldığı iki noktayla resim de çerçeve oluşturmaya yarar.
#rectangle resim,point1,point2 ve bgr değerlerini alır point1 x de 50 y de 200 gitmiştir.
cv2.imshow('Deneme Resmi',resim)

cv2.waitKey(0)

cv2.destroyAllWindows()
