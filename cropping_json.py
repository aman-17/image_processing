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
width=0.955


tree = ET.parse('/Users/amanrangapur/desktop/labels_my-project-name_2022-02-01-01-21-27/IMG_5419.xml')
root = tree.getroot() 

xmin = (root[5][4][0].text)
print("xmin: ",xmin)

xmax = (root[5][4][2].text)
print("xmax: ",xmax)

p=math.ceil((int(xmax)-int(xmin))/width)
print(p)




f = open('dh-4-panel.json')
data = json.load(f)
d=data["txl"]["m"]["hc2"]

d1=data["txl"]["m"]["fc1"]

d2=data["txl"]["m"]["bc1"]

d3=data["txl"]["m"]["fc2"]


img = cv2.imread("IMG_5438.jpg")

# plt.imshow(img)
# plt.show()


# p=35



px1=math.ceil(p*d['xp1'])
px2=math.ceil(p*d['xp2'])

py1=math.ceil(p*d['yp1'])
py2=math.ceil(p*d['yp2'])

xc1=math.ceil(p*d['cx1'])
xc2=math.ceil(p*d['cx2'])
xc3=math.ceil(p*d['cx3'])
xc4=math.ceil(p*d['cx4'])
xc5=math.ceil(p*d['cx5'])
xc6=math.ceil(p*d['cx6'])
xc7=math.ceil(p*d['cx7'])
xc8=math.ceil(p*d['cx8'])
xc9=math.ceil(p*d['cx9'])
xc10=math.ceil(p*d['cx10'])
xc11=math.ceil(p*d['cx11'])
xc12=math.ceil(p*d['cx12'])
xc13=math.ceil(p*d['cx13'])
xc14=math.ceil(p*d['cx14'])
xc15=math.ceil(p*d['cx15'])
xc16=math.ceil(p*d['cx16'])
xc17=math.ceil(p*d['cx17'])
xc18=math.ceil(p*d['cx18'])
xc19=math.ceil(p*d['cx19'])
xc20=math.ceil(p*d['cx20'])
xc21=math.ceil(p*d['cx21'])
xc22=math.ceil(p*d['cx22'])
xc23=math.ceil(p*d['cx23'])
xc24=math.ceil(p*d['cx24'])
xc25=math.ceil(p*d['cx25'])
xc26=math.ceil(p*d['cx26'])
xc27=math.ceil(p*d['cx27'])
xc28=math.ceil(p*d['cx28'])
xc29=math.ceil(p*d['cx29'])
xc30=math.ceil(p*d['cx30'])
xc31=math.ceil(p*d['cx31'])
xc32=math.ceil(p*d['cx32'])
xc33=math.ceil(p*d['cx33'])
xc34=math.ceil(p*d['cx34'])
xc35=math.ceil(p*d['cx35'])

yc1=math.ceil(p*d['cy1'])
yc2=math.ceil(p*d['cy2'])
yc3=math.ceil(p*d['cy3'])
yc4=math.ceil(p*d['cy4'])
yc5=math.ceil(p*d['cy5'])
yc6=math.ceil(p*d['cy6'])
yc7=math.ceil(p*d['cy7'])
yc8=math.ceil(p*d['cy8'])
yc9=math.ceil(p*d['cy9'])
yc10=math.ceil(p*d['cy10'])
yc11=math.ceil(p*d['cy11'])
yc12=math.ceil(p*d['cy12'])
yc13=math.ceil(p*d['cy13'])
yc14=math.ceil(p*d['cy14'])
yc15=math.ceil(p*d['cy15'])
yc16=math.ceil(p*d['cy16'])
yc17=math.ceil(p*d['cy17'])
yc18=math.ceil(p*d['cy18'])
yc19=math.ceil(p*d['cy19'])
yc20=math.ceil(p*d['cy20'])
yc21=math.ceil(p*d['cy21'])
yc22=math.ceil(p*d['cy22'])
yc23=math.ceil(p*d['cy23'])
yc24=math.ceil(p*d['cy24'])
yc25=math.ceil(p*d['cy25'])
yc26=math.ceil(p*d['cy26'])
yc27=math.ceil(p*d['cy27'])
yc28=math.ceil(p*d['cy28'])
yc29=math.ceil(p*d['cy29'])
yc30=math.ceil(p*d['cy30'])
yc31=math.ceil(p*d['cy31'])
yc32=math.ceil(p*d['cy32'])
yc33=math.ceil(p*d['cy33'])
yc34=math.ceil(p*d['cy34'])
yc35=math.ceil(p*d['cy35'])

