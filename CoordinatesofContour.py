import cv2
import numpy as np
from numpy import asarray
#from PIL import Image
from skimage.io import imread
# from maxrect import get_maximal_rectangle

img = cv2.pyrDown(cv2.imread('T11.jpeg', cv2.IMREAD_UNCHANGED))
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
contours = contours_sorted[0] #The first index points to the contour which has maximum area .
#print(len(contours))
polydp_of_contour = cv2.approxPolyDP(contours, 0.009 * cv2.arcLength(contours, True), True)
# draws boundary of contours.
cv2.drawContours(img, [polydp_of_contour], 0, (0, 0, 0), 5)

#Apporximate polygon
#poly_dp_list = approx.ravel().tolist()
#print(np.shape(polydp_of_contour.ravel()))
polydp_of_contour = polydp_of_contour.reshape(-1,2).tolist()
#print(polydp_of_contour)

# bottom_left,top_right = get_maximal_rectangle(polydp_of_contour)
#print("Bottom Left %f" %bottom_left)
#print("Top Right %f" %top_right)
cv2.drawContours(img,contours_sorted,-1,(0,0,0),-1)
fill_color = [255, 255, 255]# any BGR color value to fill with
mask_value = 255 
stencil  = np.zeros(img.shape[:-1]).astype(np.uint8)
cv2.fillPoly(stencil, contours_sorted, mask_value)

sel = stencil != mask_value # select everything that is not mask_value
img[sel] = fill_color



arr = np.array(img)
arr = np.arange(150).reshape(5, 10, 3)
x, y, z = arr.shape
indices = np.vstack(np.unravel_index(np.arange(x*y), (y, x))).T
x1=np.hstack((arr.reshape(x*y, z), indices))
print(x1)
cv2.imshow("result.jpeg", img)
#cv2.imshow("contours", img)

while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break
cv2.destroyAllWindows()


