# Importing Libraries
import numpy as np
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
        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=6)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0)
    return img


def process(img):
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
    canny_img = cv2.Canny(gray_masked_img, 100, 120)

    masked_img = region_of_interest(canny_img, np.array([roi_vertices], np.int32))

    # Probabilistic Hough Line Transform
    lines = cv2.HoughLinesP(masked_img,
                            rho=2,
                            theta=np.pi/60,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)

    final_img = draw_lines(img, lines)
    return final_img


cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        frame = process(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