list1=[(2000+px1,1700+py1),(2000+xc1,1700+yc1),(2000+xc2,1700+yc2),(2000+xc3,1700+yc3),(2000+xc4,1700+yc4),(2000+xc5,1700+yc5),(2000+xc6,1700+yc6),
(2000+xc7,1700+yc7),(2000+xc8,1700+yc8),(2000+xc9,1700+yc9),(2000+xc10,1700+yc10),(2000+xc11,1700+yc11),(2000+xc12,1700+yc12),(2000+xc13,1700+yc13),
(2000+xc14,1700+yc14),(2000+xc15,1700+yc15),(2000+xc16,1700+yc16),(2000+px2,1700+py2),(2000+xc17,1700+yc17),(2000+xc18,1700+yc18),(2000+xc19,1700+yc19),
(2000+xc20,1700+yc20),(2000+xc21,1700+yc21),(2000+xc22,1700+yc22),(2000+xc23,1700+yc23),(2000+xc24,1700+yc24),(2000+xc25,1700+yc25),(2000+xc26,1700+yc26),
(2000+xc27,1700+yc27),(2000+xc28,1700+yc28),(2000+xc29,1700+yc29),(2000+xc30,1700+yc30),(2000+xc31,1700+yc31),(2000+xc32,1700+yc32),(2000+xc33,1700+yc33),
(2000+xc34,1700+yc34),(2000+xc35,1700+yc35)]

list01=[(2000+px1,2500+py1),(2000+xc1,2500+yc1),(2000+xc2,2500+yc2),(2000+xc3,2500+yc3),(2000+xc4,2500+yc4),(2000+xc5,2500+yc5),(2000+xc6,2500+yc6),
(2000+xc7,2500+yc7),(2000+xc8,2500+yc8),(2000+xc9,2500+yc9),(2000+xc10,2500+yc10),(2000+xc11,2500+yc11),(2000+xc12,2500+yc12),(2000+xc13,2500+yc13),
(2000+xc14,2500+yc14),(2000+xc15,2500+yc15),(2000+xc16,2500+yc16),(2000+px2,2500+py2),(2000+xc17,2500+yc17),(2000+xc18,2500+yc18),(2000+xc19,2500+yc19),
(2000+xc20,2500+yc20),(2000+xc21,2500+yc21),(2000+xc22,2500+yc22),(2000+xc23,2500+yc23),(2000+xc24,2500+yc24),(2000+xc25,2500+yc25),(2000+xc26,2500+yc26),
(2000+xc27,2500+yc27),(2000+xc28,2500+yc28),(2000+xc29,2500+yc29),(2000+xc30,2500+yc30),(2000+xc31,2500+yc31),(2000+xc32,2500+yc32),(2000+xc33,2500+yc33),
(2000+xc34,2500+yc34),(2000+xc35,2500+yc35)]
# print("******")
# print(len(list1))

