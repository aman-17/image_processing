from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import math
from shapely.affinity import scale
from shapely.ops import transform
from shapely.geometry import Polygon
import json

width=0.955
b, h = 4.748, 4.233 

#s=29, m=29.5, l=30.5, xl=31, ts=29.5, tm=30, tl=31, txl=31.5

img = cv2.imread("test1.jpeg")

plt.imshow(img)
plt.show()

p=abs(747/31)


f = open('dh-34-panel.json')
data = json.load(f)
d=data["txl"]["f"]["b10"]

d1=data["txl"]["f"]["b4"]

d2=data["txl"]["f"]["b8"]




c1 = math.ceil(p * float(d1['h']))
c2 = math.ceil(p * float(d1['b']))
coordinates = [(178+0, 605+0),(178+0, 605+c2),(178+ c1, 605+c2),(178+0 + c1, 605+0)]
list1 = [coordinates[3], coordinates[2], coordinates[1], coordinates[0]]
# p=74

c1 = math.ceil(p * float(d2['h']))
c2 = math.ceil(p * float(d2['b']))
coordinates = [(424+0, 506+0),(424+0, 506+c2),(424+ c1-50, 506+c2),(424+0-50 + c1, 506+0)]
list2 = [coordinates[3], coordinates[2], coordinates[1], coordinates[0]]

img=cv2.line(img, list1[0], list1[1], (0,255,0), 2)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 2)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 2)
img=cv2.line(img, list1[3], list1[0], (0,255,0), 2)


img=cv2.line(img, list2[0], list2[1], (0,255,0), 2)
img=cv2.line(img, list2[1], list2[2], (0,255,0), 2)
img=cv2.line(img, list2[2], list2[3], (0,255,0), 2)
img=cv2.line(img, list2[3], list2[0], (0,255,0), 2)

# img=cv2.line(img, list1[4], list1[5], (0,255,0), 2)

# img=cv2.line(img, list1[5], list1[6], (0,255,0), 2)
# img=cv2.line(img, list1[6], list1[7], (0,255,0), 2)
# img=cv2.line(img, list1[7], list1[8], (0,255,0), 2)
# img=cv2.line(img, list1[8], list1[9], (0,255,0), 2)
# img=cv2.line(img, list1[9], list1[10], (0,255,0), 2)
# img=cv2.line(img, list1[10], list1[11], (0,255,0), 2)
# img=cv2.line(img, list1[11], list1[12], (0,255,0), 2)
# img=cv2.line(img, list1[12], list1[13], (0,255,0), 2)
# img=cv2.line(img, list1[13], list1[14], (0,255,0), 2)
# img=cv2.line(img, list1[14], list1[15], (0,255,0), 2)
# img=cv2.line(img, list1[15], list1[16], (0,255,0), 2)
# img=cv2.line(img, list1[16], list1[17], (0,255,0), 2)
# img=cv2.line(img, list1[17], list1[18], (0,255,0), 2)
# img=cv2.line(img, list1[18], list1[19], (0,255,0), 2)
# img=cv2.line(img, list1[19], list1[20], (0,255,0), 2)
# img=cv2.line(img, list1[20], list1[21], (0,255,0), 2)
# img=cv2.line(img, list1[21], list1[22], (0,255,0), 2)
# img=cv2.line(img, list1[22], list1[23], (0,255,0), 2)
# img=cv2.line(img, list1[23], list1[24], (0,255,0), 2)
# img=cv2.line(img, list1[24], list1[25], (0,255,0), 2)

# img=cv2.line(img, list1[25], list1[26], (0,255,0), 2)
# img=cv2.line(img, list1[26], list1[27], (0,255,0), 2)
# img=cv2.line(img, list1[27], list1[28], (0,255,0), 2)
# img=cv2.line(img, list1[28], list1[29], (0,255,0), 2)
# img=cv2.line(img, list1[29], list1[30], (0,255,0), 2)
# img=cv2.line(img, list1[30], list1[31], (0,255,0), 2)
# img=cv2.line(img, list1[31], list1[32], (0,255,0), 2)
# img=cv2.line(img, list1[32], list1[33], (0,255,0), 2)
# img=cv2.line(img, list1[33], list1[34], (0,255,0), 2)
# img=cv2.line(img, list1[34], list1[35], (0,255,0), 2)
# img=cv2.line(img, list1[35], list1[36], (0,255,0), 2)
# img=cv2.line(img, list1[36], list1[37], (0,255,0), 2)
# img=cv2.line(img, list1[37], list1[38], (0,255,0), 2)
# img=cv2.line(img, list1[38], list1[39], (0,255,0), 2)
# img=cv2.line(img, list1[39], list1[40], (0,255,0), 2)
# img=cv2.line(img, list1[40], list1[41], (0,255,0), 2)
# img=cv2.line(img, list1[41], list1[42], (0,255,0), 2)
# img=cv2.line(img, list1[42], list1[43], (0,255,0), 2)
# img=cv2.line(img, list1[43], list1[44], (0,255,0), 2)
# img=cv2.line(img, list1[44], list1[45], (0,255,0), 2)
# img=cv2.line(img, list1[45], list1[46], (0,255,0), 2)
# img=cv2.line(img, list1[46], list1[47], (0,255,0), 2)
# img=cv2.line(img, list1[47], list1[48], (0,255,0), 2)
# img=cv2.line(img, list1[48], list1[49], (0,255,0), 2)
# img=cv2.line(img, list1[49], list1[50], (0,255,0), 2)
# img=cv2.line(img, list1[50], list1[51], (0,255,0), 2)
# img=cv2.line(img, list1[51], list1[52], (0,255,0), 2)
# img=cv2.line(img, list1[52], list1[53], (0,255,0), 2)
# img=cv2.line(img, list1[53], list1[54], (0,255,0), 2)
# img=cv2.line(img, list1[54], list1[0], (0,255,0), 2)

cv2.imshow('no-coin-1.jpg', img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

