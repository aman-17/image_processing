import math
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")
pixelPermetric=41.96
xsmh2h, xsmh2b, xsmh2xh = 6.508, 2.793, 6.851
xsmch1h, xsmch1b, xsmch1xb = 5.890, 3.116, 3.929
xsmch2h, xsmch2b, xsmch2xb = 6.577, 3.929, 3.510
xsmch3h, xsmch3b, xsmch3xb = 6.375, 3.510, 3.104

'''
"h2": { "h": "6.508", "b": "2.793", "s": "6.851"},
"ch1": { "h": "5.890", "b": "3.116", "s": "3.929"},
"ch2": { "h": "6.577", "b": "3.929", "s": "3.510"},



"h2": { "h": "6.668", "b": "2.793", "s": "7.011"},
"ch1": { "h": "6.389", "b": "3.116", "s": "3.929"},
"ch2": { "h": "6.577", "b": "3.929", "s": "3.510"},
"ch3": { "h": "6.375", "b": "3.510", "s": "3.104"},

'''





if(sex=='m' and size=='xs' and panel_id=='h2'):
    s=0.5+xsmh2b
    x1=pixelPermetric*xsmh2h
    y1=pixelPermetric*xsmh2b
    x2=pixelPermetric*xsmh2xh
    x4=pixelPermetric*s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    c4=math.ceil(x4)
    l=c3-c1
    
    list1=[(0,l),(c4,0),(c2,c3),(0,c3)]
    print(list1)

    list2=[(0,0),(c4,0),(c2,c3),(0,c3)]
    print(list2)

elif(sex=='m' and size=='xs' and panel_id=='ch1'):

    l1=(xsmch1xb-xsmch1b)/2
    x0=pixelPermetric*l1
    x1=pixelPermetric*xsmch1h
    y1=pixelPermetric*xsmch1b
    x2=pixelPermetric*xsmch1xb
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    #l=c3-c2
    
    list1=[(c0,0),(c0+c2,0),(c3,c1),(0,c1)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='ch2'):
    
    x1=pixelPermetric*xsmch2h
    y1=pixelPermetric*xsmch2b
    x2=pixelPermetric*xsmch2xb
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c2-c3
    
    list1=[(0,0),(c2,0),(c2,c1),(l,c1)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='ch3'):
    
    x1=pixelPermetric*xsmch3h
    y1=pixelPermetric*xsmch3b
    x2=pixelPermetric*xsmch3xb
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c2-c3
    
    list1=[(0,0),(c2,0),(c2,c1),(l,c1)]
    print(list1)
