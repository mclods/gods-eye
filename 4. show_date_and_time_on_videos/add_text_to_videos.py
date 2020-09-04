# Importing Libraries
import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        # Printing Width and Height
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Printing Date and Time
        curr_datetime = str(datetime.datetime.now())

        frame = cv2.putText(frame, curr_datetime, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
