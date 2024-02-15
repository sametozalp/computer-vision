import cv2
import numpy as np

img1 = cv2.imread("coding/07_hough_transform/media/coins.jpg")
img2 = cv2.imread("coding/07_hough_transform/media/balls.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1_blue = cv2.medianBlur(gray1, 5)
img2_blue = cv2.medianBlur(gray2, 5)

circles = cv2.HoughCircles(img1_blue, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/4, param1=200, param2=10, minRadius=15, maxRadius= 80) # param1 = gradient, param2 = threshold değeri.
# img1.shape[0]/64 çemberler arasındaki minimum mesafe
# radius = çap

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0,255,0), 2)
        
cv2.imshow("img", img1)
cv2.waitKey(0)