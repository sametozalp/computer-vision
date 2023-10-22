import cv2

cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
img = cv2.imread("resim.jpg")
img = cv2.resize(img, (640, 480))

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()