import cv2


def resizeWithAspectRatio(img, width=None,  height=None, inter=cv2.INTER_AREA):
    dimention = None  # boyut
    (h, w) = img.shape[:2]

    if width is None and height is None:
        return img

    if width is None:
        r = height / float(h)
        dimention = (int(w*r), height)

    else:
        r = width/float(w)
        dimention = (width, int(h*r))

    return cv2.resize(img, dimention, interpolation=inter)


img = cv2.imread("resim.jpg")
img1 = resizeWithAspectRatio(img, width=None, height=600, inter=cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
