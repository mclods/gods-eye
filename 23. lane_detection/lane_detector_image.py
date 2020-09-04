# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2


def region_of_interest(img, roi_vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, roi_vertices, 255)
    mask = cv2.bitwise_and(img, mask)
    return mask


def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros_like(img)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0)
    return img


img = cv2.imread('road.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(img.shape)
ht = img.shape[0]
wd = img.shape[1]

# Region of Interest (Taking Region of Interest as a Triangle)
roi_vertices = [
    (0, ht),
    (wd/2, ht/2),
    (wd, ht)
]

# Grayscale Image
gray_masked_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Canny Edge Detection
canny_img = cv2.Canny(gray_masked_img, 100, 200)

masked_img = region_of_interest(canny_img, np.array([roi_vertices], np.int32))

# Probabilistic Hough Line Transform
lines = cv2.HoughLinesP(masked_img,
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

final_img = draw_lines(img, lines)

plt.imshow(final_img)
plt.show()
