import math
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")
pixelPermetric=41.96

#xs
xsmf1xh, xsmf1xb, xsmf1s, xsmf1h, xsmf1b = 0.8, 3.484, 1.108, 7.883, 4.683
xsmh3h, xsmh3b, xsmh3xb, xsmh3s = 6.289, 2.793, 0.393, 2.827
h, b = 12.771, 2.199
#s
smf1xh, smf1xb, smf1s, smf1h, smf1b = 0.99, 3.840, 1.199, 8.133, 5.308
smh3h, smh3b, smh3xb, smh3s = 6.289, 2.793, 1.455, 2.827
h, b = 12.958, 2.443
#m



'''

"f1": {"h1":"0.8","h2":"3.484", 1.108, 7.883, 4.683
"h3": {6.289, 2.793, 1.455, 2.827
"h1": {12.771, 2.199

'''



if(sex=='m' and size=='xs' and panel_id=='f1'):

    
    l0=math.sqrt((xsmf1xb**2)-(xsmf1xh**2))
    l1=xsmf1b-l0
    l2=math.sqrt((xsmf1s**2)-(xsmf1xh**2))
    l3=xsmf1h+xsmf1xh
    l4=xsmf1b+l2
    x0=pixelPermetric*(l0+l1)
    x1=pixelPermetric*l0
    x2=pixelPermetric*l1
    x3=pixelPermetric*l2
    y1=pixelPermetric*xsmf1xh
    y2=pixelPermetric*l3
    y3=pixelPermetric*xsmf1b
    y4=pixelPermetric*l4
    
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    c3=math.ceil(y1)
    c4=math.ceil(y2)
    c5=math.ceil(y3)
    c6=math.ceil(y4)

    list1=[(c0,0),(c6,c3),(c6,c4),(0,c4),(c2,c3)]
    print(list1)

    list2=[(0,0),(c6,0),(c6,c4),(0,c4)]
    print(list2)   

elif(sex=='m' and size=='xs' and panel_id=='h3'):
    
    
    l=xsmh3b+xsmh3s
    x0=pixelPermetric*xsmh3h
    x1=pixelPermetric*xsmh3b
    x2=pixelPermetric*l
    x3=pixelPermetric*xsmh3xb
    
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    c3=math.ceil(x3)
    
    list1=[(0,0),(c1,0),(c2,(c0-c3)),(c2,c0),(0,c0)]
    print(list1)

    list2=[(0,0),(c2,0),(c2,c0),(0,c0)]
    print(list2)

elif(sex=='m' and size=='xs' and panel_id=='h1'):

    
    l=h*0.35
    x0=pixelPermetric*h
    x1=pixelPermetric*b
    x2=pixelPermetric*l
    
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    
    list1=[(c2,0),(c2,c0),((c2-c1),c0),(0,c2)]
    print(list1)

    list2=[(0,0),(c2,0),(c2,c0),(0,c0)]
    print(list2)
  
