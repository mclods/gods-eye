# Importing Libraries
import cv2

# Reading an Image
img = cv2.imread('lena.jpg', -1)    
print(img)

# Show the Image 
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

# Close the image window if user presses q
# Write the image if user presses s
if k == ord('q'):

    # Destroy all Image Windows
    cv2.destroyAllWindows()

elif k == ord('s'):

    # Writing an Image
    cv2.imwrite('lena_copy.png', img)

    cv2.destroyAllWindows()

