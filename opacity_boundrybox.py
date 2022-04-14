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
import os, glob, requests
import random
import urllib

image_url = 'https://ik.imagekit.io/2360uyb96/duplo-dsphere-beta/preview/41f1e7e2-d304-454d-ab07-a16e3a628eae'
req = urllib.request.urlopen(image_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)


# img = cv2.imread("testimage_1.jpeg")
f = open('dh-tshirt-panel.json')
data = json.load(f)
point=data["xs"]["f"]["fb1"]

pixelsPerMetric=28


xcp1=math.ceil(pixelsPerMetric*point['xp1'])
xcp2=math.ceil(pixelsPerMetric*point['xp2'])

ycp1=math.ceil(pixelsPerMetric*point['yp1'])
ycp2=math.ceil(pixelsPerMetric*point['yp2'])


c1=math.ceil(pixelsPerMetric*point['h'])
c2=math.ceil(pixelsPerMetric*point['b'])

ccx1=math.ceil(point['cx1']*pixelsPerMetric)
ccx2=math.ceil(point['cx2']*pixelsPerMetric)
ccx3=math.ceil(point['cx3']*pixelsPerMetric)
ccx4=math.ceil(point['cx4']*pixelsPerMetric)
ccx5=math.ceil(point['cx5']*pixelsPerMetric)
ccx6=math.ceil(point['cx6']*pixelsPerMetric)
ccx7=math.ceil(point['cx7']*pixelsPerMetric)
ccx8=math.ceil(point['cx8']*pixelsPerMetric)
ccx9=math.ceil(point['cx9']*pixelsPerMetric)
ccx10=math.ceil(point['cx10']*pixelsPerMetric)
ccx11=math.ceil(point['cx11']*pixelsPerMetric)
ccx12=math.ceil(point['cx12']*pixelsPerMetric)
ccx13=math.ceil(point['cx13']*pixelsPerMetric)
ccx14=math.ceil(point['cx14']*pixelsPerMetric)
ccx15=math.ceil(point['cx15']*pixelsPerMetric)
ccx16=math.ceil(point['cx16']*pixelsPerMetric)
ccx17=math.ceil(point['cx17']*pixelsPerMetric)
ccx18=math.ceil(point['cx18']*pixelsPerMetric)
ccx19=math.ceil(point['cx19']*pixelsPerMetric)
ccx20=math.ceil(point['cx20']*pixelsPerMetric)
ccx21=math.ceil(point['cx21']*pixelsPerMetric)

ccy1=math.ceil(point['cy1']*pixelsPerMetric)
ccy2=math.ceil(point['cy2']*pixelsPerMetric)
ccy3=math.ceil(point['cy3']*pixelsPerMetric)
ccy4=math.ceil(point['cy4']*pixelsPerMetric)
ccy5=math.ceil(point['cy5']*pixelsPerMetric)
ccy6=math.ceil(point['cy6']*pixelsPerMetric)
ccy7=math.ceil(point['cy7']*pixelsPerMetric)
ccy8=math.ceil(point['cy8']*pixelsPerMetric)
ccy9=math.ceil(point['cy9']*pixelsPerMetric)
ccy10=math.ceil(point['cy10']*pixelsPerMetric)
ccy11=math.ceil(point['cy11']*pixelsPerMetric)
ccy12=math.ceil(point['cy12']*pixelsPerMetric)
ccy13=math.ceil(point['cy13']*pixelsPerMetric)
ccy14=math.ceil(point['cy14']*pixelsPerMetric)
ccy15=math.ceil(point['cy15']*pixelsPerMetric)
ccy16=math.ceil(point['cy16']*pixelsPerMetric)
ccy17=math.ceil(point['cy17']*pixelsPerMetric)
ccy18=math.ceil(point['cy18']*pixelsPerMetric)
ccy19=math.ceil(point['cy19']*pixelsPerMetric)
ccy20=math.ceil(point['cy20']*pixelsPerMetric)
ccy21=math.ceil(point['cy21']*pixelsPerMetric)



contours = [ np.array([[320+0,110+0],[320+xcp2, 110+ycp2],[320+c2,110+c1],[320+ccx21, 110+ccy21],[320+ccx20, 110+ccy20],[320+ccx19, 110+ccy19],[320+ccx18, 110+ccy18],[320+ccx17, 110+ccy17],[320+ccx16, 110+ccy16],
                    [320+ccx15, 110+ccy15],[320+ccx14, 110+ccy14],[320+ccx13, 110+ccy13],[320+ccx12, 110+ccy12],[320+ccx11, 110+ccy11],[320+ccx10, 110+ccy10],[320+ccx9, 110+ccy9],[320+ccx8, 110+ccy8],[320+ccx7, 110+ccy7],
                    [320+ccx6, 110+ccy6],[320+ccx5, 110+ccy5],[320+ccx4, 110+ccy4],[320+ccx3, 110+ccy3],[320+ccx2, 110+ccy2],[320+ccx1, 110+ccy1],[320+xcp1, 110+ycp1],[320+0,110+0]])
           ]

