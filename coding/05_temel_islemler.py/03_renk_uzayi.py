import cv2

img = cv2.imread("resim.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # renk uzaylarının birbirine dönüşümü, bgr => rgb
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("resim BGR", img)
cv2.imshow("resim1 RGB", img_rgb)
cv2.imshow("resim1 HSV", img_hsv)
cv2.imshow("resim1 GRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()