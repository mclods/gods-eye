# Importing Libraries
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened() and ret is True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # For drawing Rectangles
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # Reduce some noise
        if cv2.contourArea(contour) < 800:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('feed', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    # Press esc to quit
    if cv2.waitKey(40) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
