import math
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")
pixelPermetric=41.96

xsmf2h, xsmf2b, xsmf2s = 2.550, 3.395, 0.499
xsmb3h, xsmb3b, xsmb3s = 7.102, 4.296, 5.707
xsmb5h, xsmb5b, xsmb5s = 6.294, 4.302, 4.988

smf2h, smf2b, smf2s = 2.800, 3.395, 0.574 
smb3h, smb3b, smb3s = 7.727, 4.296, 6.207
smb5h, smb5b, smb5s = 6.919, 4.302, 5.488

mmf2h, mmf2b, mmf2s = 3.050, 3.395, 0.699 
mmb3h, mmb3b, mmb3s = 8.352, 4.296, 6.707
mmb5h, mmb5b, mmb5s = 7.544, 4.302, 5.988

lmf2h, lmf2b, lmf2s = 3.300, 3.395, 0.824 
lmb3h, lmb3b, lmb3s = 8.977, 4.296, 7.207
lmb5h, lmb5b, lmb5s = 8.169, 4.302, 6.488

xlmf2h, xlmf2b, xlmf2s = 3.550, 3.395, 0.949
xlmb3h, xlmb3b, xlmb3s = 9.602, 4.296, 7.707
xlmb5h, xlmb5b, xlmb5s = 8.794, 4.302, 6.988

txsmf2h, txsmf2b, txsmf2s = 2.550, 3.395, 0.499 
txsmb3h, txsmb3b, txsmb3s = 7.102, 4.296, 5.707
txsmb5h, txsmb5b, txsmb5s = 6.294, 4.302, 4.988

tsmf2h, tsmf2b, tsmf2s = 2.800, 3.395, 0.574  
tsmb3h, tsmb3b, tsmb3s = 7.727, 4.296, 6.207
tsmb5h, tsmb5b, tsmb5s = 6.919, 4.302, 5.488

tmmf2h, tmmf2b, tmsmf2s = 2.550, 3.395, 0.699 
tmmb3h, tmmb3b, tmsmb3s = 8.352, 4.296, 6.707
tmmb5h, tmmb5b, tmsmb5s = 7.544, 4.302, 5.988


tlmf2h, tlmf2b, tlmf2s = 3.300, 3.395, 0.824 
tlmb3h, tlmb3b, tlmb3s = 8.977, 4.296, 7.207
tlmb5h, tlmb5b, tlmb5s = 8.169, 4.302, 6.488

txlmf2h, txlmf2b, txlmf2s = 3.550, 3.395, 0.949 
txlmb3h, txlmb3b, txlmb3s = 9.602, 4.296, 7.707
txlmb5h, txlmb5b, txlmb5s = 8.794, 4.302, 6.988













xsff2h, xsff2b, xsff2s = 2.550, 3.395, 0.499
xsfb3h, xsfb3b, xsfb3s = 6.639, 4.296, 5.243
xsfb5h, xsfb5b, xsfb5s = 5.803, 4.302, 4.497

sff2h, sff2b, sff2s = 2.800, 3.395, 0.574 
sfb3h, sfb3b, sfb3s = 7.264, 4.296, 5.743
sfb5h, sfb5b, sfb5s = 6.428, 4.302, 4.997

mff2h, mff2b, mff2s = 3.050, 3.395, 0.699 
mfb3h, mfb3b, mfb3s = 7.899, 4.296, 6.243
mfb5h, mfb5b, mfb5s = 7.053, 4.302, 5.497

lff2h, lff2b, lff2s = 3.300, 3.395, 0.824 
lfb3h, lfb3b, lfb3s = 8.514, 4.296, 6.743
lfb5h, lfb5b, lfb5s = 7.678, 4.302, 5.997

xlff2h, xlff2b, xlff2s = 3.550, 3.395, 0.949
xlfb3h, xlfb3b, xlfb3s = 9.139, 4.296, 7.243
xlfb5h, xlfb5b, xlfb5s = 8.303, 4.302, 6.497

txsff2h, txsff2b, txsff2s = 2.550, 3.395, 0.499 
txsfb3h, txsfb3b, txsfb3s = 7.102, 4.296, 5.707
txsfb5h, txsfb5b, txsfb5s = 6.294, 4.302, 4.988

