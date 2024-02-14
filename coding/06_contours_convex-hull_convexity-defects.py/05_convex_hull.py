
# sekilli anlatim: 

import cv2
import numpy as np

img = cv2.imread("coding/06_contours_convex-hull_convexity-defects.py/media/map.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3,3))

_, thresh = cv2.threshold(blur, 40,255,cv2.THRESH_BINARY) # ikinci parametre 75 değerinde iken kıtanın orta kısmındaki görselleri kaybettik, 40a çekmek durumu düzeltti.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)): # 0'dan adedine kadar
    hull.append(cv2.convexHull(contours[i], False))

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8) # background

for i in range(len(contours)): # 0'dan adedine kadar
    cv2.drawContours(bg, contours, i, (255,0,0), 3, 8, hierarchy)
    cv2.drawContours(bg, hull, i, (255,0,0), 1, 8)

cv2.imshow("image", bg)

cv2.waitKey(0)