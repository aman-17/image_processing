import cv2
import numpy as np

img = cv2.imread('tablest.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0,0,50])
upper = np.array([160,255,255])

mask = cv2.inRange(hsv, lower, upper)

res = cv2.bitwise_and(hsv,hsv, mask= mask)
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for i in contours:
    cnt = cv2.contourArea(i)
    if cnt > 1000:  
        cv2.drawContours(img, [i], 0, (0,0,0), -1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = max(contours, key=cv2.contourArea)
area = cv2.contourArea(cnt)
cv2.putText(img,'Gray area ='+str(area),(60,90), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
