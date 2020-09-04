# Importing Libraries
import numpy as np
import cv2


def nothing(x):
    pass


cv2.namedWindow('Tracking')

cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)

cv2.createTrackbar('UH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 0, 255, nothing)

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH', 'Tracking')
    ls = cv2.getTrackbarPos('LS', 'Tracking')
    lv = cv2.getTrackbarPos('LV', 'Tracking')

    uh = cv2.getTrackbarPos('UH', 'Tracking')
    us = cv2.getTrackbarPos('US', 'Tracking')
    uv = cv2.getTrackbarPos('UV', 'Tracking')

    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
