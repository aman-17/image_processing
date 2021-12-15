
import numpy as np
from numpy import asarray
import cv2
import matplotlib.pyplot as plt
from PIL import Image

img=Image.open('F1.jpeg')
numpydata=asarray(img)
#print(numpydata.dtype)
nm=numpydata.astype('uint32')


#nm.reshape(-1)
nm.ravel()
print(nm)



#a3 = np.array( [[[500,400],[650,400],[650,550],[500,550]]], dtype=np.int32 )
im = np.zeros([2000,2000],dtype=np.uint8)

cv2.fillPoly(im, nm, 255)

plt.imshow(im)
plt.show()
'''


import numpy as np
import cv2

img = cv2.imread("F1.jpeg")
pts = np.array([[300,400],[550,400],[550,650],[300,650]])

## (1) Crop the bounding rect
rect = cv2.boundingRect(pts)
x,y,w,h = rect
croped = img[y:y+h, x:x+w].copy()

## (2) make mask
pts = pts - pts.min(axis=0)

mask = np.zeros(croped.shape[:2], np.uint8)
cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

## (3) do bit-op
dst = cv2.bitwise_and(croped, croped, mask=mask)

## (4) add the white background
bg = np.ones_like(croped, np.uint8)*255
cv2.bitwise_not(bg,bg, mask=mask)
dst2 = bg+ dst


cv2.imshow("croped.png", croped)
cv2.imshow("mask.png", mask)
cv2.imwrite("dst.png", dst)
cv2.imshow("dst2.png", dst2)
'''
