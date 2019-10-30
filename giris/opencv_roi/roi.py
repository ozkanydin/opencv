import cv2
import numpy as np

img = cv2.imread('deneme.jpg')

img2 = cv2.imread('birlesecekresim.jpg')

img2_gri = cv2.cvtColor(img2,cv2.COLOR_BG2_GRAY')

yukseklik,genislik,kanal = img2.shape
#eklenecek resmin yukseklik ve genişliğin belirledik

ROI = img[0:yukseklik,0:genislik]
#img2 boyutlarına göre yeni bir resim oluşturduk

ret,mask = cv2.threshold(img2,10,255,cv2.THRES_BINARY)
#threshold() ile gri yapılan resim de bit değeri 10 üzerinde olanları 255 yapıyoruz // farklı renkte olan kısım beyaz olur
mask_inver = cv2.bitwise_not(mask)
#bitwise_not() ile bit değerlerinin yerini değiştirdik siyah olanları beyaz beyaz olanları siyah yaptık

birlesecek_resim_arka = cv2.bitwise_and(ROI,ROI,mask = mask_inver)
#bitwise_and() ile siyah kısımları birleştireceğimiz resim ile and liyoruz. Sonucta 8bit i de 1 olan siyah ve bit değerleri farklı olan birleşmeye tabi tutulan resim and lenince 8bit i de 1 olan siyah arka plan etkisiz kalarak arka plandaki görüntüyü alır
cv2.imshow('Birleşecek resmin boyutlarındaki birleşme',birlesecek_resim_arka)

toplam = cv2.add(birlesecek_resim_arka,img2)
#birleştirmek istediğimiz resimdeki arka plan siyahı resmin arka planı yaptık kalan beyaz kısmı da resmin gerçek renklerine döndürmek için cv2.add() ile iki resmi topladık

cv2.imshow('toplam',toplam)

img[0:yukseklik,0:genislik] = toplam
#artık resimleri birleştirdik, birleşecek olan 2.resimdeki boyutları büyük resimdeki yerine toplam resmi ile koyduk

cv2.imshow('Birleşmiş Resim',img)







cv2.waitKey(0)

cv2.destroyAllWindows()
