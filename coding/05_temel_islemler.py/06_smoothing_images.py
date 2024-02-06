import cv2

img_filter = cv2.imread("coding/05_temel_islemler.py/images/filter.png")
img_median = cv2.imread("coding/05_temel_islemler.py/images/median.png")
img_bilateral = cv2.imread("coding/05_temel_islemler.py/images/bilateral.png")

blur = cv2.blur(img_filter, (5,5)) # pozitif tek sayılar olmalı
blur2 = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

blur_m = cv2.medianBlur(img_median, 5)

cv2.imshow("original", img_median)
cv2.imshow("blur_m", blur_m)

cv2.waitKey(0)
cv2.destroyAllWindows()