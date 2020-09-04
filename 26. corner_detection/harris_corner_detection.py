# Importing Libraries
import numpy as np
import cv2

img = cv2.imread('chessboard.png')
img = cv2.resize(img, (512, 512))
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# As cornerHarris() method takes the image in float32 format so we convert it
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# To get better results we dilate the image
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()

