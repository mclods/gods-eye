# Importing Libraries
import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ', ' + str(y)
        print(strxy)
        cv2.putText(img, strxy, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        print(strbgr)
        cv2.putText(img, strbgr, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)

img = cv2.imread('lena.jpg', 1)

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

