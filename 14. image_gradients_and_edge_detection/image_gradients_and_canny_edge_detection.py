# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

# img = cv2.imread('messi.jpg', 0)
img = cv2.imread('sudoku.png', 0)

# Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelcombined = cv2.bitwise_or(sobelx, sobely)

# Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined', 'Canny']
images = [img, lap, sobelx, sobely, sobelcombined, canny]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