tsff2h, tsff2b, tsff2s = 2.800, 3.395, 0.574  
tsfb3h, tsfb3b, tsfb3s = 7.727, 4.296, 6.207
tsfb5h, tsfb5b, tsfb5s = 6.919, 4.302, 5.488

tmff2h, tmff2b, tmsff2s = 2.550, 3.395, 0.699 
tmfb3h, tmfb3b, tmsfb3s = 8.352, 4.296, 6.707
tmfb5h, tmfb5b, tmsfb5s = 7.544, 4.302, 5.988


tlff2h, tlff2b, tlff2s = 3.300, 3.395, 0.824 
tlfb3h, tlfb3b, tlfb3s = 8.977, 4.296, 7.207
tlfb5h, tlfb5b, tlfb5s = 8.169, 4.302, 6.488

txlff2h, txlff2b, txlff2s = 3.550, 3.395, 0.949 
txlfb3h, txlfb3b, txlfb3s = 9.602, 4.296, 7.707
txlfb5h, txlfb5b, txlfb5s = 8.794, 4.302, 6.988





if(sex=='m' and size=='xs' and panel_id=='f2'):
    x1=pixelPermetric*xsmf2h
    y1=pixelPermetric*xsmf2b
    y2=pixelPermetric*xsmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)

    list2=[(0,0),(c2,0),(c2,c1),(0,c1)]
    print(list2)
    
elif(sex=='m' and size=='xs' and panel_id=='b3'):
    x1=pixelPermetric*xsmb3h
    y1=pixelPermetric*xsmb3b
    x2=pixelPermetric*xsmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    list2=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list2)
    
elif(sex=='m' and size=='xs' and panel_id=='b5'):
    x1=pixelPermetric*xsmb5h
    y1=pixelPermetric*xsmb5b
    x2=pixelPermetric*xsmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)

    list2=[(0,0),(c1,0),(c1,c2),(0,c2)]
    print(list2)    
    
elif(sex=='m' and size=='s' and panel_id=='f2'):
    x1=pixelPermetric*smf2h
    y1=pixelPermetric*smf2b
    y2=pixelPermetric*smf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='s' and panel_id=='b3'):
    x1=pixelPermetric*smb3h
    y1=pixelPermetric*smb3b
    x2=pixelPermetric*smb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='s' and panel_id=='b5'):
    x1=pixelPermetric*smb5h
    y1=pixelPermetric*smb5b
    x2=pixelPermetric*smb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='m' and size=='m' and panel_id=='f2'):
    x1=pixelPermetric*mmf2h
    y1=pixelPermetric*mmf2b
    y2=pixelPermetric*mmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='m' and panel_id=='b3'):
    x1=pixelPermetric*mmb3h
    y1=pixelPermetric*mmb3b
    x2=pixelPermetric*mmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='m' and panel_id=='b5'):
    x1=pixelPermetric*mmb5h
    y1=pixelPermetric*mmb5b
    x2=pixelPermetric*mmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='m' and size=='l' and panel_id=='f2'):
    x1=pixelPermetric*lmf2h
    y1=pixelPermetric*lmf2b
    y2=pixelPermetric*lmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='l' and panel_id=='b3'):
    x1=pixelPermetric*lmb3h
    y1=pixelPermetric*lmb3b
    x2=pixelPermetric*lmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='l' and panel_id=='b5'):
    x1=pixelPermetric*lmb5h
    y1=pixelPermetric*lmb5b
    y2=pixelPermetric*lmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='m' and size=='xl' and panel_id=='f2'):
    x1=pixelPermetric*xlmf2h
    y1=pixelPermetric*xlmf2b
    y2=pixelPermetric*xlmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='xl' and panel_id=='b3'):
    x1=pixelPermetric*xlmb3h
    y1=pixelPermetric*xlmb3b
    x2=pixelPermetric*xlmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='xl' and panel_id=='b5'):
    x1=pixelPermetric*xlmb5h
    y1=pixelPermetric*xlmb5b
    x2=pixelPermetric*xlmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='m' and size=='txs' and panel_id=='f2'):
    x1=pixelPermetric*txsmf2h
    y1=pixelPermetric*txsmf2b
    y2=pixelPermetric*txsmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='txs' and panel_id=='b3'):
    x1=pixelPermetric*txsmb3h
    y1=pixelPermetric*txsmb3b
    x2=pixelPermetric*txsmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='txs' and panel_id=='b5'):
    x1=pixelPermetric*txsmb5h
    y1=pixelPermetric*txsmb5b
    x2=pixelPermetric*txsmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
