import cv2
import numpy as np

resim = np.zeros((400,400,3),dtype='uint8')
resim.fill(255)
#fill ile tek değer ile resim o renk olur
cv2.line(resim,(0,0),(200,200),(0,255,0),1)
#cv2.line() ile çizgi çekilebilir, 5 parametre alır. Çizgi çizilecek resim , pt1 ,pt2 ,bgr ve kalınlık
cv2.circle(resim,(200,200),50,(255,0,0),2)
#cv2.circle() ile resme daire çizilir 5 parametre alır koordinatı yarı çapı, bgr ve kalınlık
cv2.putText(resim,'Hello World',(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
#cv2.putText() ile resme yazı yazılır. 7 parametre alır yazı yazılacak resim, yazı,koordinatı,fontstyle,çizgi kalınlığı,bgr ve kalınlık
cv2.imshow('Resim',resim)

cv2.waitKey(0)

cv2.destroyAllWindows()
