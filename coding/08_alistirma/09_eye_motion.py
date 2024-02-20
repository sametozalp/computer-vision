import cv2

vid = cv2.VideoCapture("coding/08_alistirma/media/eye_motion.mp4")

while 1:
    ret, frame = vid.read()
    
    if ret == False:
        break
    
    roi = frame[80:210, 230:450]
    rows, cols, _ = roi.shape
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key= lambda x: cv2.contourArea(x), reverse= True) # alana göre contourları sırala , reverse = tersten sıralama
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), color= 0)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), color= 0)
        break
    
    frame[80:210, 230:450] = roi
    
    cv2.imshow("frame", frame)
    
    cv2.waitKey(50)
    
vid.release()