# Importing Libraries
import numpy as np
import cv2

img = cv2.imread('messi.jpg', 1)
img2 = cv2.imread('ronaldo.jpg', 1)

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[360:411, 526:580]
img[364:415, 466:520] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .6, img2, .4, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
