from turtle import width
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
from pprint import pprint
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os
width=0.955

# name="IMG_5430.xml"
# img_names = os.path.basename(name).split(".")[0]
# img = cv2.imread(img_names+'.jpg')



# tree = ET.parse('/Users/amanrangapur/desktop/labels_my-project-name_2022-02-01-01-21-27/'+name)
# root = tree.getroot() 

# xmin = (root[5][4][0].text)
# print("xmin: ",xmin)

# xmax = (root[5][4][2].text)
# print("xmax: ",xmax)

# p=math.ceil((int(xmax)-int(xmin))/width)
# print(p)

#h3=365,532
#f1=587,703
#b1=337,974

img = cv2.imread("test3.jpeg")

f = open('dh-34-panel.json')
data = json.load(f)
d=data["xs"]["f"]["h3"]

d1=data["xs"]["f"]["b1"]

d2=data["xs"]["f"]["f1"]

# d3=data["txl"]["m"]["fc2"]


#b10=210,422
#b8=424,506 (right-big)
#b4=178,604

# plt.imshow(img)
# plt.show()


# p=35



#s=29, m=29.5, l=30.5, xl=31, ts=29.5, tm=30, tl=31, txl=31.5

pixelsPerMetric = abs(920-157)/29


# c1 = math.ceil(pixelsPerMetric * float(d2['h']))
# c2 = math.ceil(pixelsPerMetric * float(d2['b']))
# coordinates = [(210+0, 422+0),(210+0 + c1, 422+0),(210+0 + c1, 422+0 + c2),(210+0, 422+c2)] 
# list1 = [coordinates[3], coordinates[2], coordinates[1], coordinates[0]]

# img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
# img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
# img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
# img=cv2.line(img, list1[3], list1[0], (0,255,0), 6)



# c1 = math.ceil(pixelsPerMetric * float(d['h']))
# c2 = math.ceil(pixelsPerMetric * float(d['b']))
# coordinates = [(178+0, 604+0),(178+0 + c1, 604+0),(178+0 + c1, 604+0 + c2),(178+0, 604+c2)] 
# list1 = [coordinates[3], coordinates[2], coordinates[1], coordinates[0]]

# img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
# img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
# img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
# img=cv2.line(img, list1[3], list1[0], (0,255,0), 6)


# c1 = math.ceil(pixelsPerMetric * float(d1['h']))
# c2 = math.ceil(pixelsPerMetric * float(d1['b']))
# coordinates = [(432+0, 512+0),(432+0 + c1, 512+0),(432+0 + c1, 512+0 + c2),(432+0, 512+c2)] 
# list1 = [coordinates[3], coordinates[2], coordinates[1], coordinates[0]]

# img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
# img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
# img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
# img=cv2.line(img, list1[3], list1[0], (0,255,0), 6)






c0=math.ceil(pixelsPerMetric*float(d['h']))
c1=math.ceil(pixelsPerMetric*float(d['b']))

ccx1=math.ceil(pixelsPerMetric*float(d['cx1']))
ccx2=math.ceil(pixelsPerMetric*float(d['cx2']))
ccx3=math.ceil(pixelsPerMetric*float(d['cx3']))
ccx4=math.ceil(pixelsPerMetric*float(d['cx4']))
ccx5=math.ceil(pixelsPerMetric*float(d['cx5']))
ccx6=math.ceil(pixelsPerMetric*float(d['cx6']))
ccx7=math.ceil(pixelsPerMetric*float(d['cx7']))
ccx8=math.ceil(pixelsPerMetric*float(d['cx8']))
ccx9=math.ceil(pixelsPerMetric*float(d['cx9']))
ccx10=math.ceil(pixelsPerMetric*float(d['cx10']))
ccx11=math.ceil(pixelsPerMetric*float(d['cx11']))
ccx12=math.ceil(pixelsPerMetric*float(d['cx12']))
ccx13=math.ceil(pixelsPerMetric*float(d['cx13']))
ccx14=math.ceil(pixelsPerMetric*float(d['cx14']))
ccx15=math.ceil(pixelsPerMetric*float(d['cx15']))
ccx16=math.ceil(pixelsPerMetric*float(d['cx16']))

