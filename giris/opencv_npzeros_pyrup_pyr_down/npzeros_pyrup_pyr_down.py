import cv2
import numpy as np

img = cv2.imread('deneme.jpg')

iki_kat_buyuk = cv2.pyrup(img)
cv2.imshow('Iki kat buyuk',iki_kat_buyuk)
iki_kat_kucuk = cv2.pyrdown(img)
cv2.imshow('Iki kat kucuk',iki_kat_kucuk)

img = np.zeros((400,400,3),dtype='uint8')
#npzeros() ile 400x400 lük alanı siyah yaparız

cv2.imshow('NPzeros',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