point=data["xs"]["f"]["fb2"]

xcp1=math.ceil(point['xp1']*pixelsPerMetric)
xcp2=math.ceil(point['xp2']*pixelsPerMetric)
xcp3=math.ceil(point['xp3']*pixelsPerMetric)

ycp1=math.ceil(point['yp1']*pixelsPerMetric)
ycp2=math.ceil(point['yp2']*pixelsPerMetric)
ycp3=math.ceil(point['yp3']*pixelsPerMetric)


c1=math.ceil(point['h']*pixelsPerMetric)
c2=math.ceil(point['b']*pixelsPerMetric)


ccx1=math.ceil(point['cx1']*pixelsPerMetric)
ccx2=math.ceil(point['cx2']*pixelsPerMetric)
ccx3=math.ceil(point['cx3']*pixelsPerMetric)
ccx4=math.ceil(point['cx4']*pixelsPerMetric)
ccx5=math.ceil(point['cx5']*pixelsPerMetric)
ccx6=math.ceil(point['cx6']*pixelsPerMetric)
ccx7=math.ceil(point['cx7']*pixelsPerMetric)
ccx8=math.ceil(point['cx8']*pixelsPerMetric)
ccx9=math.ceil(point['cx9']*pixelsPerMetric)
ccx10=math.ceil(point['cx10']*pixelsPerMetric)
ccx11=math.ceil(point['cx11']*pixelsPerMetric)
ccx12=math.ceil(point['cx12']*pixelsPerMetric)
ccx13=math.ceil(point['cx13']*pixelsPerMetric)
ccx14=math.ceil(point['cx14']*pixelsPerMetric)
ccx15=math.ceil(point['cx15']*pixelsPerMetric)
ccx16=math.ceil(point['cx16']*pixelsPerMetric)
ccx17=math.ceil(point['cx17']*pixelsPerMetric)
ccx18=math.ceil(point['cx18']*pixelsPerMetric)
ccx19=math.ceil(point['cx19']*pixelsPerMetric)
ccx20=math.ceil(point['cx20']*pixelsPerMetric)
ccx21=math.ceil(point['cx21']*pixelsPerMetric)
ccx22=math.ceil(point['cx22']*pixelsPerMetric)
ccx23=math.ceil(point['cx23']*pixelsPerMetric)
ccx24=math.ceil(point['cx24']*pixelsPerMetric)
ccx25=math.ceil(point['cx25']*pixelsPerMetric)
ccx26=math.ceil(point['cx26']*pixelsPerMetric)
ccx27=math.ceil(point['cx27']*pixelsPerMetric)
ccx28=math.ceil(point['cx28']*pixelsPerMetric)
ccx29=math.ceil(point['cx29']*pixelsPerMetric)
ccx30=math.ceil(point['cx30']*pixelsPerMetric)
ccx31=math.ceil(point['cx31']*pixelsPerMetric)
ccx32=math.ceil(point['cx32']*pixelsPerMetric)
ccx33=math.ceil(point['cx33']*pixelsPerMetric)
ccx34=math.ceil(point['cx34']*pixelsPerMetric)
ccx35=math.ceil(point['cx35']*pixelsPerMetric)
ccx36=math.ceil(point['cx36']*pixelsPerMetric)
ccx37=math.ceil(point['cx37']*pixelsPerMetric)
ccx38=math.ceil(point['cx38']*pixelsPerMetric)
ccx39=math.ceil(point['cx39']*pixelsPerMetric)
ccx40=math.ceil(point['cx40']*pixelsPerMetric)
ccx41=math.ceil(point['cx41']*pixelsPerMetric)
ccx42=math.ceil(point['cx42']*pixelsPerMetric)
ccx43=math.ceil(point['cx43']*pixelsPerMetric)
ccx44=math.ceil(point['cx44']*pixelsPerMetric)
ccx45=math.ceil(point['cx45']*pixelsPerMetric)
ccx46=math.ceil(point['cx46']*pixelsPerMetric)
ccx47=math.ceil(point['cx47']*pixelsPerMetric)
ccx48=math.ceil(point['cx48']*pixelsPerMetric)
ccx49=math.ceil(point['cx49']*pixelsPerMetric)
ccx50=math.ceil(point['cx50']*pixelsPerMetric)


