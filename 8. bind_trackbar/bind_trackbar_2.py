# Importing Libraries
import numpy as np
import cv2


def nothing(x):
    print(x)


cv2.namedWindow('image')

cv2.createTrackbar('pos', 'image', 10, 100, nothing)

switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    img = cv2.imread('lena.jpg')

    pos = cv2.getTrackbarPos('pos', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 5)

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
