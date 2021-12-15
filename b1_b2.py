import math
import cv2
import numpy as np
#image01 = cv2.imread("1.jpeg")
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")
pixelPermetric=1

#men
xsmb1xh, xsmb1xl, xsmb1xb, xsmb1b, xsmb1h, xsmb1xb1 = 4.59, 4.693, 3.2, 10.877, 3.048, 3.405 #b1
xsmb1xbb, xsmb1xl, xsmb1b, xsmb1h, xsmb1xb1, xsmb1xhh = 3.1, 4.697, 7.075, 3.055, 3.367,4.59 #b2

smb1xh, smb1xl, smb1xb, smb1b, smb1h, smb1xb1 = 4.9, 5.045, 3.55, 11.377, 3.423, 3.760
smb1xbb, smb1xl, smb1b, smb1h, smb1xb1, smb1xhh = 3.52, 5.049, 7.575, 3.43, 3.722, 4.9

mmb1xh, mmb1xl, mmb1xb, mmb1b, mmb1h, mmb1xb1 = 5.3, 5.403, 3.9, 11.877, 3.798, 4.119
mmb1xbb, mmb1xl, mmb1b, mmb1h, mmb1xb1, mmb1xhh = 3.9, 5.407, 8.075, 3.805, 4.082, 5.30

lmb1xh, lmb1xl, lmb1xb, lmb1b, lmb1h, lmb1xb1 = 5.65, 5.766, 4.28, 12.377, 4.173, 4.480
lmb1xbb, lmb1xl, lmb1b, lmb1h, lmb1xb1, lmb1xhh = 4.24, 5.770, 8.575, 4.180, 4.443, 5.67

xlmb1xh, xlmb1xl, xlmb1xb, xlmb1b, xlmb1h, xlmb1xb1 = 6.03, 6.133, 4.64, 12.877, 4.548, 4.843
xlmb1xbb, xlmb1xl, xlmb1b, xlmb1h, xlmb1xb1, xlmb1xhh = 4.6, 6.136, 9.075, 4.555, 4.807, 6.03

txsmb1xh, txsmb1xl, txsmb1xb, txsmb1b, txsmb1h, txsmb1xb1 = 4.59, 4.693, 3.2, 10.877, 3.048, 3.405
txsmb1xbb, txsmb1xl, txsmb1b, txsmb1h, txsmb1xb1, txsmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tsmb1xh, tsmb1xl, tsmb1xb, tsmb1b, tsmb1h, tsmb1xb1 = 4.9, 5.045, 3.55, 11.377, 3.423, 3.760
tsmb1xbb, tsmb1xl, tsmb1b, tsmb1h, tsmb1xb1, tsmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tmmb1xh, tmmb1xl, tmmb1xb, tmmb1b, tmmb1h, tmmb1xb1 = 5.3, 5.403, 3.9, 11.877, 3.798, 4.119
tmmb1xbb, tmmb1xl, tmmb1b, tmmb1h, tmmb1xb1, tmmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tlmb1xh, tlmb1xl, tlmb1xb, tlmb1b, tlmb1h, tlmb1xb1 = 5.65, 5.766, 4.28, 12.377, 4.173, 4.480
tlmb1xbb, tlmb1xl, tlmb1b, tlmb1h, tlmb1xb1, tlmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

txlmb1xh, txlmb1xl, txlmb1xb, txlmb1b, txlmb1h, txlmb1xb1 = 6.03, 6.133, 4.64, 12.877, 4.548, 4.843
txlmb1xbb, txlmb1xl, txlmb1b, txlmb1h, txlmb1xb1, txlmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59



#women


xsfb1xh, xsfb1xl, xsfb1xb, xsfb1b, xsfb1h, xsfb1xb1 = 4.59, 4.693, 2.77, 10.414, 3.048, 2.973
xsfb1xbb, xsfb1xl, xsfb1b, xsfb1h, xsfb1xb1, xsfb1xhh = 2.7, 4.697, 6.584, 3.055, 2.905, 4.59

