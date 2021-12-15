import cv2
import numpy as np

# load image
img = cv2.imread("T11.jpeg")

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold image
thresh = cv2.threshold(gray,4,255,0)[1]

# apply morphology open to smooth the outline
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# find contours
cntrs = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]

# Contour filtering to get largest area
area_thresh = 0
for c in cntrs:
    area = cv2.contourArea(c)
    if area > area_thresh:
        area = area_thresh
        big_contour = c

# draw the contour on a copy of the input image
results = img.copy()
cv2.drawContours(results,[big_contour],0,(0,0,255),2)


# write result to disk
cv2.imshow("threshold", thresh)
cv2.imshow("contour", results)

cv2.imshow("THRESH", thresh)
cv2.imshow("RESULTS", results)
cv2.waitKey(0)
cv2.destroyAllWindows()
