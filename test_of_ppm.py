pixelsPerMetric  =41.96     
xsmf5h, xsmf5b = 1.717, 7.389
xsmf6h, xsmf6b = 2.966, 7.411
xsmf7h, xsmf7b = 4.662, 7.564
xsmf8h, xsmf8b = 3.416, 14.933
xsmf3h, xsmf3b = 3.395, 2.750
xsmf4h, xsmf4b = 3.395, 2.579
xsmb4h, xsmb4b = 7.258, 4.302
xsmb6h, xsmb6b = 7.104, 5.089
xsmb7h, xsmb7b = 7.258, 8.679
xsmb8h, xsmb8b = 6.294, 8.679
xsmb9h, xsmb9b = 7.103, 9.820
xsmb10h, xsmb10b = 4.681, 6.233
xsmb11h, xsmb11b = 4.748, 6.233
xsmb12h, xsmb12b = 4.136, 6.238
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")

if(sex=='m' and size=='xs' and panel_id=='f5'):
    x=pixelsPerMetric*xsmf5h
    y=pixelsPerMetric*xsmf5b
    c1=math.ceil(x)
    c2=math.ceil(y)
            #list0=[(0,0),(xsmf5h,0),(xsmf5h, xsmf5b),(0,xsmf5b)]
    print(list0)
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)
'''
            c11=350+c2
            c22=400+c1
            crop_img = image[350:c11, 400:c22]
            cv2.imshow("out", image01)
            cv2.imshow("cropped", crop_img)
            k=cv2.waitKey(0) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
'''
elif(sex=='m' and size=='xs' and panel_id=='f6'):
    x=pixelPermetric*xsmf6h
    y=pixelPermetric*xsmf6b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)    

elif(sex=='m' and size=='xs' and panel_id=='f7'):
    x=pixelPermetric*xsmf7h
    y=pixelPermetric*xsmf7b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='f8'):
    x=pixelPermetric*xsmf8h
    y=pixelPermetric*xsmf8b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='f3'):
    x=pixelPermetric*xsmf3h
    y=pixelPermetric*xsmf3b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='f4'):
    x=pixelPermetric*xsmf4h
    y=pixelPermetric*xsmf4b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)


elif(sex=='m' and size=='xs' and panel_id=='b4'):
    x=pixelPermetric*xsmb4h
    y=pixelPermetric*xsmb4b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b6'):
    x=pixelPermetric*xsmb6h
    y=pixelPermetric*xsmb6b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b7'):
    x=pixelPermetric*xsmb7h
    y=pixelPermetric*xsmb7b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b8'):
    x=pixelPermetric*xsmb8h
    y=pixelPermetric*xsmb8b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b9'):
    x=pixelPermetric*xsmb9h
    y=pixelPermetric*xsmb9b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b10'):
    x=pixelPermetric*xsmb10h
    y=pixelPermetric*xsmb10b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b11'):
    x=pixelPermetric*xsmb11h
    y=pixelPermetric*xsmb11b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='b12'):
    x=pixelPermetric*xsmb12h
    y=pixelPermetric*xsmb12b
    c1=math.ceil(x)
    c2=math.ceil(y)
    
    list1=[(0,0),(0+c1,0),(0+c1,0+c2),(0,c2)]
    print(list1)