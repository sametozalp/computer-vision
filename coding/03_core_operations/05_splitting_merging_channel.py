import cv2

img = cv2.imread("coding/03_core_operations/test_images/opencv-logo.png")

(B, G, R) = cv2.split(img) # renkleri böldü
merged = cv2.merge([B,G,R]) # renkleri birleştirdi

cv2.imshow("OpenCV", img)
cv2.imshow("OpenCV merged", img)
cv2.imshow("OpenCV-B", B)
cv2.imshow("OpenCV-G", G)
cv2.imshow("OpenCV-R", R) # kırmızı renk yok oldu ama resim siyah beyaz
cv2.waitKey(0)
cv2.destroyAllWindows()