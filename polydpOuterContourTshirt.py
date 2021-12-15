import cv2
import numpy as np
#from maxrect import get_maximal_rectangle,rect2poly
#from maxrect import get_intersection, get_maximal_rectangle, rect2poly
# img=cv2.imread('')
img = cv2.pyrDown(cv2.imread('2.jpg', cv2.IMREAD_UNCHANGED))
#img = cv2.medianBlur(img,5)
#fname='T1.jpeg'

ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
           # cv2.THRESH_BINARY,11,2)
cv2.imshow('fnam', threshed_img)

while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break
cv2.destroyAllWindows()
contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


### Find the contour with highest area

contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
contours = contours_sorted[0] #The first index points to the contour which has maximmum area .
#print(len(contours))


polydp_of_contour = cv2.approxPolyDP(contours, 0.009 * cv2.arcLength(contours, True), True)
  
# draws boundary of contours.

cv2.drawContours(img, [contours], 0, (0, 0, 255), 5)


#Apporximate polygon
#poly_dp_list = approx.ravel().tolist()
#print(np.shape(polydp_of_contour.ravel()))

polydp_of_contour = polydp_of_contour.reshape(-1,2).tolist()
#print(polydp_of_contour)

'''
for i in range(len(polydp_of_contour)):
    print(polydp_of_contour[i])
    data = np.array(polydp_of_contour, dtype=np.int32)
    print(data)
    hull=cv2.convexHull(data) #error here
    drawing = np.zeros((threshed_img.shape[0], threshed_img.shape[1], 3), np.uint8)
    cv2.drawContours(img,[hull], -1, (255, 0, 0), 2)

'''



#bottom_left,top_right = get_maximal_rectangle(polydp_of_contour)
#print("Bottom Left %f" %bottom_left)
#print("Top Right %f" %top_right)

#print(type(bottom_left))
#print('\n')
#print(rect2poly(bottom_left,top_right))


#img1 = cv2.rectangle(img, (240,170), (328, 315), (255, 0, 0), 2)
cv2.imshow('fnam', img)

while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break
cv2.destroyAllWindows()




