import cv2

path = "coding/09_alistirma_2/media/starwars.jpg"
img = cv2.imread(path)
blurry_image = cv2.medianBlur(img, 9)

laplacian = cv2.Laplacian(blurry_image, cv2.CV_64F).var()

if laplacian < 500:
    print("blurry image")

cv2.imshow("img", img)
cv2.imshow("blurry_image", blurry_image)

cv2.waitKey(0)
cv2.destroyAllWindows()