import math

p=10

#xs
h, b =  8.614, 11.756

xp1, yp1 = 0, 0
xp2, yp2 = 6.14, 0
xp3, yp3 = 10.5, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.10, 0.43
cx3, cy3 = 0.13, 0.59
cx4, cy4 = 0.21, 1.02
cx5, cy5 = 0.35, 1.45
cx6, cy6 = 0.43, 1.69
cx7, cy7 = 0.62, 2.08
cx8, cy8 = 0.74, 2.24
cx9, cy9 = 0.80, 2.40
cx10, cy10 =0.95, 2.59 
cx11, cy11 =1.14, 2.79
cx12, cy12 =1.29, 2.91
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

#s
h, b =  9.111, 12.631

xp1, yp1 = 0, 0
xp2, yp2 = 6.37, 0
xp3, yp3 = 10.7, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.10, 0.43
cx3, cy3 = 0.13, 0.59
cx4, cy4 = 0.27, 1.02
cx5, cy5 = 0.45, 1.45
cx6, cy6 = 0.53, 1.69
cx7, cy7 = 0.72, 2.08
cx8, cy8 = 0.84, 2.24
cx9, cy9 = 0.90, 2.40
cx10, cy10 =1.15, 2.59 
cx11, cy11 =1.34, 2.79
cx12, cy12 =1.49, 2.91
cx13, cy13 =2.05, 3.12

cx14, cy14 =2.20, 3.17
cx15, cy15 =2.52, 3.26 
cx16, cy16 =2.83, 3.33 
cx17, cy17 =3.19, 3.38
cx18, cy18 =3.78, 3.42
cx19, cy19 =4.49, 3.34
cx20, cy20 =4.64, 3.28
cx21, cy21 =4.92, 3.14
cx22, cy22 =5.27, 2.95
cx23, cy23 =5.51, 2.75
cx24, cy24 =5.71, 2.55
cx25, cy25 =5.86, 2.36
cx26, cy26 =5.98, 2.04
cx27, cy27 =6.14, 1.61
cx28, cy28 =6.26, 1.18
cx29, cy29 =6.30, 0.82
cx30, cy30 =6.34, 0.39

cx31, cy31 = 10.34, 1.65
cx32, cy32 = 10.12, 1.96
cx33, cy33 = 9.93, 2.4 
cx34, cy34 = 9.80, 2.95
cx35, cy35 = 9.74, 3.38 
cx36, cy36 = 9.66, 3.85
cx37, cy37 = 9.67, 4.25
cx38, cy38 = 9.68, 4.72
cx39, cy39 = 9.70, 5.19
cx40, cy40 = 9.75, 5.59
cx41, cy41 = 9.83, 6.06
cx42, cy42 = 9.90, 6.49
cx43, cy43 = 10.02, 6.92
cx44, cy44 = 10.13, 7.28
cx45, cy45 = 10.37, 7.63
cx46, cy46 = 10.53, 7.91
cx47, cy47 = 10.72, 8.11
cx48, cy48 = 10.86, 8.22 
cx49, cy49 = 11.1, 8.38
cx50, cy50 = 11.8, 8.80

#m
h, b =  9.610, 13.506

xp1, yp1 = 0, 0
xp2, yp2 = 6.57, 0
xp3, yp3 = 11.3, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.10, 0.43
cx3, cy3 = 0.13, 0.59
cx4, cy4 = 0.21, 1.02
cx5, cy5 = 0.35, 1.45
cx6, cy6 = 0.43, 1.69
cx7, cy7 = 0.62, 2.08
cx8, cy8 = 0.74, 2.24
cx9, cy9 = 0.80, 2.40
cx10, cy10 =0.95, 2.59 
cx11, cy11 =1.14, 2.79
cx12, cy12 =1.29, 2.91
cx13, cy13 =1.85, 3.12

cx14, cy14 =2.40, 3.24
cx15, cy15 =2.72, 3.29 
cx16, cy16 =3.03, 3.37 
cx17, cy17 =3.39, 3.38
cx18, cy18 =3.98, 3.42
cx19, cy19 =4.69, 3.34
cx20, cy20 =4.84, 3.28
cx21, cy21 =5.12, 3.14
cx22, cy22 =5.47, 2.95
cx23, cy23 =5.71, 2.75
cx24, cy24 =5.91, 2.55
cx25, cy25 =6.06, 2.36
cx26, cy26 =6.18, 2.04
cx27, cy27 =6.34, 1.61
cx28, cy28 =6.46, 1.18
cx29, cy29 =6.50, 0.82
cx30, cy30 =6.54, 0.39

cx31, cy31 = 10.78, 1.65
cx32, cy32 = 10.58, 1.96
cx33, cy33 = 10.43, 2.4 
cx34, cy34 = 10.20, 2.95
cx35, cy35 = 10.14, 3.38 
cx36, cy36 = 10.06, 3.85
cx37, cy37 = 10.07, 4.25
cx38, cy38 = 10.08, 4.72
cx39, cy39 = 10.10, 5.19
cx40, cy40 = 10.15, 5.59
cx41, cy41 = 10.23, 6.06
cx42, cy42 = 10.30, 6.49
cx43, cy43 = 10.42, 6.92
cx44, cy44 = 10.53, 7.28
cx45, cy45 = 10.77, 7.63
cx46, cy46 = 10.93, 7.91
cx47, cy47 = 11.12, 8.11
cx48, cy48 = 11.26, 8.22 
cx49, cy49 = 11.4, 8.38
cx50, cy50 = 12.2, 8.90

