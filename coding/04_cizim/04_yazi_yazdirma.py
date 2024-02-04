import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 # tuval oluşturma / +255 siyahı beyaz yapar

cv2.putText(canvas, "OpenCV", (10,100), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), cv2.LINE_AA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()