sfb1xh, sfb1xl, sfb1xb, sfb1b, sfb1h, sfb1xb1 = 4.9, 5.045, 3.12, 10.914, 3.423, 3.322
sfb1xbb, sfb1xl, sfb1b, sfb1h, sfb1xb1, sfb1xhh = 3.055, 5.049, 7.084, 3.43, 3.255, 4.9

mfb1xh, mfb1xl, mfb1xb, mfb1b, mfb1h, mfb1xb1 = 5.3, 5.403, 3.47, 11.414, 3.798, 3.676
mfb1xbb, mfb1xl, mfb1b, mfb1h, mfb1xb1, mfb1xhh = 3.41, 5.407, 7.584, 3.805, 3.610, 5.30

lfb1xh, lfb1xl, lfb1xb, lfb1b, lfb1h, lfb1xb1 = 5.65, 5.766, 3.83, 11.914, 4.173, 4.034
lfb1xbb, lfb1xl, lfb1b, lfb1h, lfb1xb1, lfb1xhh = 3.76, 5.770, 8.084, 4.180, 3.968, 5.67

xlfb1xh, xlfb1xl, xlfb1xb, xlfb1b, xlfb1h, xlfb1xb1 = 6.03, 6.133, 4.19, 12.414, 4.548, 4.395
xlfb1xbb, xlfb1xl, xlfb1b, xlfb1h, xlfb1xb1, xlfb1xhh = 4.12, 6.136, 8.584, 4.555, 4.329, 6.03

txsfb1xh, txsfb1xl, txsfb1xb, txsfb1b, txsfb1h, txsfb1xb1 = 4.59, 4.693, 2.77, 10.414, 3.048, 2.973
txsfb1xbb, txsfb1xl, txsfb1b, txsfb1h, txsfb1xb1, txsfb1xhh = 2.7, 4.697, 6.584, 3.055, 2.905, 4.59

tsfb1xh, tsfb1xl, tsfb1xb, tsfb1b, tsfb1h, tsfb1xb1 = 4.9, 5.045, 3.12, 10.914, 3.423, 3.322
tsfb1xbb, tsfb1xl, tsfb1b, tsfb1h, tsfb1xb1, tsfb1xhh = 3.055, 5.049, 7.084, 3.43, 3.255, 4.9

tmfb1xh, tmfb1xl, tmfb1xb, tmfb1b, tmfb1h, tmfb1xb1 = 5.3, 5.403, 3.47, 11.414, 3.798, 3.676
tmfb1xbb, tmfb1xl, tmfb1b, tmfb1h, tmfb1xb1, tmfb1xhh = 3.41, 5.407, 7.584, 3.805, 3.610, 5.30

tlfb1xh, tlfb1xl, tlfb1xb, tlfb1b, tlfb1h, tlfb1xb1 = 5.65, 5.766, 3.83, 11.914, 4.173, 4.034
tlfb1xbb, tlfb1xl, tlfb1b, tlfb1h, tlfb1xb1, tlfb1xhh = 3.76, 5.770, 8.084, 4.180, 3.968, 5.67

txlfb1xh, txlfb1xl, txlfb1xb, txlfb1b, txlfb1h, txlfb1xb1 = 6.03, 6.133, 4.19, 12.414, 4.548, 4.395
txlfb1xbb, txlfb1xl, txlfb1b, txlfb1h, txlfb1xb1, txlfb1xhh = 4.12, 6.136, 8.584, 4.555, 4.329, 6.03












'''

"b1": {"h1":"4.59", "h2":"4.693", "h3":"3.2", "h4":"10.877", "h5":"3.048", "h6":"3.405"},
"b2": {"h1":"3.1", 4.697, 7.075, 3.055, 3.367,4.59
       
"b1": {"h1":"4.9", "h2":"5.045, 3.55, 11.377, 3.423, 3.760
"b2": {"h1":"3.52, 5.049, 7.575, 3.43, 3.722, 4.9
'''
mmb1xh, mmb1xl, mmb1xb, mmb1b, mmb1h, mmb1xb1 = 5.3, 5.403, 3.9, 11.877, 3.798, 4.119
mmb1xbb, mmb1xl, mmb1b, mmb1h, mmb1xb1, mmb1xhh = 3.9, 5.407, 8.075, 3.805, 4.082, 5.30

