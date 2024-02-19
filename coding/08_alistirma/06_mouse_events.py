import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")

circles = []

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

cv2.setMouseCallback("frame", mouse)

while 1:
    _, frame = cap.read()
    
    for center in circles:
        cv2.circle(frame, center, 20, (255,0,0), -1)
        
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    
    if key == 27: # escye bastıysa
        break
    elif key == ord("h"):
        circles = []
        
cap.release()
cv2.destroyAllWindows()