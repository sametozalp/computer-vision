import cv2
import numpy as np

img = cv2.imread("coding/03_core_operations/test_images/opencv-logo.png")

(B, G, R) = cv2.split(img)  # renkleri böldü

black = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([black, black, R]))

cv2.waitKey(0)
cv2.destroyAllWindows()