img=cv2.line(img, list1[0], list1[1], (0,255,0), 8)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 8)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 8)
img=cv2.line(img, list1[3], list1[4], (0,255,0), 8)
img=cv2.line(img, list1[4], list1[5], (0,255,0), 8)
img=cv2.line(img, list1[5], list1[6], (0,255,0), 8)
img=cv2.line(img, list1[6], list1[7], (0,255,0), 8)
img=cv2.line(img, list1[7], list1[8], (0,255,0), 8)
img=cv2.line(img, list1[8], list1[9], (0,255,0), 8)
img=cv2.line(img, list1[9], list1[10], (0,255,0), 8)
img=cv2.line(img, list1[10], list1[11], (0,255,0), 8)
img=cv2.line(img, list1[11], list1[12], (0,255,0), 8)
img=cv2.line(img, list1[12], list1[13], (0,255,0), 8)
img=cv2.line(img, list1[13], list1[14], (0,255,0), 8)
img=cv2.line(img, list1[14], list1[15], (0,255,0), 8)
img=cv2.line(img, list1[15], list1[16], (0,255,0), 8)
img=cv2.line(img, list1[16], list1[17], (0,255,0), 8)
img=cv2.line(img, list1[17], list1[18], (0,255,0), 8)
img=cv2.line(img, list1[18], list1[19], (0,255,0), 8)
img=cv2.line(img, list1[19], list1[20], (0,255,0), 8)
img=cv2.line(img, list1[20], list1[21], (0,255,0), 8)
img=cv2.line(img, list1[21], list1[22], (0,255,0), 8)
img=cv2.line(img, list1[22], list1[23], (0,255,0), 8)
img=cv2.line(img, list1[23], list1[24], (0,255,0), 8)
img=cv2.line(img, list1[24], list1[25], (0,255,0), 8)
img=cv2.line(img, list1[25], list1[26], (0,255,0), 8)
img=cv2.line(img, list1[26], list1[27], (0,255,0), 8)
img=cv2.line(img, list1[27], list1[28], (0,255,0), 8)
img=cv2.line(img, list1[28], list1[29], (0,255,0), 8)
img=cv2.line(img, list1[29], list1[30], (0,255,0), 8)
img=cv2.line(img, list1[30], list1[31], (0,255,0), 8)
img=cv2.line(img, list1[31], list1[32], (0,255,0), 8)
img=cv2.line(img, list1[32], list1[33], (0,255,0), 8)
img=cv2.line(img, list1[33], list1[34], (0,255,0), 8)
img=cv2.line(img, list1[34], list1[35], (0,255,0), 8)
img=cv2.line(img, list1[35], list1[36], (0,255,0), 8)
img=cv2.line(img, list1[36], list1[0], (0,255,0), 8)

img=cv2.line(img, list01[0], list01[1], (0,255,0), 8)
img=cv2.line(img, list01[1], list01[2], (0,255,0), 8)
img=cv2.line(img, list01[2], list01[3], (0,255,0), 8)
img=cv2.line(img, list01[3], list01[4], (0,255,0), 8)
img=cv2.line(img, list01[4], list01[5], (0,255,0), 8)
img=cv2.line(img, list01[5], list01[6], (0,255,0), 8)
img=cv2.line(img, list01[6], list01[7], (0,255,0), 8)
img=cv2.line(img, list01[7], list01[8], (0,255,0), 8)
img=cv2.line(img, list01[8], list01[9], (0,255,0), 8)
img=cv2.line(img, list01[9], list01[10], (0,255,0), 8)
img=cv2.line(img, list01[10], list01[11], (0,255,0), 8)
img=cv2.line(img, list01[11], list01[12], (0,255,0), 8)
img=cv2.line(img, list01[12], list01[13], (0,255,0), 8)
img=cv2.line(img, list01[13], list01[14], (0,255,0), 8)
img=cv2.line(img, list01[14], list01[15], (0,255,0), 8)
img=cv2.line(img, list01[15], list01[16], (0,255,0), 8)
img=cv2.line(img, list01[16], list01[17], (0,255,0), 8)
img=cv2.line(img, list01[17], list01[18], (0,255,0), 8)
img=cv2.line(img, list01[18], list01[19], (0,255,0), 8)
img=cv2.line(img, list01[19], list01[20], (0,255,0), 8)
img=cv2.line(img, list01[20], list01[21], (0,255,0), 8)
img=cv2.line(img, list01[21], list01[22], (0,255,0), 8)
img=cv2.line(img, list01[22], list01[23], (0,255,0), 8)
img=cv2.line(img, list01[23], list01[24], (0,255,0), 8)
img=cv2.line(img, list01[24], list01[25], (0,255,0), 8)
img=cv2.line(img, list01[25], list01[26], (0,255,0), 8)
img=cv2.line(img, list01[26], list01[27], (0,255,0), 8)
img=cv2.line(img, list01[27], list01[28], (0,255,0), 8)
img=cv2.line(img, list01[28], list01[29], (0,255,0), 8)
img=cv2.line(img, list01[29], list01[30], (0,255,0), 8)
img=cv2.line(img, list01[30], list01[31], (0,255,0), 8)
img=cv2.line(img, list01[31], list01[32], (0,255,0), 8)
img=cv2.line(img, list01[32], list01[33], (0,255,0), 8)
img=cv2.line(img, list01[33], list01[34], (0,255,0), 8)
img=cv2.line(img, list01[34], list01[35], (0,255,0), 8)
img=cv2.line(img, list01[35], list01[36], (0,255,0), 8)
img=cv2.line(img, list01[36], list01[0], (0,255,0), 8)

