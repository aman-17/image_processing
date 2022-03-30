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

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

width=0.955
b, h = 4.748, 4.233 


img = cv2.imread("/Users/amanrangapur/Desktop/labels/backimage_1645048347.png")
# plt.imshow(img)
# plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)
cnts_1=cnts[0]
detected_circles = cv2.HoughCircles(gray,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40)
pixelsPerMetric = None

for c in cnts:
    if cv2.contourArea(c) < 100:
        continue
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    if pixelsPerMetric is None:
        pixelsPerMetric = dB / width
        #print(pixelsPerMetric)
        #p=math.floor(pixelsPerMetric)
        #print(p)

p=44

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

list1=[(xcp1,0),(0,c1),(c2,c1),(ccx50,ccy50),(ccx49,ccy49),(ccx48,ccy48),(ccx47,ccy47),(ccx46,ccy46),(ccx45,ccy45),(ccx44,ccy44),(ccx43,ccy43),(ccx42,ccy42),(ccx41,ccy41),(ccx40,ccy40),
       (ccx39,ccy39),(ccx38,ccy38),(ccx37,ccy37),(ccx36,ccy36),(ccx35,ccy35),(ccx34,ccy34),(ccx33,ccy33),(ccx32,ccy32),(ccx31,ccy31),(xcp3,ycp3),(xcp2,ycp2),(ccx30,ccy30),
       (ccx29,ccy29),(ccx28,ccy28),(ccx27,ccy27),(ccx26,ccy26),(ccx25,ccy25),(ccx24,ccy24),(ccx23,ccy23),(ccx22,ccy22),(ccx21,ccy21),(ccx20,ccy20),
       (ccx19,ccy19),(ccx18,ccy18),(ccx17,ccy17),(ccx16,ccy16),(ccx15,ccy15),(ccx14,ccy14),(ccx13,ccy13),(ccx12,ccy12),(ccx11,ccy11),(ccx10,ccy10),
       (ccx9,ccy9),(ccx8,ccy8),(ccx7,ccy7),(ccx6,ccy6),(ccx5,ccy5),(ccx4,ccy4),(ccx3,ccy3),(ccx2,ccy2),(ccx1,ccy1)]


# c1 = math.ceil(pixelsPerMetric * float(h))
# c2 = math.ceil(pixelsPerMetric * float(b))
# list1 = [(1610+0, 770+0),(1610+0 + c1, 770+0),(1610+0 + c1, 770+0 + c2),(1610+0, 770+c2)] 



#list1 = [(250+0,500+0),(250+0,500+c2),(250+c1,500+c2),(250+ccx6,500+ccy6),(250+ccx5,500+ccy5),(250+ccx4,500+ccy4),(250+ccx3,500+ccy3),(250+ccx2,500+ccy2),(250+ccx1,500+ccy1),(250+c3,500+0)]

