import math
#xs
h, b =  8.61, 5.33

xp1, yp1 = 4.31, 1.02
xp2, yp2 = 0.25, 8.61

cx1, cy1   = 4.28, 1.26
cx2, cy2   = 4.18, 1.67
cx3, cy3   = 4.09, 2.06
cx4, cy4   = 4.00, 2.46
cx5, cy5   = 3.92, 2.85
cx6, cy6   = 3.85, 3.25
cx7, cy7   = 3.78, 3.64
cx8, cy8   = 3.72, 4.03
cx9, cy9   = 3.67, 4.42
cx10, cy10 = 3.63, 4.87
cx11, cy11 = 3.60, 5.23
cx12, cy12 = 3.59, 5.61
cx13, cy13 = 3.61, 6.00
cx14, cy14 = 3.64, 6.39
cx15, cy15 = 3.71, 6.78
cx16, cy16 = 3.81, 7.18
cx17, cy17 = 3.98, 7.58
cx18, cy18 = 4.25, 7.97
cx19, cy19 = 4.45, 8.17
cx20, cy20 = 4.73, 8.37
cx21, cy21 = 5.08, 8.53

#s
h, b =  9.11, 6.21

xp1, yp1 = 4.80, 1.02
xp2, yp2 = 0.15, 9.11

cx1, cy1   = 4.69, 1.66 
cx2, cy2   = 4.61, 2.07
cx3, cy3   = 4.55, 2.46
cx4, cy4   = 4.48, 2.86
cx5, cy5   = 4.42, 3.25
cx6, cy6   = 4.37, 3.65
cx7, cy7   = 4.32, 4.04
cx8, cy8   = 4.29, 4.43
cx9, cy9   = 4.26, 4.82
cx10, cy10 = 4.25, 5.27
cx11, cy11 = 4.25, 5.63
cx12, cy12 = 4.27, 6.01
cx13, cy13 = 4.30, 6.40
cx14, cy14 = 4.36, 6.79
cx15, cy15 = 4.45, 7.18
cx16, cy16 = 4.59, 7.58
cx17, cy17 = 4.78, 7.98
cx18, cy18 = 5.07, 8.37
cx19, cy19 = 5.28, 8.57
cx20, cy20 = 5.57, 8.79
cx21, cy21 = 5.94, 8.99

#m
h, b =  9.61, 6.83

xp1, yp1 = 4.94, 1.02
xp2, yp2 = 0, 9.61

cx1, cy1   = 4.75, 2.06
cx2, cy2   = 4.69, 2.47
cx3, cy3   = 4.64, 2.86
cx4, cy4   = 4.59, 3.26
cx5, cy5   = 4.55, 3.65
cx6, cy6   = 4.52, 4.05
cx7, cy7   = 4.49, 4.44
cx8, cy8   = 4.48, 4.83
cx9, cy9   = 4.47, 5.22
cx10, cy10 = 4.48, 5.67
cx11, cy11 = 4.51, 6.03
cx12, cy12 = 4.55, 6.41
cx13, cy13 = 4.61, 6.80
cx14, cy14 = 4.69, 7.19
cx15, cy15 = 4.80, 7.58
cx16, cy16 = 4.96, 7.98
cx17, cy17 = 5.27, 8.38
cx18, cy18 = 5.59, 8.77
cx19, cy19 = 5.81, 8.97
cx20, cy20 = 6.11, 9.19
cx21, cy21 = 6.50, 9.39

#l
h, b =  10.11, 7.71

xp1, yp1 = 5.35, 1.02
xp2, yp2 = 0, 10.11

cx1, cy1   = 5.24, 2.46
cx2, cy2   = 5.19, 2.87
cx3, cy3   = 5.15, 3.26
cx4, cy4   = 5.12, 3.66
cx5, cy5   = 5.10, 4.05
cx6, cy6   = 5.08, 4.45
cx7, cy7   = 5.08, 4.84
cx8, cy8   = 5.08, 5.23
cx9, cy9   = 5.10, 5.62
cx10, cy10 = 5.13, 6.07
cx11, cy11 = 5.17, 6.43
cx12, cy12 = 5.23, 6.81
cx13, cy13 = 5.31, 7.20
cx14, cy14 = 5.42, 7.59
cx15, cy15 = 5.56, 7.98
cx16, cy16 = 5.73, 8.38
cx17, cy17 = 5.97, 8.78
cx18, cy18 = 6.30, 9.17
cx19, cy19 = 6.54, 9.37
cx20, cy20 = 6.85, 9.59
cx21, cy21 = 7.26, 9.84

#xl
h, b =  10.61, 8.58

xp1, yp1 = 5.57, 1.02
xp2, yp2 = 0, 10.61

cx1, cy1   = 5.44, 2.76
cx2, cy2   = 5.39, 3.17
cx3, cy3   = 5.35, 3.56
cx4, cy4   = 5.32, 3.96
cx5, cy5   = 5.30, 4.35
cx6, cy6   = 5.28, 4.75
cx7, cy7   = 5.28, 5.14
cx8, cy8   = 5.28, 5.53
cx9, cy9   = 5.30, 5.92
cx10, cy10 = 5.33, 6.37
cx11, cy11 = 5.37, 6.73
cx12, cy12 = 5.43, 7.11
cx13, cy13 = 5.51, 7.50
cx14, cy14 = 5.62, 7.89
cx15, cy15 = 5.76, 8.28
cx16, cy16 = 5.93, 8.68
cx17, cy17 = 6.17, 9.08
cx18, cy18 = 6.50, 9.47
cx19, cy19 = 6.74, 9.67
cx20, cy20 = 7.05, 9.89
cx21, cy21 = 7.46, 10.14


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
ccx21=math.ceil(cx21*p)

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

list1 = [(0,0),(xcp1, ycp1),(ccx1, ccy1),(ccx2, ccy2),(ccx3, ccy3),(ccx4, ccy4),(ccx5, ccy5),(ccx6, ccy6),(ccx7, ccy7),(ccx8, ccy8),(ccx9, ccy9)
,(ccx10, ccy10),(ccx11, ccy11),(ccx12, ccy12),(ccx13, ccy13),(ccx14, ccy14),(ccx15, ccy15),(ccx16, ccy16),(ccx17, ccy17),(ccx18, ccy18),(ccx19, ccy19),(ccx20, ccy20),(ccx21, ccy21),(c2,c1),(xcp2, ycp2),(0,0)]
