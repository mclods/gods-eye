# Importing Libraries
import cv2

# Capture Video from Device Camera
cap = cv2.VideoCapture(0)

# Get fourcc Code
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Class for writing Video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Check if Video can be Captured
print(cap.isOpened())

while cap.isOpened():
    
    # Read the Frame
    # ret = True / False whether frame is available
    # frame = Frame Object
    ret, frame = cap.read()
    
    if ret:
        
        # Print frame width and height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Write Captured Video
        out.write(frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()