lmb1xh, lmb1xl, lmb1xb, lmb1b, lmb1h, lmb1xb1 = 5.65, 5.766, 4.28, 12.377, 4.173, 4.480
lmb1xbb, lmb1xl, lmb1b, lmb1h, lmb1xb1, lmb1xhh = 4.24, 5.770, 8.575, 4.180, 4.443, 5.67

xlmb1xh, xlmb1xl, xlmb1xb, xlmb1b, xlmb1h, xlmb1xb1 = 6.03, 6.133, 4.64, 12.877, 4.548, 4.843
xlmb1xbb, xlmb1xl, xlmb1b, xlmb1h, xlmb1xb1, xlmb1xhh = 4.6, 6.136, 9.075, 4.555, 4.807, 6.03

txsmb1xh, txsmb1xl, txsmb1xb, txsmb1b, txsmb1h, txsmb1xb1 = 4.59, 4.693, 3.2, 10.877, 3.048, 3.405
txsmb1xbb, txsmb1xl, txsmb1b, txsmb1h, txsmb1xb1, txsmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tsmb1xh, tsmb1xl, tsmb1xb, tsmb1b, tsmb1h, tsmb1xb1 = 4.9, 5.045, 3.55, 11.377, 3.423, 3.760
tsmb1xbb, tsmb1xl, tsmb1b, tsmb1h, tsmb1xb1, tsmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tmmb1xh, tmmb1xl, tmmb1xb, tmmb1b, tmmb1h, tmmb1xb1 = 5.3, 5.403, 3.9, 11.877, 3.798, 4.119
tmmb1xbb, tmmb1xl, tmmb1b, tmmb1h, tmmb1xb1, tmmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

tlmb1xh, tlmb1xl, tlmb1xb, tlmb1b, tlmb1h, tlmb1xb1 = 5.65, 5.766, 4.28, 12.377, 4.173, 4.480
tlmb1xbb, tlmb1xl, tlmb1b, tlmb1h, tlmb1xb1, tlmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59

txlmb1xh, txlmb1xl, txlmb1xb, txlmb1b, txlmb1h, txlmb1xb1 = 6.03, 6.133, 4.64, 12.877, 4.548, 4.843
txlmb1xbb, txlmb1xl, txlmb1b, txlmb1h, txlmb1xb1, txlmb1xhh = 3.1, 4.697, 7.705, 3.055, 3.367, 4.59










if(sex=='m' and size=='xs' and panel_id=='b1'):
    xsmb1xh, xsmb1xl, xsmb1xb, xsmb1b, xsmb1h, xsmb1xb1 = 4.59, 4.693, 3.2, 10.877, 3.048, 3.405 #b1
       
    xb0=math.sqrt((xsmb1xb1**2)-(xsmb1xb**2)) #h1
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((xsmb1xl**2)-(xsmb1xh**2)) #b1

    x1=pixelPermetric*xsmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*xsmb1xb
    y1=pixelPermetric*xsmb1b
    x2=pixelPermetric*xsmb1h
    yy1=(xb0+x1)-(xsmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1) #b1
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    
    c7=math.ceil(xxb0) #h1
        
    list1=[(c6,0),(c2+c4,((c7+c1)-c3)),(c2+c4,c1),(c2,c1),(0,c7)]
    print(list1)

    list2=[(0,0),(c2+c4,0),(c2+c4,c1),(0,c1)]
    print(list2)


elif(sex=='m' and size=='xs' and panel_id=='b2'):
    xb0=math.sqrt((xsmb1xb1**2)-(xsmb1xbb**2))
    xb1=math.sqrt((xsmb1xl**2)-(xsmb1xhh**2))
    l=xsmb1b-xsmb1xbb
    l1=xb0+xsmb1xhh
    l2=l1-xsmb1h
    b1=xsmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*xsmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(c6,c2),(c5,c4),(0,c4),(0,c3)]
    print(list1)
    
    list2=[(0,0),(c6,0),(c6,c4),(0,c4)]
    print(list2)
    


