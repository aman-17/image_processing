import cv2
import numpy as np

img = cv2.imread('testimg.jpeg')
w=(img.shape)
width=int(w[0]/2)
height=int(w[1]/2)

print(width,height)
cv2.imshow("original", img)

# Cropping an image

cropped_image = img[0:width, 0:height]

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped_Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