l0=(float(d1['h2'])-float(d1['h0']))/2
l1=(float(d1['h2'])-float(d1['h4']))/2

c1=math.ceil(p*l0)
c2=math.ceil(p*d1['h0'])
c3=math.ceil(p*d1['h3'])
c4=math.ceil(p*d1['h2'])
c5=math.ceil(p*d1['h4'])
c6=math.ceil(p*l1)
c7=math.ceil(p*d1['h1'])

list2=[(2050+c1,600+0),(2050+c1+c2,600+0),(2050+c4,600+c7),(2050+c5+c6,600+c3+c7),(2050+c6,600+c3+c7),(2050+0,600+c7)]

img=cv2.line(img, list2[0], list2[1], (0,255,0), 8)
img=cv2.line(img, list2[1], list2[2], (0,255,0), 8)
img=cv2.line(img, list2[2], list2[3], (0,255,0), 8)
img=cv2.line(img, list2[3], list2[4], (0,255,0), 8)
img=cv2.line(img, list2[4], list2[5], (0,255,0), 8)
img=cv2.line(img, list2[5], list2[0], (0,255,0), 8)


x1=math.ceil(p*d2['b'])
y1=math.ceil(p*d2['h'])
px1=math.ceil(p*d2['xp1'])
px2=math.ceil(p*d2['xp2'])
px3=math.ceil(p*d2['xp3'])
px4=math.ceil(p*d2['xp4'])
px5=math.ceil(p*d2['xp5'])
px6=math.ceil(p*d2['xp6'])

py1=math.ceil(p*d2['yp1'])
py2=math.ceil(p*d2['yp2'])
py3=math.ceil(p*d2['yp3'])
py4=math.ceil(p*d2['yp4'])
py5=math.ceil(p*d2['yp5'])
py6=math.ceil(p*d2['yp6'])

