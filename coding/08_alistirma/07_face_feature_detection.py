import cv2
import numpy as np
import math

# yüz özelliklerini kullanma // yüzü kare içerisine almak

def findMaxCountour(contours):
    max_i = 0
    max_area = 0
    
    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])
        if max_area < area_face:
            max_area = area_face
            max_i = i
            
        try:
            c = contours[max_i]
        except:
            contours[0]
            c = contours[0]
        return c

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    roi = frame[50:250, 250:450] # frame[y1:y2, x1:x2]
    cv2.rectangle(frame, (250,50), (450,250), (0,0,255), 0)
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79], dtype= np.uint8)
    upper_color = np.array([17,255,255], dtype= np.uint8)
        
    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations= 1) # karıncalanmalar azalır
    mask = cv2.medianBlur(mask, 15)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:

            c = findMaxCountour(contours)
            ext_left = tuple(c[c[:,:,0].argmin()][0])
            ext_right = tuple(c[c[:,:,0].argmax()][0])
            ext_top = tuple(c[c[:,:,1].argmin()][0])
            ext_bottom = tuple(c[c[:,:,1].argmax()][0])
            
            cv2.circle(roi, ext_left, 5, (0,255,0),2)
            cv2.circle(roi, ext_right, 5, (0,255,0),2)
            cv2.circle(roi, ext_top, 5, (0,255,0),2)
            cv2.circle(roi, ext_bottom, 5, (0,255,0),2)
            
            cv2.line(roi, ext_left, ext_top, (255,0,0), 2)
            cv2.line(roi, ext_top, ext_right, (255,0,0), 2)
            cv2.line(roi, ext_right, ext_bottom, (255,0,0), 2)
            cv2.line(roi, ext_bottom, ext_left, (255,0,0), 2)
            
            a = math.sqrt((ext_right[0] - ext_top[0])**2+(ext_right[1]-ext_top[1])**2)
            b = math.sqrt((ext_bottom[0] - ext_right[0])**2+(ext_bottom[1]-ext_top[1])**2)
            a = math.sqrt((ext_bottom[0] - ext_top[0])**2+(ext_bottom[1]-ext_top[1])**2)
            
            try:
                angle = math.acos((a**2+b**2-c**2)/(2*b*c))*57
                cv2.putText(roi, str(angle), (ext_right[0]-10, ext_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            except:
                cv2.putText(roi, "?", (ext_right[0]-10, ext_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("roi", roi) # krıpılmış kısmı ayrı bir pencerede gösterir
    cv2.waitKey(1)
    
cap.release()