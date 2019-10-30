import cv2
import numpy as np

img = cv2.imread('deneme.jpg')

img[0:200,0:200,1] = 255
#parçasal olarak renk değiştirme , resimdeki x ve y de 0-200 pixel arasındaki green yoğunluğunu arttırdık.
cv2.imshow('Deneme Resmi',resim)

cv2.waitKey(0)

cv2.destroyAllWindows()
