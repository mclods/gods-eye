# Importing Libraries
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        cv2.imshow('frame', frame)
        cv2.imshow('fg mask frame', fgmask)
        if cv2.waitKey(30) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
