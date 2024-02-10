import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((500,500), np.uint8)
img = cv2.imread("coding/05_temel_islemler.py/images/helikopter.png")
b,g,r = cv2.split(img)

cv2.rectangle(img, (0, 60), (200,150), (255,255,255), -1)
cv2.rectangle(img, (200,150), (350,200), (255,255,255), -1)

cv2.imshow("img", img)

plt.hist(img.ravel(), 256, [0,256]) # histogram
plt.hist(b.ravel(), 256, [0,256]) # b histogram
plt.hist(g.ravel(), 256, [0,256]) # g histogram
plt.hist(r.ravel(), 256, [0,256]) # r histogram
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()