ccy1=math.ceil(pixelsPerMetric*float(d['cy1']))
ccy2=math.ceil(pixelsPerMetric*float(d['cy2']))
ccy3=math.ceil(pixelsPerMetric*float(d['cy3']))
ccy4=math.ceil(pixelsPerMetric*float(d['cy4']))
ccy5=math.ceil(pixelsPerMetric*float(d['cy5']))
ccy6=math.ceil(pixelsPerMetric*float(d['cy6']))
ccy7=math.ceil(pixelsPerMetric*float(d['cy7']))
ccy8=math.ceil(pixelsPerMetric*float(d['cy8']))
ccy9=math.ceil(pixelsPerMetric*float(d['cy9']))
ccy10=math.ceil(pixelsPerMetric*float(d['cy10']))
ccy11=math.ceil(pixelsPerMetric*float(d['cy11']))
ccy12=math.ceil(pixelsPerMetric*float(d['cy12']))
ccy13=math.ceil(pixelsPerMetric*float(d['cy13']))
ccy14=math.ceil(pixelsPerMetric*float(d['cy14']))
ccy15=math.ceil(pixelsPerMetric*float(d['cy15']))
ccy16=math.ceil(pixelsPerMetric*float(d['cy16']))
list1=[(365+0,532+0),(365+0,532+c0),(365+ccx16,532+ccy16),(365+ccx15,532+ccy15),(365+ccx14,532+ccy14),(365+ccx13,532+ccy13),(365+ccx12,532+ccy12),
(365+ccx11,532+ccy11),(365+ccx10,532+ccy10),(365+ccx9,532+ccy9),(365+ccx8,532+ccy8),(365+ccx7,532+ccy7),(365+ccx6,532+ccy6),(365+ccx5,532+ccy5),
(365+ccx4,532+ccy4),(365+ccx3,532+ccy3),(365+ccx2,532+ccy2),(365+ccx1,532+ccy1),(365+c1,532+0)]

img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
img=cv2.line(img, list1[3], list1[4], (0,255,0), 6)
img=cv2.line(img, list1[4], list1[5], (0,255,0), 6)
img=cv2.line(img, list1[5], list1[6], (0,255,0), 6)
img=cv2.line(img, list1[6], list1[7], (0,255,0), 6)
img=cv2.line(img, list1[7], list1[8], (0,255,0), 6)
img=cv2.line(img, list1[8], list1[9], (0,255,0), 6)
img=cv2.line(img, list1[9], list1[10], (0,255,0), 6)
img=cv2.line(img, list1[10], list1[11], (0,255,0), 6)
img=cv2.line(img, list1[11], list1[12], (0,255,0), 6)
img=cv2.line(img, list1[12], list1[13], (0,255,0), 6)
img=cv2.line(img, list1[13], list1[14], (0,255,0), 6)
img=cv2.line(img, list1[14], list1[15], (0,255,0), 6)
img=cv2.line(img, list1[15], list1[16], (0,255,0), 6)
img=cv2.line(img, list1[16], list1[17], (0,255,0), 6)
img=cv2.line(img, list1[17], list1[18], (0,255,0), 6)
img=cv2.line(img, list1[18], list1[0], (0,255,0), 6)


c1=math.ceil(pixelsPerMetric*float(d1['h']))
c2=math.ceil(pixelsPerMetric*float(d1['b']))

ccx1=math.ceil(pixelsPerMetric*float(d1['cx1']))
ccx2=math.ceil(pixelsPerMetric*float(d1['cx2']))
ccx3=math.ceil(pixelsPerMetric*float(d1['cx3']))
ccx4=math.ceil(pixelsPerMetric*float(d1['cx4']))
ccx5=math.ceil(pixelsPerMetric*float(d1['cx5']))
ccx6=math.ceil(pixelsPerMetric*float(d1['cx6']))
ccx7=math.ceil(pixelsPerMetric*float(d1['cx7']))

