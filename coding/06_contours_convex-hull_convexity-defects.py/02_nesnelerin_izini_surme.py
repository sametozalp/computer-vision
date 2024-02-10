import cv2
import numpy as np

cap = cv2.VideoCapture("coding/06_contours_convex-hull_convexity-defects.py/media/dog.mp4")

while True:
    _, frame = cap.read()

    if _ == False:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensivity = 15
    lower_white = np.array([0,0,255-sensivity])
    upper_white = np.array([255, sensivity, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)

    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()