# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('j.png', 0)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=3)
erosion = cv2.erode(img, kernel, iterations=3)

# Opening is Erosion followed by Dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing is Dilation followed by Erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient is the difference between dilation and erosion of an image
morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Top Hat is the difference between image and the opening of the image
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

titles = ['Original', 'Dilation', 'Erosion', 'Opening', 'Closing', 'Morph_Gradient', 'Top_Hat']
images = [img, dilation, erosion, opening, closing, morph_gradient, top_hat]

for i in range(7):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