xc1=math.ceil(p*d2['cx1'])
xc2=math.ceil(p*d2['cx2'])
xc3=math.ceil(p*d2['cx3'])
xc4=math.ceil(p*d2['cx4'])
xc5=math.ceil(p*d2['cx5'])
xc6=math.ceil(p*d2['cx6'])
xc7=math.ceil(p*d2['cx7'])
xc8=math.ceil(p*d2['cx8'])
xc9=math.ceil(p*d2['cx9'])
xc10=math.ceil(p*d2['cx10'])
xc11=math.ceil(p*d2['cx11'])
xc12=math.ceil(p*d2['cx12'])
xc13=math.ceil(p*d2['cx13'])
xc14=math.ceil(p*d2['cx14'])
xc15=math.ceil(p*d2['cx15'])
xc16=math.ceil(p*d2['cx16'])
xc17=math.ceil(p*d2['cx17'])
xc18=math.ceil(p*d2['cx18'])
xc19=math.ceil(p*d2['cx19'])
xc20=math.ceil(p*d2['cx20'])
xc21=math.ceil(p*d2['cx21'])
xc22=math.ceil(p*d2['cx22'])
xc23=math.ceil(p*d2['cx23'])
xc24=math.ceil(p*d2['cx24'])
xc25=math.ceil(p*d2['cx25'])
xc26=math.ceil(p*d2['cx26'])
xc27=math.ceil(p*d2['cx27'])
xc28=math.ceil(p*d2['cx28'])
xc29=math.ceil(p*d2['cx29'])
xc30=math.ceil(p*d2['cx30'])
xc31=math.ceil(p*d2['cx31'])
xc32=math.ceil(p*d2['cx32'])
xc33=math.ceil(p*d2['cx33'])

yc1=math.ceil(p*d2['cy1'])
yc2=math.ceil(p*d2['cy2'])
yc3=math.ceil(p*d2['cy3'])
yc4=math.ceil(p*d2['cy4'])
yc5=math.ceil(p*d2['cy5'])
yc6=math.ceil(p*d2['cy6'])
yc7=math.ceil(p*d2['cy7'])
yc8=math.ceil(p*d2['cy8'])
yc9=math.ceil(p*d2['cy9'])
yc10=math.ceil(p*d2['cy10'])
yc11=math.ceil(p*d2['cy11'])
yc12=math.ceil(p*d2['cy12'])
yc13=math.ceil(p*d2['cy13'])
yc14=math.ceil(p*d2['cy14'])
yc15=math.ceil(p*d2['cy15'])
yc16=math.ceil(p*d2['cy16'])
yc17=math.ceil(p*d2['cy17'])
yc18=math.ceil(p*d2['cy18'])
yc19=math.ceil(p*d2['cy19'])
yc20=math.ceil(p*d2['cy20'])
yc21=math.ceil(p*d2['cy21'])
yc22=math.ceil(p*d2['cy22'])
yc23=math.ceil(p*d2['cy23'])
yc24=math.ceil(p*d2['cy24'])
yc25=math.ceil(p*d2['cy25'])
yc26=math.ceil(p*d2['cy26'])
yc27=math.ceil(p*d2['cy27'])
yc28=math.ceil(p*d2['cy28'])
yc29=math.ceil(p*d2['cy29'])
yc30=math.ceil(p*d2['cy30'])
yc31=math.ceil(p*d2['cy31'])
yc32=math.ceil(p*d2['cy32'])
yc33=math.ceil(p*d2['cy33'])

list3=[(700+px1,600+py1),(700+px2,600+py2),(700+xc1,600+yc1),(700+xc2,600+yc2),(700+xc3,600+yc3),(700+xc4,600+yc4),
(700+xc5,600+yc5),(700+xc6,600+yc6),(700+xc7,600+yc7),(700+xc8,600+yc8),(700+xc9,600+yc9),(700+xc10,600+yc10),
(700+xc11,600+yc11),(700+xc12,600+yc12),(700+0,600+py3),(700+0,600+py3+y1),(700+x1,600+py3+y1),(700+x1,600+py6),
(700+xc24,600+yc24),(700+xc23,600+yc23),(700+xc22,600+yc22),(700+xc21,600+yc21),(700+xc20,600+yc20),(700+xc19,600+yc19),
(700+xc18,600+yc18),(700+xc17,600+yc17),(700+xc16,600+yc16),(700+xc15,600+yc15),(700+xc14,600+yc14),(700+xc13,600+yc13),
(700+px5,600+py5),(700+px4,600+py4),(700+xc33,600+yc33),(700+xc32,600+yc32),(700+xc31,600+yc31),(700+xc30,600+yc30),
(700+xc29,600+yc29),(700+xc28,600+yc28),(700+xc27,600+yc27),(700+xc26,600+yc26),(700+xc25,600+yc25)]
# print("******")
# print(len(list3))

