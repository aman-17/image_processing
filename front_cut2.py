import math

p=10

s = 12.931
b = 8.272
h = 18.835


xp1, yp1 = 4.48, 0
xp2, yp2 = 0.78, 1.37
xp3, yp3 = 0, 9.13
xp4, yp4 = 8.272, 3.54

cx1, cy1 = 1.61, 6.45
cx2, cy2 = 1.65, 6.73
cx3, cy3 = 1.66, 6.96
cx4, cy4 = 1.65, 7.59
cx5, cy5 = 1.56, 8.22
cx6, cy6 = 1.54, 8.34
cx7, cy7 = 1.42, 8.54
cx8, cy8 = 1.14, 8.75
cx9, cy9 = 0.86, 8.86
cx10, cy10 = 0.39, 9.05

cx11, cy11 = 7.95, 3.43
cx12, cy12 = 7.48, 3.25
cx13, cy13 = 6.96, 3.00
cx14, cy14 = 6.60, 2.70

y1=math.ceil(p*h)
x1=math.ceil(p*b)
y2=math.ceil(p*s)

px1=math.ceil(p*xp1)
px2=math.ceil(p*xp2)
px3=math.ceil(p*xp3)
px4=math.ceil(p*xp4)

py1=math.ceil(p*yp1)
py2=math.ceil(p*yp2)
py3=math.ceil(p*yp3)
py4=math.ceil(p*yp4)

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

list1=[(px1,py1),(px2,py2),(xc1,yc1),(xc2,yc2),(xc3,yc3),(xc4,yc4),(xc5,yc5),(xc6,yc6),(xc7,yc7),(xc8,yc8),(xc9,yc9),(xc10,yc10),(px3,py3),(0,py3+y2),(x1,py3+y2),(x1,py4),(xc11,yc11),(xc12,yc12),(xc13,yc13),(xc14,yc14)]
print(list1)