elif(sex=='m' and size=='ts' and panel_id=='f2'):
    x1=pixelPermetric*tsmf2h
    y1=pixelPermetric*tsmf2b
    y2=pixelPermetric*tsmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='ts' and panel_id=='b3'):
    x1=pixelPermetric*tsmb3h
    y1=pixelPermetric*tsmb3b
    x2=pixelPermetric*tsmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='ts' and panel_id=='b5'):
    x1=pixelPermetric*tsmb5h
    y1=pixelPermetric*tsmb5b
    x2=pixelPermetric*tsmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='m' and size=='tm' and panel_id=='f2'):
    x1=pixelPermetric*tmmf2h
    y1=pixelPermetric*tmmf2b
    y2=pixelPermetric*tmmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='tm' and panel_id=='b3'):
    x1=pixelPermetric*tmmb3h
    y1=pixelPermetric*tmmb3b
    x2=pixelPermetric*tmmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='tm' and panel_id=='b5'):
    x1=pixelPermetric*tmmb5h
    y1=pixelPermetric*tmmb5b
    x2=pixelPermetric*tmmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
elif(sex=='m' and size=='tl' and panel_id=='f2'):
    x1=pixelPermetric*tlmf2h
    y1=pixelPermetric*tlmf2b
    y2=pixelPermetric*tlmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='tl' and panel_id=='b3'):
    x1=pixelPermetric*tlmb3h
    y1=pixelPermetric*tlmb3b
    x2=pixelPermetric*tlmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='tl' and panel_id=='b5'):
    x1=pixelPermetric*tlmb3h
    y1=pixelPermetric*tlmb3b
    x2=pixelPermetric*tlmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
elif(sex=='m' and size=='txl' and panel_id=='f2'):
    x1=pixelPermetric*txlmf2h
    y1=pixelPermetric*txlmf2b
    y2=pixelPermetric*txlmf2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='m' and size=='txl' and panel_id=='b3'):
    x1=pixelPermetric*txlmb3h
    y1=pixelPermetric*txlmb3b
    x2=pixelPermetric*txlmb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='txl' and panel_id=='b5'):
    x1=pixelPermetric*txlmb5h
    y1=pixelPermetric*txlmb5b
    x2=pixelPermetric*txlmb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

    
############################################################
    #------------women------------#
############################################################



elif(sex=='f' and size=='xs' and panel_id=='f2'):
    x1=pixelPermetric*xsff2h
    y1=pixelPermetric*xsff2b
    y2=pixelPermetric*xsff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='xs' and panel_id=='b3'):
    x1=pixelPermetric*xsfb3h
    y1=pixelPermetric*xsfb3b
    x2=pixelPermetric*xsfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='xs' and panel_id=='b5'):
    x1=pixelPermetric*xsfb5h
    y1=pixelPermetric*xsfb5b
    x2=pixelPermetric*xsfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    

    
    
    
    