img=cv2.line(img, list3[0], list3[1], (0,255,0), 8)
img=cv2.line(img, list3[1], list3[2], (0,255,0), 8)
img=cv2.line(img, list3[2], list3[3], (0,255,0), 8)
img=cv2.line(img, list3[3], list3[4], (0,255,0), 8)
img=cv2.line(img, list3[4], list3[5], (0,255,0), 8)
img=cv2.line(img, list3[5], list3[6], (0,255,0), 8)
img=cv2.line(img, list3[6], list3[7], (0,255,0), 8)
img=cv2.line(img, list3[7], list3[8], (0,255,0), 8)
img=cv2.line(img, list3[8], list3[9], (0,255,0), 8)
img=cv2.line(img, list3[9], list3[10], (0,255,0), 8)
img=cv2.line(img, list3[10], list3[11], (0,255,0), 8)
img=cv2.line(img, list3[11], list3[12], (0,255,0), 8)
img=cv2.line(img, list3[12], list3[13], (0,255,0), 8)
img=cv2.line(img, list3[13], list3[14], (0,255,0), 8)
img=cv2.line(img, list3[14], list3[15], (0,255,0), 8)
img=cv2.line(img, list3[15], list3[16], (0,255,0), 8)
img=cv2.line(img, list3[16], list3[17], (0,255,0), 8)
img=cv2.line(img, list3[17], list3[18], (0,255,0), 8)
img=cv2.line(img, list3[18], list3[19], (0,255,0), 8)
img=cv2.line(img, list3[19], list3[20], (0,255,0), 8)
img=cv2.line(img, list3[20], list3[21], (0,255,0), 8)
img=cv2.line(img, list3[21], list3[22], (0,255,0), 8)
img=cv2.line(img, list3[22], list3[23], (0,255,0), 8)
img=cv2.line(img, list3[23], list3[24], (0,255,0), 8)
img=cv2.line(img, list3[24], list3[25], (0,255,0), 8)
img=cv2.line(img, list3[25], list3[26], (0,255,0), 8)
img=cv2.line(img, list3[26], list3[27], (0,255,0), 8)
img=cv2.line(img, list3[27], list3[28], (0,255,0), 8)
img=cv2.line(img, list3[28], list3[29], (0,255,0), 8)
img=cv2.line(img, list3[29], list3[30], (0,255,0), 8)
img=cv2.line(img, list3[30], list3[31], (0,255,0), 8)
img=cv2.line(img, list3[31], list3[32], (0,255,0), 8)
img=cv2.line(img, list3[32], list3[33], (0,255,0), 8)
img=cv2.line(img, list3[33], list3[34], (0,255,0), 8)
img=cv2.line(img, list3[34], list3[35], (0,255,0), 8)
img=cv2.line(img, list3[35], list3[36], (0,255,0), 8)
img=cv2.line(img, list3[36], list3[37], (0,255,0), 8)
img=cv2.line(img, list3[37], list3[38], (0,255,0), 8)
img=cv2.line(img, list3[38], list3[39], (0,255,0), 8)
img=cv2.line(img, list3[39], list3[40], (0,255,0), 8)
img=cv2.line(img, list3[40], list3[0], (0,255,0), 8)
# img=cv2.line(img, list3[41], list3[0], (0,255,0), 8)

x1=math.ceil(p*d3['b'])
y1=math.ceil(p*d3['h'])
y2=math.ceil(p*d3['s'])
px1=math.ceil(p*d3['xp1'])
px2=math.ceil(p*d3['xp2'])
px3=math.ceil(p*d3['xp3'])
px4=math.ceil(p*d3['xp4'])

py1=math.ceil(p*d3['yp1'])
py2=math.ceil(p*d3['yp2'])
py3=math.ceil(p*d3['yp3'])
py4=math.ceil(p*d3['yp4'])

