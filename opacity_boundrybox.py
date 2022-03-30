import re
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
import os, glob, requests
import random

img = cv2.imread("mrcnn_37.jpg")
f = open('dh-34-panel.json')
data = json.load(f)
d=data["xs"]["f"]["h3"]

pixelsPerMetric_ann=37

# ann_c0=math.ceil(pixelsPerMetric_ann*float(d['h']))
# ann_c1=math.ceil(pixelsPerMetric_ann*float(d['b']))
# ann_ccx1=math.ceil(pixelsPerMetric_ann*float(d['cx1']))
# ann_ccx2=math.ceil(pixelsPerMetric_ann*float(d['cx2']))
# ann_ccx3=math.ceil(pixelsPerMetric_ann*float(d['cx3']))
# ann_ccx4=math.ceil(pixelsPerMetric_ann*float(d['cx4']))
# ann_ccx5=math.ceil(pixelsPerMetric_ann*float(d['cx5']))
# ann_ccx6=math.ceil(pixelsPerMetric_ann*float(d['cx6']))
# ann_ccx7=math.ceil(pixelsPerMetric_ann*float(d['cx7']))
# ann_ccx8=math.ceil(pixelsPerMetric_ann*float(d['cx8']))
# ann_ccx9=math.ceil(pixelsPerMetric_ann*float(d['cx9']))
# ann_ccx10=math.ceil(pixelsPerMetric_ann*float(d['cx10']))
# ann_ccx11=math.ceil(pixelsPerMetric_ann*float(d['cx11']))
# ann_ccx12=math.ceil(pixelsPerMetric_ann*float(d['cx12']))
# ann_ccx13=math.ceil(pixelsPerMetric_ann*float(d['cx13']))
# ann_ccx14=math.ceil(pixelsPerMetric_ann*float(d['cx14']))
# ann_ccx15=math.ceil(pixelsPerMetric_ann*float(d['cx15']))
# ann_ccx16=math.ceil(pixelsPerMetric_ann*float(d['cx16']))

# ann_ccy1=math.ceil(pixelsPerMetric_ann*float(d['cy1']))
# ann_ccy2=math.ceil(pixelsPerMetric_ann*float(d['cy2']))
# ann_ccy3=math.ceil(pixelsPerMetric_ann*float(d['cy3']))
# ann_ccy4=math.ceil(pixelsPerMetric_ann*float(d['cy4']))
# ann_ccy5=math.ceil(pixelsPerMetric_ann*float(d['cy5']))
# ann_ccy6=math.ceil(pixelsPerMetric_ann*float(d['cy6']))
# ann_ccy7=math.ceil(pixelsPerMetric_ann*float(d['cy7']))
# ann_ccy8=math.ceil(pixelsPerMetric_ann*float(d['cy8']))
# ann_ccy9=math.ceil(pixelsPerMetric_ann*float(d['cy9']))
# ann_ccy10=math.ceil(pixelsPerMetric_ann*float(d['cy10']))
# ann_ccy11=math.ceil(pixelsPerMetric_ann*float(d['cy11']))
# ann_ccy12=math.ceil(pixelsPerMetric_ann*float(d['cy12']))
# ann_ccy13=math.ceil(pixelsPerMetric_ann*float(d['cy13']))
# ann_ccy14=math.ceil(pixelsPerMetric_ann*float(d['cy14']))
# ann_ccy15=math.ceil(pixelsPerMetric_ann*float(d['cy15']))
# ann_ccy16=math.ceil(pixelsPerMetric_ann*float(d['cy16']))

# ann_list1=[(0,0),(0,ann_c0),(ann_ccx16,ann_ccy16),(ann_ccx15,ann_ccy15),(ann_ccx14,ann_ccy14),(ann_ccx13,ann_ccy13),(ann_ccx12,ann_ccy12),
# (ann_ccx11,ann_ccy11),(ann_ccx10,ann_ccy10),(ann_ccx9,ann_ccy9),(ann_ccx8,ann_ccy8),(ann_ccx7,ann_ccy7),(ann_ccx6,ann_ccy6),(ann_ccx5,ann_ccy5),
# (ann_ccx4,ann_ccy4),(ann_ccx3,ann_ccy3),(ann_ccx2,ann_ccy2),(ann_ccx1,ann_ccy1),(ann_c1,0)]

p=37

h, b =  8.614, 11.756

