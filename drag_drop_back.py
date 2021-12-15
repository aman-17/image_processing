import math
p=35
#xs
b = 17.318
h = 15.06


xp1, yp1 = 5.7, 0
xp2, yp2 = 0.86, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 12.20, 0
xp5, yp5 = 17.00, 1.18
xp6, yp6 = 19.676, 10.23

cx1, cy1 = 1.00, 3.89
cx2, cy2 = 1.03, 4.92
cx3, cy3 = 1.05, 5.31
cx4, cy4 = 1.09, 5.70
cx5, cy5 = 1.13, 7.87
cx6, cy6 = 1.09, 8.30
cx7, cy7 = 1.05, 8.77
cx8, cy8 = 0.97, 9.13
cx9, cy9 = 0.85, 9.44
cx10, cy10 = 0.66, 9.76
cx11, cy11 = 0.38, 10
cx12, cy12 = 0.15, 10.16

cx13, cy13 = 16.39, 3.89
cx14, cy14 = 16.28, 4.92
cx15, cy15 = 16.26, 5.31
cx16, cy16 = 16.20, 5.70
cx17, cy17 = 16.17, 7.87
cx18, cy18 = 16.24, 8.30
cx19, cy19 = 16.32, 8.77
cx20, cy20 = 16.36, 9.13
cx21, cy21 = 16.48, 9.44
cx22, cy22 = 16.60, 9.76
cx23, cy23 = 16.83, 10
cx24, cy24 = 17.15, 10.16

cx25, cy25 = 5.86, 0.35
cx26, cy26 = 6.06, 0.55
cx27, cy27 = 6.45, 1.06
cx28, cy28 = 6.77, 1.25
cx29, cy29 = 7.20, 1.41
cx30, cy30 = 10.7, 1.41
cx31, cy31 = 11.14, 1.25
cx32, cy32 = 11.69, 0.78
cx33, cy33 = 12.00, 0.39

#s
b = 19.056
h = 15.559


xp1, yp1 = 5.7, 0
xp2, yp2 = 0.86, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 13.70, 0
xp5, yp5 = 18.50, 1.18
xp6, yp6 = 19.676, 10.23

cx1, cy1 = 1.00, 3.89
cx2, cy2 = 1.03, 4.92
cx3, cy3 = 1.05, 5.31
cx4, cy4 = 1.09, 5.70
cx5, cy5 = 1.13, 7.87
cx6, cy6 = 1.09, 8.30
cx7, cy7 = 1.05, 8.77
cx8, cy8 = 0.97, 9.13
cx9, cy9 = 0.85, 9.44
cx10, cy10 = 0.66, 9.76
cx11, cy11 = 0.38, 10
cx12, cy12 = 0.15, 10.16

cx13, cy13 = 18.29, 3.89
cx14, cy14 = 18.18, 4.92
cx15, cy15 = 18.16, 5.31
cx16, cy16 = 18.10, 5.70
cx17, cy17 = 18.07, 7.87
cx18, cy18 = 18.14, 8.30
cx19, cy19 = 18.22, 8.77
cx20, cy20 = 18.26, 9.13
cx21, cy21 = 18.38, 9.44
cx22, cy22 = 18.50, 9.76
cx23, cy23 = 18.73, 10
cx24, cy24 = 19.05, 10.16

cx25, cy25 = 5.86, 0.35
cx26, cy26 = 6.06, 0.55
cx27, cy27 = 6.45, 1.06
cx28, cy28 = 6.77, 1.25
cx29, cy29 = 7.20, 1.41
cx30, cy30 = 12.2, 1.41
cx31, cy31 = 12.64, 1.25
cx32, cy32 = 13.19, 0.78
cx33, cy33 = 13.50, 0.39

#m
b = 20.794
h = 16.059


xp1, yp1 = 6.4, 0
xp2, yp2 = 0.86, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 14.40, 0
xp5, yp5 = 20.30, 1.18
xp6, yp6 = 19.676, 10.23

cx1, cy1 = 1.00, 3.89
cx2, cy2 = 1.03, 4.92
cx3, cy3 = 1.05, 5.31
cx4, cy4 = 1.09, 5.70
cx5, cy5 = 1.13, 7.87
cx6, cy6 = 1.09, 8.30
cx7, cy7 = 1.05, 8.77
cx8, cy8 = 0.97, 9.13
cx9, cy9 = 0.85, 9.44
cx10, cy10 = 0.66, 9.76
cx11, cy11 = 0.38, 10
cx12, cy12 = 0.15, 10.16

cx13, cy13 = 19.89, 3.89
cx14, cy14 = 19.78, 4.92
cx15, cy15 = 19.76, 5.31
cx16, cy16 = 19.70, 5.70
cx17, cy17 = 19.67, 7.87
cx18, cy18 = 19.74, 8.30
cx19, cy19 = 19.82, 8.77
cx20, cy20 = 19.86, 9.13
cx21, cy21 = 19.98, 9.44
cx22, cy22 = 20.10, 9.76
cx23, cy23 = 20.33, 10
cx24, cy24 = 20.65, 10.16

