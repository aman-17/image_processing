import math

b = 20.937
h = 12.922

p=10

xp1, yp1 = 3.93, 0
xp2, yp2 = 1.18, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 16.92, 0
xp5, yp5 = 20.07, 1.18
xp6, yp6 = 20.93, 10.23

cx1, cy1 = 1.40, 3.89
cx2, cy2 = 1.43, 4.92
cx3, cy3 = 1.45, 5.31
cx4, cy4 = 1.49, 5.70
cx5, cy5 = 1.53, 7.87
cx6, cy6 = 1.49, 8.30
cx7, cy7 = 1.45, 8.77
cx8, cy8 = 1.37, 9.13
cx9, cy9 = 1.25, 9.44
cx10, cy10 = 1.06, 9.76
cx11, cy11 = 0.78, 10
cx12, cy12 = 0.35, 10.16

cx13, cy13 = 19.59, 3.89
cx14, cy14 = 19.48, 4.92
cx15, cy15 = 19.46, 5.31
cx16, cy16 = 19.40, 5.70
cx17, cy17 = 19.37, 7.87
cx18, cy18 = 19.44, 8.30
cx19, cy19 = 19.52, 8.77
cx20, cy20 = 19.56, 9.13
cx21, cy21 = 19.68, 9.44
cx22, cy22 = 19.80, 9.76
cx23, cy23 = 20.03, 10
cx24, cy24 = 20.35, 10.13

cx25, cy25 = 4.92, 1.22
cx26, cy26 = 5.62, 1.81
cx27, cy27 = 6.45, 2.12
cx28, cy28 = 7.87, 2.55
cx29, cy29 = 11.10, 2.71
cx30, cy30 = 12.99, 2.55
cx31, cy31 = 14.09, 2.32
cx32, cy32 = 15.15, 1.88
cx33, cy33 = 16.00, 1.20

y1=math.ceil(p*h)
x1=math.ceil(p*b)

px1=math.ceil(p*xp1)
px2=math.ceil(p*xp2)
px3=math.ceil(p*xp3)
px4=math.ceil(p*xp4)
px5=math.ceil(p*xp5)
px6=math.ceil(p*xp6)

py1=math.ceil(p*yp1)
py2=math.ceil(p*yp2)
py3=math.ceil(p*yp3)
py4=math.ceil(p*yp4)
py5=math.ceil(p*yp5)
py6=math.ceil(p*yp6)

xc1=math.ceil(p*cx1)
xc2=math.ceil(p*cx2)
xc3=math.ceil(p*cx3)
xc4=math.ceil(p*cx4)
xc5=math.ceil(p*cx5)
xc6=math.ceil(p*cx6)
xc7=math.ceil(p*cx7)
xc8=math.ceil(p*cx8)
xc9=math.ceil(p*cx9)
xc10=math.ceil(p*cx10)
xc11=math.ceil(p*cx11)
xc12=math.ceil(p*cx12)
xc13=math.ceil(p*cx13)
xc14=math.ceil(p*cx14)
xc15=math.ceil(p*cx15)
xc16=math.ceil(p*cx16)
xc17=math.ceil(p*cx17)
xc18=math.ceil(p*cx18)
xc19=math.ceil(p*cx19)
xc20=math.ceil(p*cx20)
xc21=math.ceil(p*cx21)
xc22=math.ceil(p*cx22)
xc23=math.ceil(p*cx23)
xc24=math.ceil(p*cx24)
xc25=math.ceil(p*cx25)
xc26=math.ceil(p*cx26)
xc27=math.ceil(p*cx27)
xc28=math.ceil(p*cx28)
xc29=math.ceil(p*cx29)
xc30=math.ceil(p*cx30)
xc31=math.ceil(p*cx31)
xc32=math.ceil(p*cx32)
xc33=math.ceil(p*cx33)

yc1=math.ceil(p*cy1)
yc2=math.ceil(p*cy2)
yc3=math.ceil(p*cy3)
yc4=math.ceil(p*cy4)
yc5=math.ceil(p*cy5)
yc6=math.ceil(p*cy6)
yc7=math.ceil(p*cy7)
yc8=math.ceil(p*cy8)
yc9=math.ceil(p*cy9)
yc10=math.ceil(p*cy10)
yc11=math.ceil(p*cy11)
yc12=math.ceil(p*cy12)
yc13=math.ceil(p*cy13)
yc14=math.ceil(p*cy14)
yc15=math.ceil(p*cy15)
yc16=math.ceil(p*cy16)
yc17=math.ceil(p*cy17)
yc18=math.ceil(p*cy18)
yc19=math.ceil(p*cy19)
yc20=math.ceil(p*cy20)
yc21=math.ceil(p*cy21)
yc22=math.ceil(p*cy22)
yc23=math.ceil(p*cy23)
yc24=math.ceil(p*cy24)
yc25=math.ceil(p*cy25)
yc26=math.ceil(p*cy26)
yc27=math.ceil(p*cy27)
yc28=math.ceil(p*cy28)
yc29=math.ceil(p*cy29)
yc30=math.ceil(p*cy30)
yc31=math.ceil(p*cy31)
yc32=math.ceil(p*cy32)
yc33=math.ceil(p*cy33)

list1=[(px1,py1),(px2,py2),(xc1,yc1),(xc2,yc2),(xc3,yc3),(xc4,yc4),(xc5,yc5),(xc6,yc6),(xc7,yc7),(xc8,yc8),(xc9,yc9),(xc10,yc10),(xc11,yc11),(xc12,yc12),(0,py3),(0,py3+y1),(x1,py3+y1),(x1,py6),(xc24,yc24),(xc23,yc3),(xc22,yc22),(xc21,yc21),(xc20,yc20),(xc19,yc19),(xc18,yc18),(xc17,yc17),(xc16,yc16),(xc15,yc15),(xc14,yc14),(xc13,yc13),(px5,py5),(px4,py4),(xc33,yc33),(xc32,yc32),(xc31,yc31),(xc30,yc30),(xc29,yc29),(xc28,yc28),(xc27,yc27),(xc26,yc26),(xc25,yc25)]
print(list1)
