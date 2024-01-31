# ROI: region of interest -- ilgi alanı
# mesela yüzleri bulmak

import cv2

img = cv2.imread("coding/03_core_operations/test_images/basketball.jpg")

roi = img[100:200, 0:50]
img[300:400, 300:350] = roi

cv2.imshow("Basketball", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()