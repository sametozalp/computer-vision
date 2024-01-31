import cv2

img = cv2.imread("coding/03_core_operations/test_images/opencv-logo.png")

print(img.shape) # height, width, channel
# channel 3 ise resim renklidir
# channel 1 ise resim gridir

img.size() # bu üç değerin çarpımına eşittir.
img.dtype # resmin veri tipi (uint8)
# resim sadece renliyse channel değerine erişebiliriz

cv2.imshow("OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()