# list1=[(950+c2,1520+ycp1),(950+xcp2,1520+ycp2),(950+ccx1,1520+ccy1),(950+ccx2,1520+ccy2),(950+ccx3,1520+ccy3),(950+ccx4,1520+ccy4),(950+ccx5,1520+ccy5),(950+ccx6,1520+ccy6),(950+ccx7,1520+ccy7),(950+ccx8,1520+ccy8),(950+ccx9,1520+ccy9),(950+ccx10,1520+ccy10),(950+ccx11,1520+ccy11),(950+ccx12,1520+ccy12),(950+ccx13,1520+ccy13),(950+ccx14,1520+ccy14),(950+ccx15,1520+ccy15),(950+ccx16,1520+ccy16)
#        ,(950+ccx17,1520+ccy17),(950+ccx18,1520+ccy18),(950+ccx19,1520+ccy19),(950+ccx20,1520+ccy20),(950+0,1520+c1),(950+c2,1520+c1)]
'''
panelPoints=[]
new_points=[]

#coordinates=Polygon([(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
#       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)])

#list1=[(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
#       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)]

#list1=[(184, 0), (40, 43), (47, 63), (54, 78), (60, 93), (65, 111), (68, 125), (72, 143),
#       (75, 163), (77, 175), (76, 187), (74, 199), (72, 213), (70, 224), (68, 234), (66, 246), (61, 257), (58, 265), (51, 278), (42, 288), (33, 295), (24, 301), (0, 311), (184, 311)]


Q1 = scale(coordinates, xfact = -1, origin = (1, 0))
panelPoints=(list((Q1.exterior.coords)))
panelPoints.reverse()
#print(panelPoints)




mav_val=0
for points in panelPoints:
    if points[0]<mav_val:
        mav_val=points[0]
    
for points in panelPoints:
    point_x=points[0]-mav_val
    point_y=points[1]
    new_points.append((point_x, point_y))
    
print('\n\n')
print(new_points)

'''




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
img=cv2.line(img, list1[18], list1[19], (0,255,0), 6)
img=cv2.line(img, list1[19], list1[20], (0,255,0), 6)
img=cv2.line(img, list1[20], list1[21], (0,255,0), 6)
img=cv2.line(img, list1[21], list1[22], (0,255,0), 6)
img=cv2.line(img, list1[22], list1[23], (0,255,0), 6)
img=cv2.line(img, list1[23], list1[24], (0,255,0), 6)
img=cv2.line(img, list1[24], list1[25], (0,255,0), 6)

img=cv2.line(img, list1[25], list1[26], (0,255,0), 6)
img=cv2.line(img, list1[26], list1[27], (0,255,0), 6)
img=cv2.line(img, list1[27], list1[28], (0,255,0), 6)
img=cv2.line(img, list1[28], list1[29], (0,255,0), 6)
img=cv2.line(img, list1[29], list1[30], (0,255,0), 6)
img=cv2.line(img, list1[30], list1[31], (0,255,0), 6)
img=cv2.line(img, list1[31], list1[32], (0,255,0), 6)
img=cv2.line(img, list1[32], list1[33], (0,255,0), 6)
img=cv2.line(img, list1[33], list1[34], (0,255,0), 6)
img=cv2.line(img, list1[34], list1[35], (0,255,0), 6)
img=cv2.line(img, list1[35], list1[36], (0,255,0), 6)
img=cv2.line(img, list1[36], list1[37], (0,255,0), 6)
img=cv2.line(img, list1[37], list1[38], (0,255,0), 6)
img=cv2.line(img, list1[38], list1[39], (0,255,0), 6)
img=cv2.line(img, list1[39], list1[40], (0,255,0), 6)
img=cv2.line(img, list1[40], list1[41], (0,255,0), 6)
img=cv2.line(img, list1[41], list1[42], (0,255,0), 6)
img=cv2.line(img, list1[42], list1[43], (0,255,0), 6)
img=cv2.line(img, list1[43], list1[44], (0,255,0), 6)
img=cv2.line(img, list1[44], list1[45], (0,255,0), 6)
img=cv2.line(img, list1[45], list1[46], (0,255,0), 6)
img=cv2.line(img, list1[46], list1[47], (0,255,0), 6)
img=cv2.line(img, list1[47], list1[48], (0,255,0), 6)
img=cv2.line(img, list1[48], list1[49], (0,255,0), 6)
img=cv2.line(img, list1[49], list1[50], (0,255,0), 6)
img=cv2.line(img, list1[50], list1[51], (0,255,0), 6)
img=cv2.line(img, list1[51], list1[52], (0,255,0), 6)
img=cv2.line(img, list1[52], list1[53], (0,255,0), 6)
img=cv2.line(img, list1[53], list1[54], (0,255,0), 6)
img=cv2.line(img, list1[54], list1[0], (0,255,0), 6)

cv2.imwrite('mrcnn_44.jpg', img)
# k=cv2.waitKey(0) & 0xFF
# if k == 27:
#     cv2.destroyAllWindows()

