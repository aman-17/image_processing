import cv2
import numpy as np
import math
import matplotlib.pyplot as plt



# img = cv2.imread("IMG_5446.jpg")
# plt.imshow(img)
# plt.show()

img = cv2.pyrDown(cv2.imread('IMG_5448.jpg', cv2.IMREAD_UNCHANGED))
gray = cv2.GaussianBlur(img, (7, 7), 0)

ret, threshed_img = cv2.threshold(cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
                
contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    
    if w*h> 10000:
        
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
        # get the min area rect
        rect = cv2.minAreaRect(c)
        area = w*h
        # print(area)
        #rect= cv2.convexHull(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        # print("y1",box[0][1])
        # print("y2",box[3][1])
        print([box])
m = 11.02
l = 11.41
s = 10.8
print("y1",box[0][1])
print("y2",box[3][1])
ppm = math.ceil((box[3][1]-box[0][1])/m)
print("PPM: ",ppm)
cv2.imshow("contours", img)
while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break
cv2.destroyAllWindows()
