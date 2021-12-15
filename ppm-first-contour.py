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

global x1,y1,y3
width=1.02
image = cv2.imread("1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)

cnts_1=cnts[0]
img = cv2.drawContours(image, cnts_1, -1, (0, 255, 0), 3)
pixelsPerMetric = None
box = cv2.minAreaRect(cnts_1)
box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
box = np.array(box, dtype="int")
(tl, tr, br, bl) = box
(tltrX, tltrY) = midpoint(tl, tr)
(blbrX, blbrY) = midpoint(bl, br)
(tlblX, tlblY) = midpoint(tl, bl)
(trbrX, trbrY) = midpoint(tr, br)
dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
if pixelsPerMetric is None:
    pixelsPerMetric = dB / width
    p=math.floor(pixelsPerMetric)
    print(p)
   
lff2h, lff2b, lff2s = 3.300, 3.395, 0.824
x1=p*lff2h
y1=p*lff2b
y2=p*lff2s
c1=math.ceil(x1)
c2=math.ceil(y1)
c3=math.ceil(y2)
    
list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
print(list1)
'''    
img=cv2.line(image, list1[0], list1[1], (255,0,0), 2)
img=cv2.line(image, list1[1], list1[2], (255,0,0), 2)
img=cv2.line(image, list1[2], list1[3], (255,0,0), 2)
img=cv2.line(image, list1[3], list1[0], (255,0,0), 2)
'''
cv2.imshow('T-CH2.jpeg', img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