#l
h, b =  10.111, 14.381

xp1, yp1 = 0, 0
xp2, yp2 = 6.67, 0
xp3, yp3 = 11.7, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.10, 0.43
cx3, cy3 = 0.13, 0.59
cx4, cy4 = 0.21, 1.02
cx5, cy5 = 0.35, 1.45
cx6, cy6 = 0.43, 1.69
cx7, cy7 = 0.62, 2.08
cx8, cy8 = 0.74, 2.24
cx9, cy9 = 0.80, 2.40
cx10, cy10 =0.95, 2.59 
cx11, cy11 =1.14, 2.79
cx12, cy12 =1.29, 2.91
cx13, cy13 =1.85, 3.12

cx14, cy14 =2.50, 3.24
cx15, cy15 =2.82, 3.29 
cx16, cy16 =3.13, 3.37 
cx17, cy17 =3.49, 3.38
cx18, cy18 =4.08, 3.42
cx19, cy19 =4.79, 3.34
cx20, cy20 =4.94, 3.28
cx21, cy21 =5.22, 3.14
cx22, cy22 =5.57, 2.95
cx23, cy23 =5.81, 2.75
cx24, cy24 =6.01, 2.55
cx25, cy25 =6.16, 2.36
cx26, cy26 =6.28, 2.04
cx27, cy27 =6.44, 1.61
cx28, cy28 =6.56, 1.18
cx29, cy29 =6.60, 0.82
cx30, cy30 =6.64, 0.39

cx31, cy31 = 11.58, 1.65
cx32, cy32 = 11.50, 1.96
cx33, cy33 = 11.33, 2.4 
cx34, cy34 = 11.20, 2.95
cx35, cy35 = 11.14, 3.38 
cx36, cy36 = 11.06, 3.85
cx37, cy37 = 11.07, 4.25
cx38, cy38 = 11.08, 4.72
cx39, cy39 = 11.10, 5.19
cx40, cy40 = 11.15, 5.59
cx41, cy41 = 11.23, 6.06
cx42, cy42 = 11.30, 6.49
cx43, cy43 = 11.42, 6.92
cx44, cy44 = 11.53, 7.28
cx45, cy45 = 11.77, 7.63
cx46, cy46 = 11.93, 7.91
cx47, cy47 = 12.12, 8.11
cx48, cy48 = 12.26, 8.22 
cx49, cy49 = 12.4, 8.38
cx50, cy50 = 13.2, 9.15

#xl
h, b =  10.613, 15.256

xp1, yp1 = 0, 0
xp2, yp2 = 6.87, 0
xp3, yp3 = 12.0, 1.02

cx1, cy1 = 0.06, 0.27
cx2, cy2 = 0.10, 0.43
cx3, cy3 = 0.13, 0.59
cx4, cy4 = 0.21, 1.02
cx5, cy5 = 0.35, 1.45
cx6, cy6 = 0.43, 1.69
cx7, cy7 = 0.62, 2.08
cx8, cy8 = 0.74, 2.24
cx9, cy9 = 0.80, 2.40
cx10, cy10 =0.95, 2.64 
cx11, cy11 =1.14, 2.84
cx12, cy12 =1.29, 2.97
cx13, cy13 =1.85, 3.17

cx14, cy14 =2.60, 3.30
cx15, cy15 =2.92, 3.33 
cx16, cy16 =3.23, 3.37 
cx17, cy17 =3.39, 3.38
cx18, cy18 =4.18, 3.42
cx19, cy19 =4.89, 3.34
cx20, cy20 =5.04, 3.28
cx21, cy21 =5.32, 3.14
cx22, cy22 =5.67, 2.95
cx23, cy23 =5.91, 2.75
cx24, cy24 =6.11, 2.55
cx25, cy25 =6.26, 2.36
cx26, cy26 =6.38, 2.04
cx27, cy27 =6.54, 1.61
cx28, cy28 =6.66, 1.18
cx29, cy29 =6.72, 0.82
cx30, cy30 =6.84, 0.39

cx31, cy31 = 11.98, 1.65
cx32, cy32 = 11.95, 1.96
cx33, cy33 = 11.93, 2.4 
cx34, cy34 = 11.88, 2.95
cx35, cy35 = 11.84, 3.38 
cx36, cy36 = 11.79, 3.85
cx37, cy37 = 11.77, 4.25
cx38, cy38 = 11.78, 4.72
cx39, cy39 = 11.80, 5.19
cx40, cy40 = 11.85, 5.59
cx41, cy41 = 11.93, 6.06
cx42, cy42 = 12.00, 6.49
cx43, cy43 = 12.12, 6.92
cx44, cy44 = 12.23, 7.28
cx45, cy45 = 12.47, 7.63
cx46, cy46 = 12.63, 7.91
cx47, cy47 = 12.82, 8.11
cx48, cy48 = 12.96, 8.22 
cx49, cy49 = 13.1, 8.38
cx50, cy50 = 13.9, 9.25


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

print(list1)

