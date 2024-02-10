import cv2
import numpy as np

# resmi erozyona uğratma

img = cv2.imread("coding/05_temel_islemler.py/images/helikopter.png", 0)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
opening = cv2.morphologyEx(img, 0,  kernel, iterations = 1)

cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation) # kalınlaştırma
cv2.imshow("opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()