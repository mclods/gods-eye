# Importing Libraries
import numpy as np
import cv2


def nothing(x):
    pass


cv2.namedWindow('image')
cv2.createTrackbar('thl', 'image', 0, 255, nothing)
cv2.createTrackbar('thu', 'image', 0, 255, nothing)

while True:
    img = cv2.imread('messi.jpg', 0)

    thl = cv2.getTrackbarPos('thl', 'image')
    thu = cv2.getTrackbarPos('thu', 'image')

    canny = cv2.Canny(img, thl, thu)

    cv2.imshow('image', canny)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
