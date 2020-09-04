# Importing Libraries
import numpy as np
import cv2

img = cv2.imread('lena.jpg')

# Gaussian Pyramids
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

# Laplacian Pyramids
layer = gp[5]
cv2.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    layer = cv2.subtract(gp[i-1], gaussian_extended)
    lp.append(layer)
    cv2.imshow(str(i), layer)

# Original Image
cv2.imshow('original', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
