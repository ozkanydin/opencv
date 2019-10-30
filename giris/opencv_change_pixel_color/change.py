import cv2
import numpy as np

img = cv2.imread('deneme.jpg', 0)

for i in range(200):
    img[50,i] = [255,255,255]

cv2.imshow('Deneme Resim',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