ccy1=math.ceil(point['cy1']*pixelsPerMetric)
ccy2=math.ceil(point['cy2']*pixelsPerMetric)
ccy3=math.ceil(point['cy3']*pixelsPerMetric)
ccy4=math.ceil(point['cy4']*pixelsPerMetric)
ccy5=math.ceil(point['cy5']*pixelsPerMetric)
ccy6=math.ceil(point['cy6']*pixelsPerMetric)
ccy7=math.ceil(point['cy7']*pixelsPerMetric)
ccy8=math.ceil(point['cy8']*pixelsPerMetric)
ccy9=math.ceil(point['cy9']*pixelsPerMetric)
ccy10=math.ceil(point['cy10']*pixelsPerMetric)
ccy11=math.ceil(point['cy11']*pixelsPerMetric)
ccy12=math.ceil(point['cy12']*pixelsPerMetric)
ccy13=math.ceil(point['cy13']*pixelsPerMetric)
ccy14=math.ceil(point['cy14']*pixelsPerMetric)
ccy15=math.ceil(point['cy15']*pixelsPerMetric)
ccy16=math.ceil(point['cy16']*pixelsPerMetric)
ccy17=math.ceil(point['cy17']*pixelsPerMetric)
ccy18=math.ceil(point['cy18']*pixelsPerMetric)
ccy19=math.ceil(point['cy19']*pixelsPerMetric)
ccy20=math.ceil(point['cy20']*pixelsPerMetric)
ccy21=math.ceil(point['cy21']*pixelsPerMetric)
ccy22=math.ceil(point['cy22']*pixelsPerMetric)
ccy23=math.ceil(point['cy23']*pixelsPerMetric)
ccy24=math.ceil(point['cy24']*pixelsPerMetric)
ccy25=math.ceil(point['cy25']*pixelsPerMetric)
ccy26=math.ceil(point['cy26']*pixelsPerMetric)
ccy27=math.ceil(point['cy27']*pixelsPerMetric)
ccy28=math.ceil(point['cy28']*pixelsPerMetric)
ccy29=math.ceil(point['cy29']*pixelsPerMetric)
ccy30=math.ceil(point['cy30']*pixelsPerMetric)
ccy31=math.ceil(point['cy31']*pixelsPerMetric)
ccy32=math.ceil(point['cy32']*pixelsPerMetric)
ccy33=math.ceil(point['cy33']*pixelsPerMetric)
ccy34=math.ceil(point['cy34']*pixelsPerMetric)
ccy35=math.ceil(point['cy35']*pixelsPerMetric)
ccy36=math.ceil(point['cy36']*pixelsPerMetric)
ccy37=math.ceil(point['cy37']*pixelsPerMetric)
ccy38=math.ceil(point['cy38']*pixelsPerMetric)
ccy39=math.ceil(point['cy39']*pixelsPerMetric)
ccy40=math.ceil(point['cy40']*pixelsPerMetric)
ccy41=math.ceil(point['cy41']*pixelsPerMetric)
ccy42=math.ceil(point['cy42']*pixelsPerMetric)
ccy43=math.ceil(point['cy43']*pixelsPerMetric)
ccy44=math.ceil(point['cy44']*pixelsPerMetric)
ccy45=math.ceil(point['cy45']*pixelsPerMetric)
ccy46=math.ceil(point['cy46']*pixelsPerMetric)
ccy47=math.ceil(point['cy47']*pixelsPerMetric)
ccy48=math.ceil(point['cy48']*pixelsPerMetric)
ccy49=math.ceil(point['cy49']*pixelsPerMetric)
ccy50=math.ceil(point['cy50']*pixelsPerMetric)

