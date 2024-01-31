import cv2

cap = cv2.VideoCapture(0) # görüntüyü kameradan alır. videodan almasını istiyorsak adres gireriz.

while True:
    ret, frame = cap.read()  # iki tane değer döndürür: videoları doğru okuma durumuna göre true - false, frameler(kareler)
    frame = cv2.flip(frame, 1) # y eksenine göre simetriğini alıp gösterir

    cv2.imshow("WebCam", frame)
    cv2.waitKey(30) # her kareyi ekranda 30 milisaniye görürüz

cap.release()
cv2.destroyAllWindows()