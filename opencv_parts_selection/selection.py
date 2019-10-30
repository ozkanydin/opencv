import cv2
import numpy as np

img = cv2.imread('deneme.jpg')


bolge = img[100:200,300:400]
cv2.imshow('Deneme Resmi',resim)

cv2.waitKey(0)

cv2.destroyAllWindows()
