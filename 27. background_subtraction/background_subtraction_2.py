# Importing Libraries
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

# This method detects shadows by default
# We can change it by using detectShadows=False
# Shadows are shown in gray color

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame', frame)
        cv2.imshow('fg mask frame', fgmask)
        if cv2.waitKey(30) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
