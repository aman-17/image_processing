import math

p=10

#xs
xp1, yp1 = 0, 3.93
xp2, yp2 = 1.96, 8.26
xp3, yp3 = 13.77, 8.26
xp4, yp4 = 14.74, 3.93

cx1, cy1 = 1.41, 3.7
cx2, cy2 = 1.81, 3.62
cx3, cy3 = 2.2, 3.50
cx4, cy4 = 2.59, 3.3
cx5, cy5 = 2.95, 3.07
cx6, cy6 = 3.42, 2.71
cx7, cy7 = 3.77, 2.32
cx8, cy8 = 4.05, 2.04
cx9, cy9 = 4.44, 1.57
cx10, cy10 = 4.92, 1.10
cx11, cy11 = 5.47, 0.62
cx12, cy12 = 5.90, 0.39
cx13, cy13 = 6.37, 0.19
cx14, cy14 = 6.88, 0.11
cx15, cy15 = 7.36, 0
cx16, cy16 = 7.95, 0.03
cx17, cy17 = 8.46, 0.11
cx18, cy18 = 8.93, 0.23
cx19, cy19 = 9.44, 0.35
cx20, cy20 = 9.72, 0.5
cx21, cy21 = 10.23, 0.74
cx22, cy22 = 10.62, 1.02
cx23, cy23 = 10.86, 1.37
cx24, cy24 = 11.22, 1.69
cx25, cy25 = 11.49, 2
cx26, cy26 = 11.83, 2.4
cx27, cy27 = 12.20, 2.79
cx28, cy28 = 12.59, 3.18
cx29, cy29 = 12.99, 3.45
cx30, cy30 = 13.42, 3.63
cx31, cy31 = 13.97, 3.83
cx32, cy32 = 14.37, 3.90

cx33, cy33 = 4.92, 8.93
cx34, cy34 = 6.10, 9.17
cx35, cy35 = 8.26, 9.29
cx36, cy36 = 10.43, 9.17 
cx37, cy37 = 11.88, 8.93  

#s
xp1, yp1 = 0, 3.93
xp2, yp2 = 1.96, 8.76
xp3, yp3 = 14.27, 8.76
xp4, yp4 = 15.24, 3.93

cx1, cy1 = 1.41, 3.7
cx2, cy2 = 1.81, 3.62
cx3, cy3 = 2.2, 3.50
cx4, cy4 = 2.59, 3.3
cx5, cy5 = 2.95, 3.07
cx6, cy6 = 3.42, 2.71
cx7, cy7 = 3.77, 2.32
cx8, cy8 = 4.05, 2.04
cx9, cy9 = 4.44, 1.57
cx10, cy10 = 4.92, 1.10
cx11, cy11 = 5.47, 0.62
cx12, cy12 = 5.90, 0.39
cx13, cy13 = 6.37, 0.19
cx14, cy14 = 6.88, 0.11
cx15, cy15 = 7.36, 0
cx16, cy16 = 7.95, 0.03
cx17, cy17 = 8.46, 0.11
cx18, cy18 = 8.93, 0.23
cx19, cy19 = 9.44, 0.35
cx20, cy20 = 9.72, 0.5
cx21, cy21 = 10.23, 0.74
cx22, cy22 = 10.62, 1.02
cx23, cy23 = 10.86, 1.37
cx24, cy24 = 11.22, 1.69
cx25, cy25 = 11.49, 2
cx26, cy26 = 11.83, 2.4
cx27, cy27 = 12.20, 2.79
cx28, cy28 = 12.59, 3.18
cx29, cy29 = 12.99, 3.45
cx30, cy30 = 13.42, 3.63
cx31, cy31 = 13.97, 3.83
cx32, cy32 = 14.37, 3.90

cx33, cy33 = 4.92, 9.09
cx34, cy34 = 6.10, 9.17
cx35, cy35 = 8.26, 9.25
cx36, cy36 = 10.43, 9.17 
cx37, cy37 = 11.88, 8.93

#m
xp1, yp1 = 0, 3.93
xp2, yp2 = 1.96, 8.96
xp3, yp3 = 14.27, 8.96
xp4, yp4 = 15.24, 3.93

cx1, cy1 = 1.41, 3.7
cx2, cy2 = 1.81, 3.62
cx3, cy3 = 2.2, 3.50
cx4, cy4 = 2.59, 3.3
cx5, cy5 = 2.95, 3.07
cx6, cy6 = 3.42, 2.71
cx7, cy7 = 3.77, 2.32
cx8, cy8 = 4.05, 2.04
cx9, cy9 = 4.44, 1.57
cx10, cy10 = 4.92, 1.10
cx11, cy11 = 5.47, 0.62
cx12, cy12 = 5.90, 0.39
cx13, cy13 = 6.37, 0.19
cx14, cy14 = 6.88, 0.11
cx15, cy15 = 7.36, 0
cx16, cy16 = 7.95, 0.03
cx17, cy17 = 8.46, 0.11
cx18, cy18 = 8.93, 0.23
cx19, cy19 = 9.44, 0.35
cx20, cy20 = 9.72, 0.5
cx21, cy21 = 10.23, 0.74
cx22, cy22 = 10.62, 1.02
cx23, cy23 = 10.86, 1.37
cx24, cy24 = 11.22, 1.69
cx25, cy25 = 11.49, 2
cx26, cy26 = 11.83, 2.4
cx27, cy27 = 12.20, 2.79
cx28, cy28 = 12.59, 3.18
cx29, cy29 = 12.99, 3.45
cx30, cy30 = 13.42, 3.63
cx31, cy31 = 13.97, 3.83
cx32, cy32 = 14.37, 3.90

