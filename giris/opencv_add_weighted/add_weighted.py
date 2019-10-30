import cv2
import numpy as np

img1 = cv2.imread('resim1.jpg')
img2 = cv2.imread('resim2.jpg')
toplam = cv2.addweighted(resim1,0.2,resim2,0,8,0)
#Ağırlıklı toplam 4 addweighted 5 parametre alır toplanacak iki resim ve birinci resmin ağırlığı(Alfa), ikinci resmin ağırlığı(Beta) ve gama değeri

cv2.imshow('Ağırlıklı toplam resim',toplam)


cv2.waitKey(0)

cv2.destroyAllWindows()
