import cv2

# resimler aynı mı ?

path = "coding/09_alistirma_2/media/aircraft.jpg"

img1 = cv2.imread(path)
img1 = cv2.resize(img1, (640, 550))

img2 = cv2.imread(path)
img2 = cv2.resize(img2, (640, 550))

img3 = cv2.imread(path)
img3 = cv2.resize(img3, (640, 550))
img3 = cv2.medianBlur(img3, 7)

# boyutlar farklıysa resimleri farklı olarak algılar

# diff = difference
diff = cv2.subtract(img1, img3) # subtract iki resimi karşılaştırıp farklı olan yerlerin rengini değiştirir // aynı yerler siyah gözükür
b,g,r = cv2.split(diff) # sayılarla kontrol
print(b)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0: # 0 olmayan değerleri sayar
    print("completely equal")
else:
    print("NOT completely equal")

cv2.imshow("diff", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()