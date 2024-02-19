import cv2

# arka plan çıkarma // öncekinin hazır versiyonu

cap = cv2.VideoCapture("C:/Users/Samet/Downloads/car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history= 100, varThreshold= 50, detectShadows= True)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    mask = subtractor.apply(frame)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.waitKey(3)
    
cap.release()
cv2.destroyAllWindows()