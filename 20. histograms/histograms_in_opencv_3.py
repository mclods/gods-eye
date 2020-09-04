# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('lena.jpg', 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

cv2.imshow('img', img)

plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
