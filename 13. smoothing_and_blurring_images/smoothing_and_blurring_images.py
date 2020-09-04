# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

# img = cv2.imread('Halftone_Gaussian_Blur.jpg')
# img = cv2.imread('Noise_salt_and_pepper.png')
img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Homogeneous Filter
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

# Low Pass Filter
blur = cv2.blur(img, (5, 5))

# Gaussian Filter
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# Median Filter for Salt and Pepper Noise (Kernel Size must be odd (except 1))
# Kernel Size 1 returns the original image
mblur = cv2.medianBlur(img, 5)

# Bilateral Filter
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Image', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gblur, mblur, bilateralfilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