elif(sex=='m' and size=='s' and panel_id=='b1'):
    xb0=math.sqrt((smb1xb1**2)-(smb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((smb1xl**2)-(smb1xh**2))

    x1=pixelPermetric*smb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*smb1xb
    y1=pixelPermetric*smb1b
    x2=pixelPermetric*smb1h
    yy1=(xb0+x1)-(smb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='s' and panel_id=='b2'):
    xb0=math.sqrt((smb1xb1**2)-(smb1xbb**2))
    xb1=math.sqrt((smb1xl**2)-(smb1xhh**2))
    l=smb1b-smb1xbb
    l1=xb0+smb1xhh
    l2=l1-smb1h
    b1=smb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*smb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    

elif(sex=='m' and size=='m' and panel_id=='b1'):
    xb0=math.sqrt((mmb1xb1**2)-(mmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((mmb1xl**2)-(mmb1xh**2))

    x1=pixelPermetric*mmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*mmb1xb
    y1=pixelPermetric*mmb1b
    x2=pixelPermetric*mmb1h
    yy1=(xb0+x1)-(mmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='m' and panel_id=='b2'):
    xb0=math.sqrt((mmb1xb1**2)-(mmb1xbb**2))
    xb1=math.sqrt((mmb1xl**2)-(mmb1xhh**2))
    l=mmb1b-mmb1xbb
    l1=xb0+mmb1xhh
    l2=l1-mmb1h
    b1=mmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*mmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
elif(sex=='m' and size=='l' and panel_id=='b1'):
    xb0=math.sqrt((lmb1xb1**2)-(lmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((lmb1xl**2)-(lmb1xh**2))

    x1=pixelPermetric*lmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*lmb1xb
    y1=pixelPermetric*lmb1b
    x2=pixelPermetric*lmb1h
    yy1=(xb0+x1)-(lmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='l' and panel_id=='b2'):
    xb0=math.sqrt((lmb1xb1**2)-(lmb1xbb**2))
    xb1=math.sqrt((lmb1xl**2)-(lmb1xhh**2))
    l=lmb1b-lmb1xbb
    l1=xb0+lmb1xhh
    l2=l1-lmb1h
    b1=lmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*lmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    

elif(sex=='m' and size=='xl' and panel_id=='b1'):
    xb0=math.sqrt((xlmb1xb1**2)-(xlmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((xlmb1xl**2)-(xlmb1xh**2))

    x1=pixelPermetric*xlmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*xlmb1xb
    y1=pixelPermetric*xlmb1b
    x2=pixelPermetric*xlmb1h
    yy1=(xb0+x1)-(xlmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='xl' and panel_id=='b2'):
    xb0=math.sqrt((xlmb1xb1**2)-(xlmb1xbb**2))
    xb1=math.sqrt((xlmb1xl**2)-(xlmb1xhh**2))
    l=xlmb1b-xlmb1xbb
    l1=xb0+xlmb1xhh
    l2=l1-xlmb1h
    b1=xlmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*xlmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    

elif(sex=='m' and size=='txs' and panel_id=='b1'):
    xb0=math.sqrt((txsmb1xb1**2)-(txsmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((txsmb1xl**2)-(txsmb1xh**2))

    x1=pixelPermetric*txsmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*txsmb1xb
    y1=pixelPermetric*txsmb1b
    x2=pixelPermetric*txsmb1h
    yy1=(xb0+x1)-(txsmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='txs' and panel_id=='b2'):
    xb0=math.sqrt((txsmb1xb1**2)-(txsmb1xbb**2))
    xb1=math.sqrt((txsmb1xl**2)-(txsmb1xhh**2))
    l=txsmb1b-txsmb1xbb
    l1=xb0+txsmb1xhh
    l2=l1-txsmb1h
    b1=xsmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*txsmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
    
    

elif(sex=='m' and size=='ts' and panel_id=='b1'):
    xb0=math.sqrt((tsmb1xb1**2)-(tsmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tsmb1xl**2)-(tsmb1xh**2))

    x1=pixelPermetric*tsmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tsmb1xb
    y1=pixelPermetric*tsmb1b
    x2=pixelPermetric*tsmb1h
    yy1=(xb0+x1)-(tsmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='ts' and panel_id=='b2'):
    xb0=math.sqrt((tsmb1xb1**2)-(tsmb1xbb**2))
    xb1=math.sqrt((tsmb1xl**2)-(tsmb1xhh**2))
    l=tsmb1b-tsmb1xbb
    l1=xb0+tsmb1xhh
    l2=l1-tsmb1h
    b1=tsmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tsmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    

    
    
    

elif(sex=='m' and size=='tm' and panel_id=='b1'):
    xb0=math.sqrt((tmmb1xb1**2)-(tmmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tmmb1xl**2)-(tmmb1xh**2))

    x1=pixelPermetric*tmmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tmmb1xb
    y1=pixelPermetric*tmmb1b
    x2=pixelPermetric*tmmb1h
    yy1=(xb0+x1)-(tmmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)   

elif(sex=='m' and size=='tm' and panel_id=='b2'):
    xb0=math.sqrt((tmmb1xb1**2)-(tmmb1xbb**2))
    xb1=math.sqrt((tmmb1xl**2)-(tmmb1xhh**2))
    l=tmmb1b-tmmb1xbb
    l1=xb0+tmmb1xhh
    l2=l1-tmmb1h
    b1=tmmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tmmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
    

elif(sex=='m' and size=='tl' and panel_id=='b1'):
    xb0=math.sqrt((tlmb1xb1**2)-(tlmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tlmb1xl**2)-(tlmb1xh**2))

    x1=pixelPermetric*tlmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tlmb1xb
    y1=pixelPermetric*tlmb1b
    x2=pixelPermetric*tlmb1h
    yy1=(xb0+x1)-(tlmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='m' and size=='tl' and panel_id=='b2'):
    xb0=math.sqrt((tlmb1xb1**2)-(tlmb1xbb**2))
    xb1=math.sqrt((tlmb1xl**2)-(tlmb1xhh**2))
    l=tlmb1b-tlmb1xbb
    l1=xb0+tlmb1xhh
    l2=l1-tlmb1h
    b1=tlmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tlmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    

elif(sex=='m' and size=='txl' and panel_id=='b1'):
    xb0=math.sqrt((txlmb1xb1**2)-(txlmb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((txlmb1xl**2)-(txlmb1xh**2))

    x1=pixelPermetric*txlmb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*txlmb1xb
    y1=pixelPermetric*txlmb1b
    x2=pixelPermetric*txlmb1h
    yy1=(xb0+x1)-(txlmb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)   

elif(sex=='m' and size=='txl' and panel_id=='b2'):
    xb0=math.sqrt((txlmb1xb1**2)-(txlmb1xbb**2))
    xb1=math.sqrt((txlsmb1xl**2)-(txlmb1xhh**2))
    l=txlmb1b-txlmb1xbb
    l1=xb0+txlmb1xhh
    l2=l1-txlmb1h
    b1=txlmb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*txlmb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    ############################################################################
#-------------------------------------women---------------------------------------#
    ############################################################################

elif(sex=='f' and size=='xs' and panel_id=='b1'):
    xb0=math.sqrt((xsfb1xb1**2)-(xsfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((xsfb1xl**2)-(xsfb1xh**2))

    x1=pixelPermetric*xsfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*xsfb1xb
    y1=pixelPermetric*xsfb1b
    x2=pixelPermetric*xsfb1h
    yy1=(xb0+x1)-(xsfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)


elif(sex=='f' and size=='xs' and panel_id=='b2'):
    xb0=math.sqrt((xsfb1xb1**2)-(xsfb1xbb**2))
    xb1=math.sqrt((xsfb1xl**2)-(xsfb1xhh**2))
    l=xsfb1b-xsfb1xbb
    l1=xb0+xsfb1xhh
    l2=l1-xsfb1h
    b1=xsfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*xsfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    


elif(sex=='f' and size=='s' and panel_id=='b1'):
    xb0=math.sqrt((sfb1xb1**2)-(sfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((sfb1xl**2)-(sfb1xh**2))

    x1=pixelPermetric*sfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*sfb1xb
    y1=pixelPermetric*sfb1b
    x2=pixelPermetric*sfb1h
    yy1=(xb0+x1)-(sfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='s' and panel_id=='b2'):
    xb0=math.sqrt((sfb1xb1**2)-(sfb1xbb**2))
    xb1=math.sqrt((sfb1xl**2)-(sfb1xhh**2))
    l=sfb1b-sfb1xbb
    l1=xb0+sfb1xhh
    l2=l1-sfb1h
    b1=sfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*sfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    

elif(sex=='f' and size=='m' and panel_id=='b1'):
    xb0=math.sqrt((mfb1xb1**2)-(mfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((mfb1xl**2)-(mfb1xh**2))

    x1=pixelPermetric*mfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*mfb1xb
    y1=pixelPermetric*mfb1b
    x2=pixelPermetric*mfb1h
    yy1=(xb0+x1)-(mfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='m' and panel_id=='b2'):
    xb0=math.sqrt((mfb1xb1**2)-(mfb1xbb**2))
    xb1=math.sqrt((mfb1xl**2)-(mfb1xhh**2))
    l=mfb1b-mfb1xbb
    l1=xb0+mfb1xhh
    l2=l1-mfb1h
    b1=mfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*mfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
elif(sex=='f' and size=='l' and panel_id=='b1'):
    xb0=math.sqrt((lfb1xb1**2)-(lfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((lfb1xl**2)-(lfb1xh**2))

    x1=pixelPermetric*lfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*lfb1xb
    y1=pixelPermetric*lfb1b
    x2=pixelPermetric*lfb1h
    yy1=(xb0+x1)-(lfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='l' and panel_id=='b2'):
    xb0=math.sqrt((lfb1xb1**2)-(lfb1xbb**2))
    xb1=math.sqrt((lfb1xl**2)-(lfb1xhh**2))
    l=lfb1b-lfb1xbb
    l1=xb0+lfb1xhh
    l2=l1-lfb1h
    b1=lfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*lfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    

elif(sex=='f' and size=='xl' and panel_id=='b1'):
    xb0=math.sqrt((xlfb1xb1**2)-(xlfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((xlfb1xl**2)-(xlfb1xh**2))

    x1=pixelPermetric*xlfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*xlfb1xb
    y1=pixelPermetric*xlfb1b
    x2=pixelPermetric*xlfb1h
    yy1=(xb0+x1)-(xlfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='xl' and panel_id=='b2'):
    xb0=math.sqrt((xlfb1xb1**2)-(xlfb1xbb**2))
    xb1=math.sqrt((xlfb1xl**2)-(xlfb1xhh**2))
    l=xlfb1b-xlfb1xbb
    l1=xb0+xlfb1xhh
    l2=l1-xlfb1h
    b1=xlfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*xlfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    

elif(sex=='f' and size=='txs' and panel_id=='b1'):
    xb0=math.sqrt((txsfb1xb1**2)-(txsfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((txsfb1xl**2)-(txsfb1xh**2))

    x1=pixelPermetric*txsfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*txsfb1xb
    y1=pixelPermetric*txsfb1b
    x2=pixelPermetric*txsfb1h
    yy1=(xb0+x1)-(txsf1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='txs' and panel_id=='b2'):
    xb0=math.sqrt((txsfb1xb1**2)-(txsfb1xbb**2))
    xb1=math.sqrt((txsfb1xl**2)-(txsfb1xhh**2))
    l=txsfb1b-txsfb1xbb
    l1=xb0+txsfb1xhh
    l2=l1-txsfb1h
    b1=xsfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*txsfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
    
    

elif(sex=='f' and size=='ts' and panel_id=='b1'):
    xb0=math.sqrt((tsfb1xb1**2)-(tsfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tsfb1xl**2)-(tsfb1xh**2))

    x1=pixelPermetric*tsfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tsfb1xb
    y1=pixelPermetric*tsfb1b
    x2=pixelPermetric*tsfb1h
    yy1=(xb0+x1)-(tsfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='ts' and panel_id=='b2'):
    xb0=math.sqrt((tsfb1xb1**2)-(tsfb1xbb**2))
    xb1=math.sqrt((tsfb1xl**2)-(tsfb1xhh**2))
    l=tsfb1b-tsfb1xbb
    l1=xb0+tsfb1xhh
    l2=l1-tsfb1h
    b1=tsfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tsfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    

    
    
    

elif(sex=='f' and size=='tm' and panel_id=='b1'):
    xb0=math.sqrt((tmfb1xb1**2)-(tmfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tmfb1xl**2)-(tmfb1xh**2))

    x1=pixelPermetric*tmfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tmfb1xb
    y1=pixelPermetric*tmfb1b
    x2=pixelPermetric*tmfb1h
    yy1=(xb0+x1)-(tmfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)   

elif(sex=='f' and size=='tm' and panel_id=='b2'):
    xb0=math.sqrt((tmfb1xb1**2)-(tmfb1xbb**2))
    xb1=math.sqrt((tmfb1xl**2)-(tmfb1xhh**2))
    l=tmmb1b-tmfb1xbb
    l1=xb0+tmfb1xhh
    l2=l1-tmfb1h
    b1=tmfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tmfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    
    

elif(sex=='f' and size=='tl' and panel_id=='b1'):
    xb0=math.sqrt((tlfb1xb1**2)-(tlfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((tlfb1xl**2)-(tlfb1xh**2))

    x1=pixelPermetric*tlfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*tlfb1xb
    y1=pixelPermetric*tlfb1b
    x2=pixelPermetric*tlfb1h
    yy1=(xb0+x1)-(tlfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)    

elif(sex=='f' and size=='tl' and panel_id=='b2'):
    xb0=math.sqrt((tlfb1xb1**2)-(tlfb1xbb**2))
    xb1=math.sqrt((tlfb1xl**2)-(tlfb1xhh**2))
    l=tlfb1b-tlfb1xbb
    l1=xb0+tlfb1xhh
    l2=l1-tlfb1h
    b1=tlfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*tlfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    
    
    
    

elif(sex=='f' and size=='txl' and panel_id=='b1'):
    xb0=math.sqrt((txlfb1xb1**2)-(txlfb1xb**2))
    xxb0=pixelPermetric*xb0
    xb=math.sqrt((txlfb1xl**2)-(txlfb1xh**2))

    x1=pixelPermetric*txlfb1xh
    xx1=pixelPermetric*xb
    xxx1=pixelPermetric*txlfb1xb
    y1=pixelPermetric*txlfb1b
    x2=pixelPermetric*txlfb1h
    yy1=(xb0+x1)-(txlfb1xb1)
    c1=math.ceil(x1)
    c2=math.ceil(xx1)
    c3=math.ceil(x2)
    c4=math.ceil(y1)
    c5=math.ceil(yy1)
    c6=math.ceil(xxx1)
    c7=math.ceil(xxb0)
        
    list1=[(c6,0),(0,c7),(c2,c1),(c2+c4,c1),(c2+c4,((c7+c1)-c3))]
    print(list1)   

elif(sex=='f' and size=='txl' and panel_id=='b2'):
    xb0=math.sqrt((txlfb1xb1**2)-(txlfb1xbb**2))
    xb1=math.sqrt((txlsfb1xl**2)-(txlfb1xhh**2))
    l=txlfb1b-txlfb1xbb
    l1=xb0+txlfb1xhh
    l2=l1-txlfb1h
    b1=txlfb1b+xb1
    
    x0=pixelPermetric*l
    x1=pixelPermetric*xb0
    x2=pixelPermetric*l2
    x3=pixelPermetric*l1

    y1=pixelPermetric*txlfb1b
    y2=pixelPermetric*b1

    c1=math.ceil(x0)
    c2=math.ceil(x1)
    c3=math.ceil(x2)
    c4=math.ceil(x3)
    c5=math.ceil(y1)
    c6=math.ceil(y2)
    
    list1=[(c1,0),(0,c3),(0,c4),(c5,c4),(c6,c2)]
    print(list1)
    
    


