import cv2

"""resim okuma"""
img = cv2.imread("resim.jpg") # ikinci parametre cv2.IMREAD_GRAYSCALE || 0 // resmi gri tonlarda okur
# print(img)

"""yeniden boyutlanabilirliği ayarlar"""
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

"""resmi pencerede açma"""
cv2.imshow("image", img)

cv2.imwrite("resim1.jpg", img)

"""tıklayana kadar pencereyi kapatmaz"""
cv2.waitKey(0)

"""birden fazla pencere varsa kapatma kolaylığı sağlar"""
cv2.destroyAllWindows()