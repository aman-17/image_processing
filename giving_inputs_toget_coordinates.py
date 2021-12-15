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
image01 = cv2.imread("1.jpeg")

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
        xsmb1xh, xsmb1xl, xsmb1xb, xsmb1b, xsmb1h, xsmb1xb1 = 4.2, 4.693, 3.2, 10.877, 3.048, 3.405
        if(sex=='m' and size=='xs' and panel_id=='b1'):
            xb0=math.sqrt((xsmb1xb1**2)-(xsmb1xb**2))
            xb=math.sqrt((xsmb1xl**2)-(xsmb1xh**2))
            x1=pixelPermetric*xsmb1xh
            xx1=pixelPermetric*xb
            xxx1=pixelPermetric*xsmb1xb
            #ox=sqrt((x1**2)+(xx1**2))
            y1=pixelPermetric*xsmb1b
            x2=pixelPermetric*xsmb1h
            yy1=(xb0+x1)-(xsmb1xb1)
            c1=math.ceil(x1)
            c2=math.ceil(xx1)
            c3=math.ceil(x2)
            c4=math.ceil(y1)
            c5=math.ceil(yy1)
            c6=math.ceil(xxx1)
            c7=math.ceil(xb0)
            list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
            print(list1)
            
            #crop_img = image[350:c11, 400:c22]
            cv2.line(image01, list1[0], list1[1], (0, 255, 0), 3)
            cv2.line(image01, list1[1], list1[2], (0, 255, 0), 3)
            cv2.line(image01, list1[2], list1[3], (0, 255, 0), 3)
            cv2.line(image01, list1[3], list1[4], (0, 255, 0), 3)
            cv2.line(image01, list1[4], list1[0], (0, 255, 0), 3)
            cv2.imshow("out", image01)
            #cv2.imshow("cropped", crop_img)
            k=cv2.waitKey(0) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
