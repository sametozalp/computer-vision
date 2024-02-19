import cv2

# arka plan çıkarma (manuel) // arabaları otobandan sıyırma

cap = cv2.VideoCapture("C:/Users/Samet/Downloads/car.mp4")
_, first_frame = cap.read()
first_frame = cv2.resize(first_frame, (640,480))
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5,5), 0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    
    if ret == False:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    diff = cv2.absdiff(first_gray, gray)
    _, diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("frame", frame)
    cv2.imshow("firstframe", first_frame)
    cv2.imshow("diff", diff)
    
    cv2.waitKey(2)
    
    
    
cap.release()
cv2.destroyAllWindows()