xc1=math.ceil(p*d3['cx1'])
xc2=math.ceil(p*d3['cx2'])
xc3=math.ceil(p*d3['cx3'])
xc4=math.ceil(p*d3['cx4'])
xc5=math.ceil(p*d3['cx5'])
xc6=math.ceil(p*d3['cx6'])
xc7=math.ceil(p*d3['cx7'])
xc8=math.ceil(p*d3['cx8'])
xc9=math.ceil(p*d3['cx9'])
xc10=math.ceil(p*d3['cx10'])
xc11=math.ceil(p*d3['cx11'])
xc12=math.ceil(p*d3['cx12'])
xc13=math.ceil(p*d3['cx13'])
xc14=math.ceil(p*d3['cx14'])

yc1=math.ceil(p*d3['cy1'])
yc2=math.ceil(p*d3['cy2'])
yc3=math.ceil(p*d3['cy3'])
yc4=math.ceil(p*d3['cy4'])
yc5=math.ceil(p*d3['cy5'])
yc6=math.ceil(p*d3['cy6'])
yc7=math.ceil(p*d3['cy7'])
yc8=math.ceil(p*d3['cy8'])
yc9=math.ceil(p*d3['cy9'])
yc10=math.ceil(p*d3['cy10'])
yc11=math.ceil(p*d3['cy11'])
yc12=math.ceil(p*d3['cy12'])
yc13=math.ceil(p*d3['cy13'])
yc14=math.ceil(p*d3['cy14'])

list4=[(650+px1,2000+py1),(650+px2,2000+py2),(650+xc1,2000+yc1),(650+xc2,2000+yc2),(650+xc3,2000+yc3),(650+xc4,2000+yc4),(650+xc5,2000+yc5),
(650+xc6,2000+yc6),(650+xc7,2000+yc7),(650+xc8,2000+yc8),(650+xc9,2000+yc9),(650+xc10,2000+yc10),(650+px3,2000+py3),(650+0,2000+py3+y2),(650+x1,2000+py3+y2),
(650+x1,2000+py4),(650+xc11,2000+yc11),(650+xc12,2000+yc12),(650+xc13,2000+yc13),(650+xc14,2000+yc14)]


list04=[(1280+px1,2000+py1),(1280+px2,2000+py2),(1280+xc1,2000+yc1),(1280+xc2,2000+yc2),(1280+xc3,2000+yc3),(1280+xc4,2000+yc4),(1280+xc5,2000+yc5),
(1280+xc6,2000+yc6),(1280+xc7,2000+yc7),(1280+xc8,2000+yc8),(1280+xc9,2000+yc9),(1280+xc10,2000+yc10),(1280+px3,2000+py3),(1280+0,2000+py3+y2),(1280+x1,2000+py3+y2),
(1280+x1,2000+py4),(1280+xc11,2000+yc11),(1280+xc12,2000+yc12),(1280+xc13,2000+yc13),(1280+xc14,2000+yc14)]
# print("******:list3")
# print(len(list4))

img=cv2.line(img, list4[0], list4[1], (0,255,0), 8)
img=cv2.line(img, list4[1], list4[2], (0,255,0), 8)
img=cv2.line(img, list4[2], list4[3], (0,255,0), 8)
img=cv2.line(img, list4[3], list4[4], (0,255,0), 8)
img=cv2.line(img, list4[4], list4[5], (0,255,0), 8)
img=cv2.line(img, list4[5], list4[6], (0,255,0), 8)
img=cv2.line(img, list4[6], list4[7], (0,255,0), 8)
img=cv2.line(img, list4[7], list4[8], (0,255,0), 8)
img=cv2.line(img, list4[8], list4[9], (0,255,0), 8)
img=cv2.line(img, list4[9], list4[10], (0,255,0), 8)
img=cv2.line(img, list4[10], list4[11], (0,255,0), 8)
img=cv2.line(img, list4[11], list4[12], (0,255,0), 8)
img=cv2.line(img, list4[12], list4[13], (0,255,0), 8)
img=cv2.line(img, list4[13], list4[14], (0,255,0), 8)
img=cv2.line(img, list4[14], list4[15], (0,255,0), 8)
img=cv2.line(img, list4[15], list4[16], (0,255,0), 8)
img=cv2.line(img, list4[16], list4[17], (0,255,0), 8)
img=cv2.line(img, list4[17], list4[18], (0,255,0), 8)
img=cv2.line(img, list4[18], list4[19], (0,255,0), 8)
img=cv2.line(img, list4[19], list4[0], (0,255,0), 8)



