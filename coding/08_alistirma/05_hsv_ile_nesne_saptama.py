import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("coding/08_alistirma/media/hsv.mp4")

cv2.namedWindow("Trackbar")
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("LH", "Trackbar")
    ls = cv2.getTrackbarPos("LS", "Trackbar")
    lv = cv2.getTrackbarPos("LV", "Trackbar")
    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")
    uv = cv2.getTrackbarPos("UV", "Trackbar")
    
    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    bitwise = cv2.bitwise_and(frame, frame, mask= mask) # silginin asıl rengini bize gösteriyor
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", bitwise)
    
    cv2.waitKey(40)
    
cap.release()
cv2.destroyAllWindows()