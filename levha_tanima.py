  # -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:02:48 2020

@author: ASUS
"""
    
import cv2
import numpy as np

kamera = cv2.imread("4.jpg")
gri = cv2.imread("4.jpg",2)



while True:
    
    nesne = cv2.imread("4.jpg",0)
    w,h = nesne.shape
    res = cv2.matchTemplate(gri,nesne,cv2.TM_CCOEFF_NORMED)
    esik = 0.8
    loc = np.where(res > esik)

    for n in zip(*loc[::-1] ):
        cv2.rectangle(kamera,n,(n[0]+h,n[1]+w),(0,255,0),10)

    cv2.imshow('goruntu',kamera)

    if cv2.waitKey(25)  & 0xFF == ord("q"):
        break
cv2.waitKey(0)

cv2.destroyAllWindows()