cx33, cy33 = 4.92, 9.09
cx34, cy34 = 6.10, 9.17
cx35, cy35 = 8.26, 9.25
cx36, cy36 = 10.43, 9.17 
cx37, cy37 = 11.88, 8.93

#l
xp1, yp1 = 0, 3.93
xp2, yp2 = 1.96, 8.96
xp3, yp3 = 15.77, 8.96
xp4, yp4 = 17.24, 3.93

cx1, cy1 = 2.41, 3.7
cx2, cy2 = 2.81, 3.62
cx3, cy3 = 3.2, 3.50
cx4, cy4 = 3.59, 3.3
cx5, cy5 = 3.95, 3.07
cx6, cy6 = 4.42, 2.71
cx7, cy7 = 4.77, 2.32
cx8, cy8 = 5.05, 2.04
cx9, cy9 = 5.44, 1.57
cx10, cy10 = 5.92, 1.10
cx11, cy11 = 6.47, 0.62
cx12, cy12 = 6.90, 0.39
cx13, cy13 = 7.37, 0.19
cx14, cy14 = 7.88, 0.11
cx15, cy15 = 8.36, 0
cx16, cy16 = 8.95, 0.03
cx17, cy17 = 9.46, 0.11
cx18, cy18 = 9.93, 0.23
cx19, cy19 = 10.44, 0.35
cx20, cy20 = 10.72, 0.5
cx21, cy21 = 11.23, 0.74
cx22, cy22 = 11.62, 1.02
cx23, cy23 = 11.86, 1.37
cx24, cy24 = 12.22, 1.69
cx25, cy25 = 12.49, 2
cx26, cy26 = 12.83, 2.4
cx27, cy27 = 13.20, 2.79
cx28, cy28 = 13.59, 3.18
cx29, cy29 = 13.99, 3.45
cx30, cy30 = 14.42, 3.63
cx31, cy31 = 14.97, 3.83
cx32, cy32 = 15.37, 3.90

cx33, cy33 = 4.92, 9.09
cx34, cy34 = 6.10, 9.17
cx35, cy35 = 8.26, 9.25
cx36, cy36 = 10.43, 9.17 
cx37, cy37 = 15.98, 8.93    



#xl
xp1, yp1 = 0, 3.93
xp2, yp2 = 1.56, 9.36
xp3, yp3 = 15.77, 9.36
xp4, yp4 = 19.64, 3.93

cx1, cy1 = 3.41, 3.7
cx2, cy2 = 3.81, 3.62
cx3, cy3 = 4.2, 3.50
cx4, cy4 = 4.59, 3.3
cx5, cy5 = 4.95, 3.07
cx6, cy6 = 5.42, 2.71
cx7, cy7 = 5.77, 2.32
cx8, cy8 = 6.05, 2.04
cx9, cy9 = 6.44, 1.57
cx10, cy10 = 6.92, 1.10
cx11, cy11 = 7.47, 0.62
cx12, cy12 = 7.90, 0.39
cx13, cy13 = 8.37, 0.19
cx14, cy14 = 8.88, 0.11
cx15, cy15 = 9.36, 0
cx16, cy16 = 9.95, 0.03
cx17, cy17 = 10.46, 0.11
cx18, cy18 = 10.93, 0.23
cx19, cy19 = 11.44, 0.35
cx20, cy20 = 11.72, 0.5
cx21, cy21 = 12.23, 0.74
cx22, cy22 = 12.62, 1.02
cx23, cy23 = 12.86, 1.37
cx24, cy24 = 13.22, 1.69
cx25, cy25 = 13.49, 2
cx26, cy26 = 13.83, 2.4
cx27, cy27 = 14.20, 2.79
cx28, cy28 = 14.59, 3.18
cx29, cy29 = 14.99, 3.45
cx30, cy30 = 15.42, 3.63
cx31, cy31 = 15.97, 3.83
cx32, cy32 = 16.37, 3.90

cx33, cy33 = 4.92, 9.36
cx34, cy34 = 6.10, 9.36
cx35, cy35 = 8.26, 9.36
cx36, cy36 = 10.43, 9.36
cx37, cy37 = 17.98, 9.36

xcp1=math.ceil(xp1*p)
xcp2=math.ceil(xp2*p)
xcp3=math.ceil(xp3*p)
xcp4=math.ceil(xp4*p)

ycp1=math.ceil(yp1*p)
ycp2=math.ceil(yp2*p)
ycp3=math.ceil(yp3*p)
ycp4=math.ceil(yp4*p)



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


list1=[(0,ycp1),(xcp2,ycp2),(ccx33,ccy33),(ccx34,ccy34),(ccx35,ccy35),(ccx36,ccy36),(ccx37,ccy37),(xcp4,ycp4),(ccx32,ccy32),(ccx31,ccy31),(ccx30,ccy30),
       (ccx29,ccy29),(ccx28,ccy28),(ccx27,ccy27),(ccx26,ccy26),(ccx25,ccy25),(ccx24,ccy24),(ccx23,ccy23),(ccx22,ccy22),(ccx21,ccy21),(ccx20,ccy20),
       (ccx19,ccy19),(ccx18,ccy18),(ccx17,ccy17),(ccx16,ccy16),(ccx15,ccy15),(ccx14,ccy14),(ccx13,ccy13),(ccx12,ccy12),(ccx11,ccy11),(ccx10,ccy10),
       (ccx9,ccy9),(ccx8,ccy8),(ccx7,ccy7),(ccx6,ccy6),(ccx5,ccy5),(ccx4,ccy4),(ccx3,ccy3),(ccx2,ccy2),(ccx1,ccy1)]

print(list1)
