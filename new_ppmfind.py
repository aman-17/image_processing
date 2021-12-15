# import the necessary packages
import math
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

global x1,y1
width=1.069
x1,y1 = 3.416,14.933



# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("ch1.jpeg")

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
        p=math.floor(pixelsPerMetric)
        print(p)
        #print(image.size)   

    if(p>100):
        p1=35
        
        xsmch2h, xsmch2b, xsmch2xb = 6.577, 3.929, 3.510
    
        x1=p1*xsmch2h
        y1=p1*xsmch2b
        x2=p1*xsmch2xb
        c1=math.ceil(x1)
        c2=math.ceil(y1)
        c3=math.ceil(x2)
        l=c2-c3
    
        list1=[(0,0),(c2,0),(c2,c1),(l,c1)]
        print(list1)
        
        ''' 
        start_point = (450, 555)
        end_point = ((450+28), (555))
    
        start_point1 = (450, 555)
        end_point1 = ((450+c1), (555+c2))
    
        start_point2 = (450, 555)
        end_point2 = ((450+c1), (555+c2))

        start_point2 = (450, 555)
        end_point2 = ((450+c1), (555+c2))

        img=cv2.line(image, list1[0], list1[1], (0,0,0), 2)
        img=cv2.line(image, list1[1], list1[2], (0,0,0), 2)
        img=cv2.line(image, list1[2], list1[3], (0,0,0), 2)
        img=cv2.line(image, list1[3], list1[0], (0,0,0), 2)
        '''
    
    
        cv2.imshow('T-F8.jpeg', img)

        k=cv2.waitKey(0) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
        
    else:
        
        xsmf1xh, xsmf1xb, xsmf1s, xsmf1h, xsmf1b = 0.8, 3.484, 1.108, 7.883, 4.683
    
    
        l0=math.sqrt((xsmf1xb**2)-(xsmf1xh**2))
        l1=xsmf1b-l0
        l2=math.sqrt((xsmf1s**2)-(xsmf1xh**2))
        l3=xsmf1h+xsmf1xh
        l4=xsmf1b+l2
        x0=p*(l0+l1)
        x1=p*l0
        x2=p*l1
        x3=p*l2
        y1=p*xsmf1xh
        y2=p*l3
        y3=p*xsmf1b
        y4=p*l4
        
        c0=math.ceil(x0)
        c1=math.ceil(x1)
        c2=math.ceil(x2)
        c3=math.ceil(y1)
        c4=math.ceil(y2)
        c5=math.ceil(y3)
        c6=math.ceil(y4)
        list1=[(c0,0),(c2,c3),(c6,c3),(c6,c4),(0,c4)]
        print(list1)   
         
        start_point = (450, 555)
        end_point = ((450+28), (555))
    
        start_point1 = (450, 555)
        end_point1 = ((450+c1), (555+c2))
    
        start_point2 = (450, 555)
        end_point2 = ((450+c1), (555+c2))

        start_point2 = (450, 555)
        end_point2 = ((450+c1), (555+c2))

        img=cv2.line(image, list1[0], list1[1], (0,0,0), 2)
        img=cv2.line(image, list1[0], list1[2], (0,0,0), 2)
        img=cv2.line(image, list1[2], list1[3], (0,0,0), 2)
        img=cv2.line(image, list1[3], list1[4], (0,0,0), 2)
        img=cv2.line(image, list1[4], list1[1], (0,0,0), 2)
    
    
        cv2.imshow('T-F8.jpeg', img)

        k=cv2.waitKey(0) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
    
