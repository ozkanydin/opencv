import cv2
import numpy as np

img = cv2.imread('deneme.jpg')

#resmi uzatma

resmi_uzatma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
#resmi aynalama
resmi_aynalama = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
#resmi tekrar etme
resmi_tekrar_etme = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
#resmin etrafını sarma
resmin_etrafini_sarma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT)



cv2.imshow('Deneme Resmi orijinal',resim)
cv2.imshow('Deneme Resmi uzatilan',resmi_uzatma)
cv2.imshow('Deneme Resmi aynalama',resmi_aynalama)
cv2.imshow('Deneme Resmi tekrar_etme',resmi_tekrar_etme)
cv2.imshow('Deneme Resmi etrafini_sarma',resmin_etrafini_sarma)

cv2.waitKey(0)

cv2.destroyAllWindows()