img=cv2.line(img, list04[0], list04[1], (0,255,0), 8)
img=cv2.line(img, list04[1], list04[2], (0,255,0), 8)
img=cv2.line(img, list04[2], list04[3], (0,255,0), 8)
img=cv2.line(img, list04[3], list04[4], (0,255,0), 8)
img=cv2.line(img, list04[4], list04[5], (0,255,0), 8)
img=cv2.line(img, list04[5], list04[6], (0,255,0), 8)
img=cv2.line(img, list04[6], list04[7], (0,255,0), 8)
img=cv2.line(img, list04[7], list04[8], (0,255,0), 8)
img=cv2.line(img, list04[8], list04[9], (0,255,0), 8)
img=cv2.line(img, list04[9], list04[10], (0,255,0), 8)
img=cv2.line(img, list04[10], list04[11], (0,255,0), 8)
img=cv2.line(img, list04[11], list04[12], (0,255,0), 8)
img=cv2.line(img, list04[12], list04[13], (0,255,0), 8)
img=cv2.line(img, list04[13], list04[14], (0,255,0), 8)
img=cv2.line(img, list04[14], list04[15], (0,255,0), 8)
img=cv2.line(img, list04[15], list04[16], (0,255,0), 8)
img=cv2.line(img, list04[16], list04[17], (0,255,0), 8)
img=cv2.line(img, list04[17], list04[18], (0,255,0), 8)
img=cv2.line(img, list04[18], list04[19], (0,255,0), 8)
img=cv2.line(img, list04[19], list04[0], (0,255,0), 8)

# img=cv2.line(img, list4[20], list4[0], (0,255,0), 8)

# img=cv2.line(img, list1[37], list1[38], (0,255,0), 8)
# img=cv2.line(img, list1[38], list1[39], (0,255,0), 8)
# img=cv2.line(img, list1[39], list1[40], (0,255,0), 8)
# img=cv2.line(img, list1[40], list1[41], (0,255,0), 8)
# img=cv2.line(img, list1[41], list1[42], (0,255,0), 8)
# img=cv2.line(img, list1[42], list1[43], (0,255,0), 8)
# img=cv2.line(img, list1[43], list1[44], (0,255,0), 8)
# img=cv2.line(img, list1[44], list1[45], (0,255,0), 8)
# img=cv2.line(img, list1[45], list1[46], (0,255,0), 8)
# img=cv2.line(img, list1[46], list1[47], (0,255,0), 8)
# img=cv2.line(img, list1[47], list1[48], (0,255,0), 8)
# img=cv2.line(img, list1[48], list1[49], (0,255,0), 8)
# img=cv2.line(img, list1[49], list1[50], (0,255,0), 8)
# img=cv2.line(img, list1[50], list1[51], (0,255,0), 8)
# img=cv2.line(img, list1[51], list1[52], (0,255,0), 8)
# img=cv2.line(img, list1[52], list1[53], (0,255,0), 8)
# img=cv2.line(img, list1[53], list1[54], (0,255,0), 8)
# img=cv2.line(img, list1[54], list1[0], (0,255,0), 8)

cv2.imshow('no-coin-1.jpg', img)
# cv2.imwrite("IMG_5438-f.jpg",img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

