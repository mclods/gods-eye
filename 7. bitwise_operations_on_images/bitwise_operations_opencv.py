# Importing Libraries
import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = cv2.imread('chessboard.png')
img2 = cv2.resize(img2, (500, 250))

# bit_and = cv2.bitwise_and(img1, img2)
# bit_or = cv2.bitwise_or(img1, img2)
# bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
# cv2.imshow('bit_and', bit_and)
# cv2.imshow('bit_or', bit_or)
# cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_not', bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