xp1, yp1 = 0, 0
xp2, yp2 = 6.14, 0
xp3, yp3 = 10.5, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.09, 0.43
cx3, cy3 = 0.11, 0.59
cx4, cy4 = 0.21, 1.02
cx5, cy5 = 0.35, 1.45
cx6, cy6 = 0.43, 1.69
cx7, cy7 = 0.61, 2.08
cx8, cy8 = 0.70, 2.24
cx9, cy9 = 0.80, 2.40
cx10, cy10 =0.95, 2.59 
cx11, cy11 =1.15, 2.79
cx12, cy12 =1.29, 2.88
cx13, cy13 =1.85, 3.12

cx14, cy14 =2.00, 3.17
cx15, cy15 =2.32, 3.26 
cx16, cy16 =2.63, 3.33 
cx17, cy17 =2.99, 3.38
cx18, cy18 =3.58, 3.42
cx19, cy19 =4.29, 3.34
cx20, cy20 =4.44, 3.28
cx21, cy21 =4.72, 3.14
cx22, cy22 =5.07, 2.95
cx23, cy23 =5.31, 2.75
cx24, cy24 =5.51, 2.55
cx25, cy25 =5.66, 2.36
cx26, cy26 =5.78, 2.04
cx27, cy27 =5.94, 1.61
cx28, cy28 =6.06, 1.18
cx29, cy29 =6.10, 0.82
cx30, cy30 =6.14, 0.39

cx31, cy31 = 10.14, 1.65
cx32, cy32 = 10.02, 1.96
cx33, cy33 = 9.83, 2.4 
cx34, cy34 = 9.70, 2.95
cx35, cy35 = 9.64, 3.38 
cx36, cy36 = 9.56, 3.85
cx37, cy37 = 9.57, 4.25
cx38, cy38 = 9.58, 4.72
cx39, cy39 = 9.60, 5.19
cx40, cy40 = 9.65, 5.59
cx41, cy41 = 9.73, 6.06
cx42, cy42 = 9.80, 6.49
cx43, cy43 = 9.92, 6.92
cx44, cy44 = 10.03, 7.28
cx45, cy45 = 10.27, 7.63
cx46, cy46 = 10.43, 7.91
cx47, cy47 = 10.62, 8.11
cx48, cy48 = 10.76, 8.22 
cx49, cy49 = 11.0, 8.38
cx50, cy50 = 11.7, 8.60

xcp1=math.ceil(xp1*p)
xcp2=math.ceil(xp2*p)
xcp3=math.ceil(xp3*p)

ycp1=math.ceil(yp1*p)
ycp2=math.ceil(yp2*p)
ycp3=math.ceil(yp3*p)


c1=math.ceil(h*p)
c2=math.ceil(b*p)


ccx1=math.ceil(cx1*p)
ccx2=math.ceil(cx2*p)
ccx3=math.ceil(cx3*p)
ccx4=math.ceil(cx4*p)
ccx5=math.ceil(cx5*p)
ccx6=math.ceil(cx6*p)
ccx7=math.ceil(cx7*p)
ccx8=math.ceil(cx8*p)
ccx9=math.ceil(cx9*p)
ccx10=math.ceil(cx10*p)
ccx11=math.ceil(cx11*p)
ccx12=math.ceil(cx12*p)
ccx13=math.ceil(cx13*p)
ccx14=math.ceil(cx14*p)
ccx15=math.ceil(cx15*p)
ccx16=math.ceil(cx16*p)
ccx17=math.ceil(cx17*p)
ccx18=math.ceil(cx18*p)
ccx19=math.ceil(cx19*p)
ccx20=math.ceil(cx20*p)
ccx21=math.ceil(cx21*p)
ccx22=math.ceil(cx22*p)
ccx23=math.ceil(cx23*p)
ccx24=math.ceil(cx24*p)
ccx25=math.ceil(cx25*p)
ccx26=math.ceil(cx26*p)
ccx27=math.ceil(cx27*p)
ccx28=math.ceil(cx28*p)
ccx29=math.ceil(cx29*p)
ccx30=math.ceil(cx30*p)
ccx31=math.ceil(cx31*p)
ccx32=math.ceil(cx32*p)
ccx33=math.ceil(cx33*p)
ccx34=math.ceil(cx34*p)
ccx35=math.ceil(cx35*p)
ccx36=math.ceil(cx36*p)
ccx37=math.ceil(cx37*p)
ccx38=math.ceil(cx38*p)
ccx39=math.ceil(cx39*p)
ccx40=math.ceil(cx40*p)
ccx41=math.ceil(cx41*p)
ccx42=math.ceil(cx42*p)
ccx43=math.ceil(cx43*p)
ccx44=math.ceil(cx44*p)
ccx45=math.ceil(cx45*p)
ccx46=math.ceil(cx46*p)
ccx47=math.ceil(cx47*p)
ccx48=math.ceil(cx48*p)
ccx49=math.ceil(cx49*p)
ccx50=math.ceil(cx50*p)