contours2 = [ np.array(
    [(540+xcp1,150+0),(540+0,150+c1),(540+c2,150+c1),(540+ccx50,150+ccy50),(540+ccx49,150+ccy49),(540+ccx48,150+ccy48),
(540+ccx47,150+ccy47),(540+ccx46,150+ccy46),(540+ccx45,150+ccy45),(540+ccx44,150+ccy44),(540+ccx43,150+ccy43),(540+ccx42,150+ccy42),(540+ccx41,150+ccy41),
(540+ccx40,150+ccy40), (540+ccx39,150+ccy39),(540+ccx38,150+ccy38),(540+ccx37,150+ccy37),(540+ccx36,150+ccy36),(540+ccx35,150+ccy35),(540+ccx34,150+ccy34),
(540+ccx33,150+ccy33),(540+ccx32,150+ccy32),(540+ccx31,150+ccy31),(540+xcp3,150+ycp3),(540+xcp2,150+ycp2),(540+ccx30,150+ccy30), (540+ccx29,150+ccy29),
(540+ccx28,150+ccy28),(540+ccx27,150+ccy27),(540+ccx26,150+ccy26),(540+ccx25,150+ccy25),(540+ccx24,150+ccy24),(540+ccx23,150+ccy23),(540+ccx22,150+ccy22),
(540+ccx21,150+ccy21),(540+ccx20,150+ccy20),(540+ccx19,150+ccy19),(540+ccx18,150+ccy18),(540+ccx17,150+ccy17),(540+ccx16,150+ccy16),(540+ccx15,150+ccy15),
(540+ccx14,150+ccy14),(540+ccx13,150+ccy13),(540+ccx12,150+ccy12),(540+ccx11,150+ccy11),(540+ccx10,150+ccy10), (540+ccx9,150+ccy9),(540+ccx8,150+ccy8),
(540+ccx7,150+ccy7),(540+ccx6,150+ccy6),(540+ccx5,150+ccy5),(540+ccx4,150+ccy4),(540+ccx3,150+ccy3),(540+ccx2,150+ccy2),(540+ccx1,150+ccy1)]
)]

point=data["xs"]["f"]["fb3"]

x0=point['b']-point['s']
c1=math.ceil(pixelsPerMetric*point['l'])
c2=math.ceil(pixelsPerMetric*point['b'])
c3=math.ceil(pixelsPerMetric*point['s'])
c4=math.ceil(pixelsPerMetric*x0)

contours3 = [ np.array(
    [(940+0,125+0),(940+c4,125+c1),(940+c2,125+c1),(940+c2,125+0)]
)]


point=data["xs"]["f"]["tb"]
y1=math.ceil(pixelsPerMetric*point['h'])
x1=math.ceil(pixelsPerMetric*point['b'])

px1=math.ceil(pixelsPerMetric*point['xp1'])
px2=math.ceil(pixelsPerMetric*point['xp2'])
px3=math.ceil(pixelsPerMetric*point['xp3'])
px4=math.ceil(pixelsPerMetric*point['xp4'])
px5=math.ceil(pixelsPerMetric*point['xp5'])
px6=math.ceil(pixelsPerMetric*point['xp6'])

py1=math.ceil(pixelsPerMetric*point['yp1'])
py2=math.ceil(pixelsPerMetric*point['yp2'])
py3=math.ceil(pixelsPerMetric*point['yp3'])
py4=math.ceil(pixelsPerMetric*point['yp4'])
py5=math.ceil(pixelsPerMetric*point['yp5'])
py6=math.ceil(pixelsPerMetric*point['yp6'])

xc1=math.ceil(pixelsPerMetric*point['cx1'])
xc2=math.ceil(pixelsPerMetric*point['cx2'])
xc3=math.ceil(pixelsPerMetric*point['cx3'])
xc4=math.ceil(pixelsPerMetric*point['cx4'])
xc5=math.ceil(pixelsPerMetric*point['cx5'])
xc6=math.ceil(pixelsPerMetric*point['cx6'])
xc7=math.ceil(pixelsPerMetric*point['cx7'])
xc8=math.ceil(pixelsPerMetric*point['cx8'])
xc9=math.ceil(pixelsPerMetric*point['cx9'])
xc10=math.ceil(pixelsPerMetric*point['cx10'])
xc11=math.ceil(pixelsPerMetric*point['cx11'])
xc12=math.ceil(pixelsPerMetric*point['cx12'])
xc13=math.ceil(pixelsPerMetric*point['cx13'])
xc14=math.ceil(pixelsPerMetric*point['cx14'])
xc15=math.ceil(pixelsPerMetric*point['cx15'])
xc16=math.ceil(pixelsPerMetric*point['cx16'])
xc17=math.ceil(pixelsPerMetric*point['cx17'])
xc18=math.ceil(pixelsPerMetric*point['cx18'])
xc19=math.ceil(pixelsPerMetric*point['cx19'])
xc20=math.ceil(pixelsPerMetric*point['cx20'])
xc21=math.ceil(pixelsPerMetric*point['cx21'])
xc22=math.ceil(pixelsPerMetric*point['cx22'])
xc23=math.ceil(pixelsPerMetric*point['cx23'])
xc24=math.ceil(pixelsPerMetric*point['cx24'])
xc25=math.ceil(pixelsPerMetric*point['cx25'])
xc26=math.ceil(pixelsPerMetric*point['cx26'])
xc27=math.ceil(pixelsPerMetric*point['cx27'])
xc28=math.ceil(pixelsPerMetric*point['cx28'])
xc29=math.ceil(pixelsPerMetric*point['cx29'])
xc30=math.ceil(pixelsPerMetric*point['cx30'])
xc31=math.ceil(pixelsPerMetric*point['cx31'])
xc32=math.ceil(pixelsPerMetric*point['cx32'])
xc33=math.ceil(pixelsPerMetric*point['cx33'])


