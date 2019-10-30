import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
#0 ise bilgisayar kamerası açılır
#1 ise bilgisayara usb ile bağlanan kamera
#Video açarsak VideoCapture() içine videonun yolu yazılır.


while True:
    ret,kare = kamera.read()

    cv2.imshow('goruntu',kare)

    if cv2.waitKey(25)  & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()
