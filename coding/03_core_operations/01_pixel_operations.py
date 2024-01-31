import cv2
import numpy as np

path = "coding/03_core_operations/test_images/opencv-logo.png"
img = cv2.imread(path)
# print(img)

# px = img[10,10] // koordinatlardındaki renk değerlerini döndürür (b,g,r)
# print(px)

(b, g, r) = img[50,30]
print("(0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

#Üçüncü parametre hangi renk olduğunu temsil ediyor
blue = img[100,100,0]
green = img[100,100,1]
red = img[100,100,2]
print(blue)
print(green)
print(red)