yc1=math.ceil(pixelsPerMetric*point['cy1'])
yc2=math.ceil(pixelsPerMetric*point['cy2'])
yc3=math.ceil(pixelsPerMetric*point['cy3'])
yc4=math.ceil(pixelsPerMetric*point['cy4'])
yc5=math.ceil(pixelsPerMetric*point['cy5'])
yc6=math.ceil(pixelsPerMetric*point['cy6'])
yc7=math.ceil(pixelsPerMetric*point['cy7'])
yc8=math.ceil(pixelsPerMetric*point['cy8'])
yc9=math.ceil(pixelsPerMetric*point['cy9'])
yc10=math.ceil(pixelsPerMetric*point['cy10'])
yc11=math.ceil(pixelsPerMetric*point['cy11'])
yc12=math.ceil(pixelsPerMetric*point['cy12'])
yc13=math.ceil(pixelsPerMetric*point['cy13'])
yc14=math.ceil(pixelsPerMetric*point['cy14'])
yc15=math.ceil(pixelsPerMetric*point['cy15'])
yc16=math.ceil(pixelsPerMetric*point['cy16'])
yc17=math.ceil(pixelsPerMetric*point['cy17'])
yc18=math.ceil(pixelsPerMetric*point['cy18'])
yc19=math.ceil(pixelsPerMetric*point['cy19'])
yc20=math.ceil(pixelsPerMetric*point['cy20'])
yc21=math.ceil(pixelsPerMetric*point['cy21'])
yc22=math.ceil(pixelsPerMetric*point['cy22'])
yc23=math.ceil(pixelsPerMetric*point['cy23'])
yc24=math.ceil(pixelsPerMetric*point['cy24'])
yc25=math.ceil(pixelsPerMetric*point['cy25'])
yc26=math.ceil(pixelsPerMetric*point['cy26'])
yc27=math.ceil(pixelsPerMetric*point['cy27'])
yc28=math.ceil(pixelsPerMetric*point['cy28'])
yc29=math.ceil(pixelsPerMetric*point['cy29'])
yc30=math.ceil(pixelsPerMetric*point['cy30'])
yc31=math.ceil(pixelsPerMetric*point['cy31'])
yc32=math.ceil(pixelsPerMetric*point['cy32'])
yc33=math.ceil(pixelsPerMetric*point['cy33'])


contours4 = [ np.array(
[(540+px1,420+py1),(540+px2,420+py2),(540+xc1,420+yc1),(540+xc2,420+yc2),(540+xc3,420+yc3),(540+xc4,420+yc4),(540+xc5,420+yc5),
(540+xc6,420+yc6),(540+xc7,420+yc7),(540+xc8,420+yc8),(540+xc9,420+yc9),(540+xc10,420+yc10),(540+xc11,420+yc11),
(540+xc12,420+yc12),(540+0,420+py3),(540+0,420+py3+y1),(540+x1,420+py3+y1),
(540+x1,420+py6),(540+xc24,420+yc24),(540+xc23,420+yc23),(540+xc22,420+yc22),(540+xc21,420+yc21),(540+xc20,420+yc20),
(540+xc19,420+yc19),(540+xc18,420+yc18),(540+xc17,420+yc17),(540+xc16,420+yc16),(540+xc15,420+yc15),
(540+xc14,420+yc14),(540+xc13,420+yc13),(540+px5,420+py5),(540+px4,420+py4),
(540+xc33,420+yc33),(540+xc32,420+yc32),(540+xc31,420+yc31),(540+xc30,420+yc30),
(540+xc29,420+yc29),(540+xc28,420+yc28),(540+xc27,420+yc27),(540+xc26,420+yc26),(540+xc25,420+yc25)]
)]

stencil  = np.zeros(img.shape[:-1]).astype(np.uint8)
cv2.fillPoly(stencil, contours, 255)
cv2.fillPoly(stencil, contours2, 255)
cv2.fillPoly(stencil, contours3, 255)
cv2.fillPoly(stencil, contours4, 255)
sel = stencil != 255
shapes = np.zeros_like(img, np.uint8)
alpha = 0.35
mask = shapes.astype(bool)
# print("mask: ",mask)

img[sel] = cv2.addWeighted(img, alpha, shapes, 1 - alpha, 0)[sel]


cv2.imshow("result1.jpg", img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()