cx25, cy25 = 6.56, 0.35
cx26, cy26 = 6.76, 0.55
cx27, cy27 = 7.15, 1.06
cx28, cy28 = 7.47, 1.25
cx29, cy29 = 7.90, 1.41
cx30, cy30 = 12.9, 1.41
cx31, cy31 = 13.34, 1.25
cx32, cy32 = 13.89, 0.78
cx33, cy33 = 14.20, 0.39

#l
b = 22.532
h = 16.558


xp1, yp1 = 6.4, 0
xp2, yp2 = 0.86, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 15.90, 0
xp5, yp5 = 21.80, 1.18
xp6, yp6 = 19.676, 10.23

cx1, cy1 = 1.00, 3.89
cx2, cy2 = 1.03, 4.92
cx3, cy3 = 1.05, 5.31
cx4, cy4 = 1.09, 5.70
cx5, cy5 = 1.13, 7.87
cx6, cy6 = 1.09, 8.30
cx7, cy7 = 1.05, 8.77
cx8, cy8 = 0.97, 9.13
cx9, cy9 = 0.85, 9.44
cx10, cy10 = 0.66, 9.76
cx11, cy11 = 0.38, 10
cx12, cy12 = 0.15, 10.16

cx13, cy13 = 21.39, 3.89
cx14, cy14 = 21.28, 4.92
cx15, cy15 = 21.26, 5.31
cx16, cy16 = 21.20, 5.70
cx17, cy17 = 21.17, 7.87
cx18, cy18 = 21.24, 8.30
cx19, cy19 = 21.32, 8.77
cx20, cy20 = 21.36, 9.13
cx21, cy21 = 21.48, 9.44
cx22, cy22 = 21.60, 9.76
cx23, cy23 = 21.83, 10
cx24, cy24 = 22.15, 10.16

cx25, cy25 = 6.56, 0.35
cx26, cy26 = 6.76, 0.55
cx27, cy27 = 7.15, 1.06
cx28, cy28 = 7.47, 1.25
cx29, cy29 = 7.90, 1.41
cx30, cy30 = 14.4, 1.41
cx31, cy31 = 14.84, 1.25
cx32, cy32 = 15.39, 0.78
cx33, cy33 = 15.70, 0.39

#xl
b = 24.27
h = 17.058


xp1, yp1 = 7.0, 0
xp2, yp2 = 1.36, 1.18
xp3, yp3 = 0, 10.23

xp4, yp4 = 17.90, 0
xp5, yp5 = 23.20, 1.18
xp6, yp6 = 19.676, 10.23

cx1, cy1 = 1.50, 3.89
cx2, cy2 = 1.53, 4.92
cx3, cy3 = 1.55, 5.31
cx4, cy4 = 1.59, 5.70
cx5, cy5 = 1.63, 7.87
cx6, cy6 = 1.69, 8.30
cx7, cy7 = 1.65, 8.77
cx8, cy8 = 1.47, 9.13
cx9, cy9 = 1.35, 9.44
cx10, cy10 = 1.16, 9.76
cx11, cy11 = 0.88, 10.00
cx12, cy12 = 0.65, 10.16

cx13, cy13 = 22.79, 3.89
cx14, cy14 = 22.68, 4.92
cx15, cy15 = 22.66, 5.31
cx16, cy16 = 22.60, 5.70
cx17, cy17 = 22.57, 7.87
cx18, cy18 = 22.64, 8.30
cx19, cy19 = 22.72, 8.77
cx20, cy20 = 22.76, 9.13
cx21, cy21 = 22.88, 9.44
cx22, cy22 = 23.00, 9.76
cx23, cy23 = 23.23, 10.00
cx24, cy24 = 23.55, 10.16

cx25, cy25 = 7.16, 0.35
cx26, cy26 = 7.36, 0.55
cx27, cy27 = 7.75, 1.06
cx28, cy28 = 8.07, 1.25
cx29, cy29 = 8.50, 1.41
cx30, cy30 = 16.4, 1.41
cx31, cy31 = 16.84, 1.25
cx32, cy32 = 17.39, 0.78
cx33, cy33 = 17.70, 0.39



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


list1=[(px1,py1),(px2,py2),(xc1,yc1),(xc2,yc2),(xc3,yc3),(xc4,yc4),(xc5,yc5),(xc6,yc6),(xc7,yc7),(xc8,yc8),(xc9,yc9),(xc10,yc10),(xc11,yc11),(xc12,yc12),(0,py3),(0,py3+y1),(x1,py3+y1),
       (x1,py6),(xc24,yc24),(xc23,yc23),(xc22,yc22),(xc21,yc21),(xc20,yc20),(xc19,yc19),(xc18,yc18),(xc17,yc17),(xc16,yc16),(xc15,yc15),(xc14,yc14),(xc13,yc13),(px5,py5),(px4,py4),
       (xc33,yc33),(xc32,yc32),(xc31,yc31),(xc30,yc30),(xc29,yc29),(xc28,yc28),(xc27,yc27),(xc26,yc26),(xc25,yc25)]
print(list1)

