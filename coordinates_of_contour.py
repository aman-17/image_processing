import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread('T11.jpeg', cv2.IMREAD_UNCHANGED))


ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


### Find the contour with highest area

contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
contours = contours_sorted[0] #The first index points to the contour which has maximmum area . 

for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # get the min area rect
    rect = cv2.minAreaRect(c)
    area = w*h
    #print(area)
    #rect= cv2.convexHull(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print([box])
cv2.imshow("contours", img)
while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break
cv2.destroyAllWindows()
