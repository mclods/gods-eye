# Importing Libraries
import numpy as np
import cv2

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# Generate Gaussian Pyramid for Apple
apple_layer = apple.copy()
gp_apple = [apple_layer]

for i in range(6):
    apple_layer = cv2.pyrDown(apple_layer)
    gp_apple.append(apple_layer)


# Generate Gaussian Pyramid for Orange
orange_layer = orange.copy()
gp_orange = [orange_layer]

for i in range(6):
    orange_layer = cv2.pyrDown(orange_layer)
    gp_orange.append(orange_layer)


# Generate Laplacian Pyramid for Apple
apple_layer = gp_apple[5]
lp_apple = [apple_layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    apple_layer = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(apple_layer)


# Generate Laplacian Pyramid for Orange
orange_layer = gp_orange[5]
lp_orange = [orange_layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    orange_layer = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(orange_layer)


# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip (lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)


# Now Reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
