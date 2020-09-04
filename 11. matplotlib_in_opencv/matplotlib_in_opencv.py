# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('lena.jpg', 1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Matplotlib works with RGB images so we convert OpenCV image from BGR to RGB
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
