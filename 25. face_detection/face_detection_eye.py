# Importing Libraries
import numpy as np
import cv2

# Trained Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    ret, img = cap.read()

    if ret is True:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            roi_eye_gray = gray[y:y+h, x:x+w]
            roi_eye_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_eye_gray)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