ccy1=math.ceil(pixelsPerMetric*float(d1['cy1']))
ccy2=math.ceil(pixelsPerMetric*float(d1['cy2']))
ccy3=math.ceil(pixelsPerMetric*float(d1['cy3']))
ccy4=math.ceil(pixelsPerMetric*float(d1['cy4']))
ccy5=math.ceil(pixelsPerMetric*float(d1['cy5']))
ccy6=math.ceil(pixelsPerMetric*float(d1['cy6']))
ccy7=math.ceil(pixelsPerMetric*float(d1['cy7']))

xp4 = float(d1['xp3'])+float(d1['b'])

cpx1=math.ceil(float(d1['xp1'])*pixelsPerMetric)
cpx2=math.ceil(float(d1['xp2'])*pixelsPerMetric)
cpx3=math.ceil(float(d1['xp3'])*pixelsPerMetric)
cpx4=math.ceil(float(xp4)*pixelsPerMetric)

cpy1=math.ceil(float(d1['yp1'])*pixelsPerMetric)
cpy2=math.ceil(float(d1['yp2'])*pixelsPerMetric)
cpy3=math.ceil(float(d1['yp3'])*pixelsPerMetric)

list1 = [(337+cpx2,974+cpy2),(337+cpx3,974+cpy3),(337+cpx4,974+cpy3),(337+cpx4,974+cpy3-c1),(337+ccx7,974+ccy7),
(337+ccx6,974+ccy6),(337+ccx5,974+ccy5),(337+ccx4,974+ccy4),(337+ccx3,974+ccy3),(337+ccx2,974+ccy2),(337+ccx1,974+ccy1),(337+cpx1,974+cpy1)]


img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
img=cv2.line(img, list1[3], list1[4], (0,255,0), 6)
img=cv2.line(img, list1[4], list1[5], (0,255,0), 6)
img=cv2.line(img, list1[5], list1[6], (0,255,0), 6)
img=cv2.line(img, list1[6], list1[7], (0,255,0), 6)
img=cv2.line(img, list1[7], list1[8], (0,255,0), 6)
img=cv2.line(img, list1[8], list1[9], (0,255,0), 6)
img=cv2.line(img, list1[9], list1[10], (0,255,0), 6)
img=cv2.line(img, list1[10], list1[11], (0,255,0), 6)
img=cv2.line(img, list1[11], list1[0], (0,255,0), 6)


c1=math.ceil(pixelsPerMetric*float(d2['h']))
c2=math.ceil(pixelsPerMetric*float(d2['b']))

ccx1=math.ceil(pixelsPerMetric*float(d2['cx1']))
ccx2=math.ceil(pixelsPerMetric*float(d2['cx2']))
ccx3=math.ceil(pixelsPerMetric*float(d2['cx3']))
ccx4=math.ceil(pixelsPerMetric*float(d2['cx4']))
ccx5=math.ceil(pixelsPerMetric*float(d2['cx5']))
ccx6=math.ceil(pixelsPerMetric*float(d2['cx6']))
ccx7=math.ceil(pixelsPerMetric*float(d2['cx7']))
ccx8=math.ceil(pixelsPerMetric*float(d2['cx8']))
ccx9=math.ceil(pixelsPerMetric*float(d2['cx9']))

ccy1=math.ceil(pixelsPerMetric*float(d2['cy1']))
ccy2=math.ceil(pixelsPerMetric*float(d2['cy2']))
ccy3=math.ceil(pixelsPerMetric*float(d2['cy3']))
ccy4=math.ceil(pixelsPerMetric*float(d2['cy4']))
ccy5=math.ceil(pixelsPerMetric*float(d2['cy5']))
ccy6=math.ceil(pixelsPerMetric*float(d2['cy6']))
ccy7=math.ceil(pixelsPerMetric*float(d2['cy7']))
ccy8=math.ceil(pixelsPerMetric*float(d2['cy8']))
ccy9=math.ceil(pixelsPerMetric*float(d2['cy9']))

