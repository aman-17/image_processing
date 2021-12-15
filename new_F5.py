# import the necessary packages
import math
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
from skimage import io

import imutils
import cv2
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


width=0.9055




def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect
    
def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	
	return warped
#image01 = io.imread('https://images-na.ssl-images-amazon.com/images/I/81FXuE3hvVL._SL1500_.jpg')
image01 = cv2.imread("B4.jpeg")

pts = np.array([(0,0),(1000,0),(1000,800),(0,800)], dtype = "float32")
# apply the four point tranform to obtain a "birds eye view" of
# the image
image = four_point_transform(image01, pts)

# load the image, convert it to grayscale, and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# sort the contours from left-to-right and initialize the
# 'pixels per metric' calibration variable
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None


# loop over the contours individually
for c in cnts:
    # if the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 100:
        continue
    # compute the rotated bounding box of the contour
    orig = image.copy()
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    
    # unpack the ordered bounding box, then compute the midpoint
    # between the top-left and top-right coordinates, followed by
    # the midpoint between bottom-left and bottom-right coordinates
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    # compute the midpoint between the top-left and top-right points,
    # followed by the midpoint between the top-righ and bottom-right
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    
    # compute the Euclidean distance between the midpoints
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    # if the pixels per metric has not been initialized, then
    # compute it as the ratio of pixels to supplied metric
    # (in this case, inches)
    if pixelsPerMetric is None:
        pixelsPerMetric = dB / width
        print(pixelsPerMetric)
        sex=input("Enter the sex (m/f): ")
        size=input("Enter the size: ")
        panel_id=input("Enter the panel_id: ")
        #pixelPermetric=20
        xsmf5h, xsmf5b = 1.717, 7.389
        xsmf6h, xsmf6b = 2.966, 7.411
        xsmf7h, xsmf7b = 4.662, 7.564
        xsmf8h, xsmf8b = 3.416, 14.933
        xsmf3h, xsmf3b = 3.395, 2.750
        xsmf4h, xsmf4b = 3.395, 2.579
        xsmb4h, xsmb4b = 7.258, 4.302
        xsmb6h, xsmb6b = 7.104, 5.089
        xsmb7h, xsmb7b = 7.258, 8.679
        xsmb8h, xsmb8b = 6.294, 8.679
        xsmb9h, xsmb9b = 7.103, 9.820
        xsmb10h, xsmb10b = 4.681, 6.233
        xsmb11h, xsmb11b = 4.748, 6.233
        xsmb12h, xsmb12b = 4.136, 6.238
        smf5h, smf5b = 2.35, 7.4
        smf6h, smf6b = 2.97, 7.42
        smf7h, smf7b = 5.32, 7.57
        smf8h, smf8b = 3.42, 14.94
        smf3h, smf3b = 3.395, 2.5
        smf4h, smf4b = 3.395, 2.58
        smb4h, smb4b = 7.26, 4.3
        smb6h, smb6b = 7.73, 5.04
        smb7h, smb7b = 7.25, 8.68
        smb8h, smb8b = 6.92, 8.68
        smb9h, smb9b = 7.73, 9.82
        smb10h, smb10b = 4.681, 6.233
        smb11h, smb11b = 4.748, 6.233
        smb12h, smb12b = 4.671, 6.238
        if(sex=='m' and size=='s' and panel_id=='b4'):
            x=pixelsPerMetric*smb4h
            y=pixelsPerMetric*smb4b
            c1=math.ceil(x)
            c2=math.ceil(y)
            #list0=[(0,0),(xsmf5h,0),(xsmf5h, xsmf5b),(0,xsmf5b)]
            #print(list0)
            list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
            print(list1)

            c11=350+c2
            c22=400+c1
            crop_img = image[350:c11, 400:c22]
            cv2.imshow("out", image01)
            cv2.imshow("cropped", crop_img)
            k=cv2.waitKey(0) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
