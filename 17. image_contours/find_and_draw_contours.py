# Importing Libraries
import numpy as np
import cv2

img = cv2.imread('thankyou.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

"""
    contours is a python list of all the contours in the image.
    Each individual contour is a numpy array of (x, y) coordinates of
    boundary points of the object.
"""
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print('No. of contours = ' + str(len(contours)))

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('image', img)
cv2.imshow('image_gray', img_gray)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
