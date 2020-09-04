# Importing Libraries
import numpy as np
import cv2

# img = cv2.imread('sudoku.png')
img = cv2.imread('road.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 1
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Step 2
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()