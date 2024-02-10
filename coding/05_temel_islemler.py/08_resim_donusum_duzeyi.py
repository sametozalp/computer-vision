import cv2
import numpy as np

img = cv2.imread("coding/05_temel_islemler.py/images/helikopter.png", 0)

row, col = img.shape

M = np.float32([[1,0,10], [0,1,70]]) # 10 soldan, 70 üstten kaydırır
dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()