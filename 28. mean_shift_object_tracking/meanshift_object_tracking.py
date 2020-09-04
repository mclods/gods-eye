# Importing Libraries
import numpy as np
import cv2

cap = cv2.VideoCapture('cars_moving.mkv')

# Take the first frame of the video
ret, frame = cap.read()

# Setup initial location of the window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# Setup ROI for Object Tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Low Light values are discarded using the inRange() function
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cv2.imshow('roi', roi)
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # Apply meanshift to get the new location
        retval, track_window = cv2.meanShift(dst, track_window, term_criteria)

        # Draw it on image
        x, y, w, h = track_window
        final_image = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 3)

        cv2.imshow('dst', dst)
        cv2.imshow('final_image', final_image)

        if cv2.waitKey(30) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
