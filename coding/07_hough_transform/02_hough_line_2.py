import cv2
import numpy as np

vid = cv2.VideoCapture("C:/Users/Samet/Desktop/line.mp4")


while True:
    ret, frame = vid.read()
    frame =  cv2.resize(frame, (1920,1080))
    if ret == False:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hsv range for... (blue) // renk aralıklarını bulmak için googleda arat
    lower_yellow = np.array([18,94,140], np.uint8)
    upper_yellow = np.array([48,255,255], np.uint8)
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow) # sarı rerngi ayır
    
    edges = cv2.Canny(mask, 75,250) # sarı çizgilerin ortasını boşaltıyor kenarlarını çiziyor.
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 5)
    
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    
vid.release()
cv2.destroyAllWindows()