ccy1=math.ceil(cy1*p)
ccy2=math.ceil(cy2*p)
ccy3=math.ceil(cy3*p)
ccy4=math.ceil(cy4*p)
ccy5=math.ceil(cy5*p)
ccy6=math.ceil(cy6*p)
ccy7=math.ceil(cy7*p)
ccy8=math.ceil(cy8*p)
ccy9=math.ceil(cy9*p)
ccy10=math.ceil(cy10*p)
ccy11=math.ceil(cy11*p)
ccy12=math.ceil(cy12*p)
ccy13=math.ceil(cy13*p)
ccy14=math.ceil(cy14*p)
ccy15=math.ceil(cy15*p)
ccy16=math.ceil(cy16*p)
ccy17=math.ceil(cy17*p)
ccy18=math.ceil(cy18*p)
ccy19=math.ceil(cy19*p)
ccy20=math.ceil(cy20*p)
ccy21=math.ceil(cy21*p)
ccy22=math.ceil(cy22*p)
ccy23=math.ceil(cy23*p)
ccy24=math.ceil(cy24*p)
ccy25=math.ceil(cy25*p)
ccy26=math.ceil(cy26*p)
ccy27=math.ceil(cy27*p)
ccy28=math.ceil(cy28*p)
ccy29=math.ceil(cy29*p)
ccy30=math.ceil(cy30*p)
ccy31=math.ceil(cy31*p)
ccy32=math.ceil(cy32*p)
ccy33=math.ceil(cy33*p)
ccy34=math.ceil(cy34*p)
ccy35=math.ceil(cy35*p)
ccy36=math.ceil(cy36*p)
ccy37=math.ceil(cy37*p)
ccy38=math.ceil(cy38*p)
ccy39=math.ceil(cy39*p)
ccy40=math.ceil(cy40*p)
ccy41=math.ceil(cy41*p)
ccy42=math.ceil(cy42*p)
ccy43=math.ceil(cy43*p)
ccy44=math.ceil(cy44*p)
ccy45=math.ceil(cy45*p)
ccy46=math.ceil(cy46*p)
ccy47=math.ceil(cy47*p)
ccy48=math.ceil(cy48*p)
ccy49=math.ceil(cy49*p)
ccy50=math.ceil(cy50*p)

contours = [ np.array([[xcp1,0],[0,c1],[c2,c1],[ccx50,ccy50],[ccx49,ccy49],[ccx48,ccy48],[ccx47,ccy47],[ccx46,ccy46],[ccx45,ccy45],[ccx44,ccy44],[ccx43,ccy43],[ccx42,ccy42],[ccx41,ccy41],[ccx40,ccy40],
       [ccx39,ccy39],[ccx38,ccy38],[ccx37,ccy37],[ccx36,ccy36],[ccx35,ccy35],[ccx34,ccy34],[ccx33,ccy33],[ccx32,ccy32],[ccx31,ccy31],[xcp3,ycp3],[xcp2,ycp2],[ccx30,ccy30],
       [ccx29,ccy29],[ccx28,ccy28],[ccx27,ccy27],[ccx26,ccy26],[ccx25,ccy25],[ccx24,ccy24],[ccx23,ccy23],[ccx22,ccy22],[ccx21,ccy21],[ccx20,ccy20],
       [ccx19,ccy19],[ccx18,ccy18],[ccx17,ccy17],[ccx16,ccy16],[ccx15,ccy15],[ccx14,ccy14],[ccx13,ccy13],[ccx12,ccy12],[ccx11,ccy11],[ccx10,ccy10],
       [ccx9,ccy9],[ccx8,ccy8],[ccx7,ccy7],[ccx6,ccy6],[ccx5,ccy5],[ccx4,ccy4],[ccx3,ccy3],[ccx2,ccy2],[ccx1,ccy1]])
           ]

stencil  = np.zeros(img.shape[:-1]).astype(np.uint8)
cv2.fillPoly(stencil, contours, 255)
sel = stencil != 255
shapes = np.zeros_like(img, np.uint8)
alpha = 0.5
mask = shapes.astype(bool)
# print("mask: ",mask)

img[sel] = cv2.addWeighted(img, alpha, shapes, 1 - alpha, 0)[sel]



cv2.imshow("result.jpg", img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()