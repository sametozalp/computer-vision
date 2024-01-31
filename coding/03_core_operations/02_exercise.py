import cv2
import numpy as np

img = cv2.imread("coding/03_core_operations/test_images/forest.jpg")

corner = img[0:100,0:100] # [y eksenini, x eksenini] temsil eder.

img[0:100, 0:250] = (255,0,0) # resmin bir bölümünü mavi yaptı

cv2.imshow("Forest", img)
cv2.imshow("Corner", corner)
cv2.waitKey(0)
cv2.destroyAllWindows()