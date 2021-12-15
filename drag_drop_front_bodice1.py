import math

p=10

#xs
h, b = 8.614, 5.087 

xp1, yp1 = 5.47,0
xp2, yp2 = 1.09, 1.18


cx1, cy1 = 1.3, 1.73
cx2, cy2 = 1.5, 2.16
cx3, cy3 = 1.66, 2.57
cx4, cy4 = 1.79, 3.07
cx5, cy5 = 1.87, 3.46
cx6, cy6 = 1.99, 3.97
cx7, cy7 = 2.08, 4.52
cx8, cy8 = 2.12, 4.84
cx9, cy9 = 2.11, 5.19
cx10, cy10 = 2.05, 5.51
cx11, cy11 = 1.99, 5.90
cx12, cy12 = 1.92, 6.22
cx13, cy13 = 1.88, 6.49
cx14, cy14 = 1.81, 6.81
cx15, cy15 = 1.69, 7.12
cx16, cy16 = 1.61, 7.36
cx17, cy17 = 1.41, 7.71
cx18, cy18 = 1.14, 7.99
cx19, cy19 = 0.9, 8.18
cx20, cy20 = 0.65, 8.34


#s
h, b = 9.111, 5.962 

xp1, yp1 = 5.47,0
xp2, yp2 = 1.19, 1.18


cx1, cy1 = 1.4, 1.73
cx2, cy2 = 1.6, 2.16
cx3, cy3 = 1.76, 2.57
cx4, cy4 = 1.89, 3.07
cx5, cy5 = 1.97, 3.46
cx6, cy6 = 2.09, 3.97
cx7, cy7 = 2.18, 4.52
cx8, cy8 = 2.22, 4.84
cx9, cy9 = 2.21, 5.19
cx10, cy10 = 2.15, 5.51
cx11, cy11 = 2.09, 5.90
cx12, cy12 = 1.99, 6.22
cx13, cy13 = 1.92, 6.49
cx14, cy14 = 1.83, 6.81
cx15, cy15 = 1.69, 7.12
cx16, cy16 = 1.61, 7.36
cx17, cy17 = 1.41, 7.71
cx18, cy18 = 1.14, 7.99
cx19, cy19 = 1.0, 8.18
cx20, cy20 = 0.85, 8.34

#m
h, b = 9.610, 6.837 

xp1, yp1 = 5.47,0
xp2, yp2 = 2.0, 1.18


cx1, cy1 = 2.21, 1.73
cx2, cy2 = 2.35, 2.16
cx3, cy3 = 2.4, 2.57
cx4, cy4 = 2.45, 3.07
cx5, cy5 = 2.51, 3.46
cx6, cy6 = 2.55, 3.97
cx7, cy7 = 2.58, 4.52
cx8, cy8 = 2.62, 4.84
cx9, cy9 = 2.61, 5.19
cx10, cy10 = 2.55, 5.51
cx11, cy11 = 2.49, 5.90
cx12, cy12 = 2.29, 6.62
cx13, cy13 = 2.19, 6.89
cx14, cy14 = 1.92, 7.41
cx15, cy15 = 1.69, 7.72
cx16, cy16 = 1.61, 7.96
cx17, cy17 = 1.41, 8.31
cx18, cy18 = 1.14, 8.59
cx19, cy19 = 1.0, 8.78
cx20, cy20 = 0.85, 8.94

#l
h, b = 10.111, 7.712 

xp1, yp1 = 5.47,0
xp2, yp2 = 2.2, 1.18


cx1, cy1 = 2.29, 1.73
cx2, cy2 = 2.35, 2.16
cx3, cy3 = 2.4, 2.57
cx4, cy4 = 2.45, 3.07
cx5, cy5 = 2.51, 3.46
cx6, cy6 = 2.55, 3.97
cx7, cy7 = 2.58, 4.52
cx8, cy8 = 2.62, 4.84
cx9, cy9 = 2.61, 5.19
cx10, cy10 = 2.55, 5.71
cx11, cy11 = 2.49, 6.30
cx12, cy12 = 2.29, 7.12
cx13, cy13 = 2.19, 7.39
cx14, cy14 = 1.92, 7.91
cx15, cy15 = 1.72, 8.22
cx16, cy16 = 1.61, 8.46
cx17, cy17 = 1.43, 8.81
cx18, cy18 = 1.18, 9.09
cx19, cy19 = 1.0, 9.28
cx20, cy20 = 0.85, 9.44


#xl
h, b = 10.613, 8.587 

xp1, yp1 = 5.47,0
xp2, yp2 = 2.3, 1.18


cx1, cy1 = 2.34, 1.73
cx2, cy2 = 2.35, 2.16
cx3, cy3 = 2.38, 2.57
cx4, cy4 = 2.41, 3.07
cx5, cy5 = 2.45, 3.46
cx6, cy6 = 2.50, 3.97
cx7, cy7 = 2.53, 4.52
cx8, cy8 = 2.58, 4.84
cx9, cy9 = 2.55, 5.19
cx10, cy10 = 2.52, 5.91
cx11, cy11 = 2.49, 6.50
cx12, cy12 = 2.29, 7.32
cx13, cy13 = 2.19, 7.59
cx14, cy14 = 1.92, 8.11
cx15, cy15 = 1.76, 8.42
cx16, cy16 = 1.61, 8.66
cx17, cy17 = 1.43, 9.01
cx18, cy18 = 1.18, 9.29
cx19, cy19 = 1.0, 9.48
cx20, cy20 = 0.85, 9.64

xcp1=math.ceil(xp1*p)
xcp2=math.ceil(xp2*p)

ycp1=math.ceil(yp1*p)
ycp2=math.ceil(yp2*p)


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

list1=[(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)]

print(list1)
