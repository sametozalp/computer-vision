import cv2

cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()
    
    if ret == False:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", frame)
    cv2.waitKey(30)
    
    if 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()