elif(sex=='f' and size=='s' and panel_id=='f2'):
    x1=pixelPermetric*sff2h
    y1=pixelPermetric*sff2b
    y2=pixelPermetric*sff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='s' and panel_id=='b3'):
    x1=pixelPermetric*sfb3h
    y1=pixelPermetric*sfb3b
    x2=pixelPermetric*sfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='s' and panel_id=='b5'):
    x1=pixelPermetric*sfb5h
    y1=pixelPermetric*sfb5b
    x2=pixelPermetric*sfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='f' and size=='m' and panel_id=='f2'):
    x1=pixelPermetric*mff2h
    y1=pixelPermetric*mff2b
    y2=pixelPermetric*mff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='m' and panel_id=='b3'):
    x1=pixelPermetric*mfb3h
    y1=pixelPermetric*mfb3b
    x2=pixelPermetric*mfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='m' and panel_id=='b5'):
    x1=pixelPermetric*mfb5h
    y1=pixelPermetric*mfb5b
    x2=pixelPermetric*mfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='f' and size=='l' and panel_id=='f2'):
    x1=pixelPermetric*lff2h
    y1=pixelPermetric*lff2b
    y2=pixelPermetric*lff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='l' and panel_id=='b3'):
    x1=pixelPermetric*lfb3h
    y1=pixelPermetric*lfb3b
    x2=pixelPermetric*lfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='l' and panel_id=='b5'):
    x1=pixelPermetric*lfb5h
    y1=pixelPermetric*lfb5b
    y2=pixelPermetric*lfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='f' and size=='xl' and panel_id=='f2'):
    x1=pixelPermetric*xlff2h
    y1=pixelPermetric*xlff2b
    y2=pixelPermetric*xlff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='xl' and panel_id=='b3'):
    x1=pixelPermetric*xlfb3h
    y1=pixelPermetric*xlfb3b
    x2=pixelPermetric*xlfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='xl' and panel_id=='b5'):
    x1=pixelPermetric*xlfb5h
    y1=pixelPermetric*xlfb5b
    x2=pixelPermetric*xlfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='f' and size=='txs' and panel_id=='f2'):
    x1=pixelPermetric*txsff2h
    y1=pixelPermetric*txsff2b
    y2=pixelPermetric*txsff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='txs' and panel_id=='b3'):
    x1=pixelPermetric*txsfb3h
    y1=pixelPermetric*txsfb3b
    x2=pixelPermetric*txsfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='txs' and panel_id=='b5'):
    x1=pixelPermetric*txsfb5h
    y1=pixelPermetric*txsfb5b
    x2=pixelPermetric*txsfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
elif(sex=='f' and size=='ts' and panel_id=='f2'):
    x1=pixelPermetric*tsff2h
    y1=pixelPermetric*tsff2b
    y2=pixelPermetric*tsff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='ts' and panel_id=='b3'):
    x1=pixelPermetric*tsfb3h
    y1=pixelPermetric*tsfb3b
    x2=pixelPermetric*tsfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='ts' and panel_id=='b5'):
    x1=pixelPermetric*tsfb5h
    y1=pixelPermetric*tsfb5b
    x2=pixelPermetric*tsfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
    
elif(sex=='f' and size=='tm' and panel_id=='f2'):
    x1=pixelPermetric*tmff2h
    y1=pixelPermetric*tmff2b
    y2=pixelPermetric*tmff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='tm' and panel_id=='b3'):
    x1=pixelPermetric*tmfb3h
    y1=pixelPermetric*tmfb3b
    x2=pixelPermetric*tmfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='tm' and panel_id=='b5'):
    x1=pixelPermetric*tmfb5h
    y1=pixelPermetric*tmfb5b
    x2=pixelPermetric*tmfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
    
elif(sex=='f' and size=='tl' and panel_id=='f2'):
    x1=pixelPermetric*tlff2h
    y1=pixelPermetric*tlff2b
    y2=pixelPermetric*tlff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='tl' and panel_id=='b3'):
    x1=pixelPermetric*tlfb3h
    y1=pixelPermetric*tlfb3b
    x2=pixelPermetric*tlfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='tl' and panel_id=='b5'):
    x1=pixelPermetric*tlfb3h
    y1=pixelPermetric*tlfb3b
    x2=pixelPermetric*tlfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)
    
    
    
    
    
    
elif(sex=='f' and size=='txl' and panel_id=='f2'):
    x1=pixelPermetric*txlff2h
    y1=pixelPermetric*txlff2b
    y2=pixelPermetric*txlff2s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(y2)
    
    list1=[(0,0),(c2,(c1-c3)),(c2,c1),(0,c1)]
    print(list1)
    #crop_img = image[200:c1, 350:c2]  
    #cv2.imshow("cropped", image02)
elif(sex=='f' and size=='txl' and panel_id=='b3'):
    x1=pixelPermetric*txlfb3h
    y1=pixelPermetric*txlfb3b
    x2=pixelPermetric*txlfb3s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    l=c1-c3
    
    list1=[(l,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    

elif(sex=='f' and size=='txl' and panel_id=='b5'):
    x1=pixelPermetric*txlfb5h
    y1=pixelPermetric*txlfb5b
    x2=pixelPermetric*txlfb5s
    c1=math.ceil(x1)
    c2=math.ceil(y1)
    c3=math.ceil(x2)
    
    list1=[(0,0),(c3,0),(c1,c2),(0,c2)]
    print(list1)    
