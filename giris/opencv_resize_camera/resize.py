import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

def ayar(kare,yuzde=75):
    genislik= int(kare.shape[1]* yuzde/100)
    yukseklik = int(kare.shape[0]*yuzde/100)
    boyut = (genislik,yukseklik)
    return cv2.resize(kare,boyut,interpolation= cv2.INTER_AREA)


while True:
    ret,kare1 = kamera.read()

    kare2 = ayar(kare1,20)

    cv2.imshow('goruntu',kare1)
    cv2.imshow('boyutlandırılmış goruntu',kare2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
