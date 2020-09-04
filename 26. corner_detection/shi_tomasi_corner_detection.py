# Importing Libraries
import numpy as np
import cv2

img = cv2.imread('pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert the corners to int64 format
corners = np.int64(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
