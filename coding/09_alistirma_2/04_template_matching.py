import cv2

# aynı resimde kesit var mı ?

path1 = "coding/09_alistirma_2/media/starwars.jpg"
path2 = "coding/09_alistirma_2/media/starwars2.jpg"

img = cv2.imread(path1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(path2, 0) # 0 girersem gri gösterir

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

cv2.imshow("Result", result)

cv2.waitKey(0)

# tamamlanmadı