xcp1=math.ceil(float(d2['xp1'])*pixelsPerMetric)
xcp2=math.ceil(float(d2['xp2'])*pixelsPerMetric)
xcp3=math.ceil(float(d2['xp3'])*pixelsPerMetric)

ycp1=math.ceil(float(d2['yp1'])*pixelsPerMetric)
ycp2=math.ceil(float(d2['yp2'])*pixelsPerMetric)
ycp3=math.ceil(float(d2['yp3'])*pixelsPerMetric)
list1=[(593+xcp1,703+ycp1),(593+xcp3,703+ycp3),(593+ccx1,703+ccy1),(593+ccx2,703+ccy2),(593+ccx3,703+ccy3),(593+ccx4,703+ccy4),(593+ccx5,703+ccy5),
(593+ccx6,703+ccy6),(593+ccx7,703+ccy7),(593+ccx8,703+ccy8),(593+ccx9,703+ccy9),(593+0,703+c1+ycp2),(593+c2,703+c1+ycp2),(593+xcp2,703+ycp2)]

img=cv2.line(img, list1[0], list1[1], (0,255,0), 6)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 6)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 6)
img=cv2.line(img, list1[3], list1[4], (0,255,0), 6)
img=cv2.line(img, list1[4], list1[5], (0,255,0), 6)
img=cv2.line(img, list1[5], list1[6], (0,255,0), 6)
img=cv2.line(img, list1[6], list1[7], (0,255,0), 6)
img=cv2.line(img, list1[7], list1[8], (0,255,0), 6)
img=cv2.line(img, list1[8], list1[9], (0,255,0), 6)
img=cv2.line(img, list1[9], list1[10], (0,255,0), 6)
img=cv2.line(img, list1[10], list1[11], (0,255,0), 6)
img=cv2.line(img, list1[11], list1[12], (0,255,0), 6)

img=cv2.line(img, list1[12], list1[13], (0,255,0), 6)
img=cv2.line(img, list1[13], list1[0], (0,255,0), 6)




# img=cv2.line(img, list1[14], list1[15], (0,255,0), 6)
# img=cv2.line(img, list1[15], list1[16], (0,255,0), 6)
# img=cv2.line(img, list1[16], list1[17], (0,255,0), 6)
# img=cv2.line(img, list1[17], list1[18], (0,255,0), 6)
# img=cv2.line(img, list1[18], list1[19], (0,255,0), 6)
# img=cv2.line(img, list1[19], list1[20], (0,255,0), 6)
# img=cv2.line(img, list1[20], list1[21], (0,255,0), 6)
# img=cv2.line(img, list1[21], list1[22], (0,255,0), 6)
# img=cv2.line(img, list1[22], list1[23], (0,255,0), 6)
# img=cv2.line(img, list1[23], list1[24], (0,255,0), 6)
# img=cv2.line(img, list1[24], list1[25], (0,255,0), 6)
# img=cv2.line(img, list1[25], list1[26], (0,255,0), 6)
# img=cv2.line(img, list1[26], list1[27], (0,255,0), 6)
# img=cv2.line(img, list1[27], list1[28], (0,255,0), 6)
# img=cv2.line(img, list1[28], list1[29], (0,255,0), 6)
# img=cv2.line(img, list1[29], list1[30], (0,255,0), 6)
# img=cv2.line(img, list1[30], list1[31], (0,255,0), 6)
# img=cv2.line(img, list1[31], list1[32], (0,255,0), 6)
# img=cv2.line(img, list1[32], list1[33], (0,255,0), 6)
# img=cv2.line(img, list1[33], list1[34], (0,255,0), 6)
# img=cv2.line(img, list1[34], list1[35], (0,255,0), 6)
# img=cv2.line(img, list1[35], list1[36], (0,255,0), 6)
# img=cv2.line(img, list1[36], list1[0], (0,255,0), 6)


cv2.imshow('no-coin-1.jpg', img)
# cv2.imwrite("IMG_5438-f.jpg",img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

