import cv2

img = cv2.imread("coding/06_contours_convex-hull_convexity-defects.py/media/contour.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt) # alan bulma
perimeter = cv2.arcLength(cnt, True) # çevreyi bulma

M = cv2.moments(cnt) # map