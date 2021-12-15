import cv2
import numpy as np
from maxrect import get_maximal_rectangle,rect2poly
from maxrect import get_intersection, get_maximal_rectangle, rect2poly

img = cv2.pyrDown(cv2.imread('T11.jpeg', cv2.IMREAD_UNCHANGED))

thresh = img.copy()


ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)

cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)



cv2.namedWindow('image')




while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        contours = contours_sorted[0]
        polydp_of_contour = cv2.approxPolyDP(contours, 0.009 * cv2.arcLength(contours, True), True)
        cv2.drawContours(img, [contours], 0, (0, 0, 255), 5)
        polydp_of_contour = polydp_of_contour.reshape(-1,2).tolist()
        
        ts=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
        threshold = cv2.getTrackbarPos('threshold', 'image')
        _, thresh = cv2.threshold(ts, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1
        thresh = cv2.dilate(thresh, None, iterations=4) #2
        thresh = cv2.medianBlur(thresh, 3) #3
        thresh = cv2.bitwise_not(thresh)
        contouring(thresh[:, 0:mid], mid, img)
        contouring(thresh[:, mid:], mid, img, True)

    cv2.imshow('t-shirt', img)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
