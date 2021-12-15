import os, sys, glob
import math, imutils, json, cv2, urllib, requests, numpy as np, base64, scipy as sp, scipy.ndimage as nd, matplotlib.pyplot as plt, scipy.misc 
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from skimage import io
from urllib.request import urlopen
from skimage import data 


width=0.955


image_url = "https://i.postimg.cc/W40VmdqW/IMG20210921121433-Warped.jpg"
url = 'https://od-v2.api.dhana.com/models/coin-detection-v2/predict_image_url?image_url=' + image_url
myobj = {'image_url': image_url}
x = requests.post(url ,data = myobj)

bounding_boxes_data=x.json()
final_value=0
final_data=None
result = None
print(bounding_boxes_data['data']['bounding-boxes'][0]['coordinates'])
bounding_box = bounding_boxes_data['data']['bounding-boxes'][0]['coordinates']

req = urllib.request.urlopen(image_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
full_img = cv2.imdecode(arr, -1)


w = bounding_box['right']-bounding_box['left']
h = bounding_box['bottom']-bounding_box['top']
image = full_img[bounding_box['top']:bounding_box['top']+h, bounding_box['left']:bounding_box['left']+w]




def distance_transform(width=0.955,image="img1.jpg") ->None:
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    draw = image[dist_transform == 1] = [255,0,0]
    #dist_transform = dist_transform.T
    binary_matrix = np.sum(dist_transform == 1,axis=1)
    x = dist_transform==1
    count_xcoords=[]
    mean_x = 0
    mean_y = 0
    count_ycoords=[]
    count = 0
    
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]==True:
                mean_x += i
                mean_y += j
                count+=1
                count_xcoords.append(i)
                count_ycoords.append(j)
    mean_x = mean_x // count
    mean_y = mean_y // count
    
    distances=[]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j] == True and mean_x == i:
                distances.append(abs(mean_y-j))

    distancesSorted = sorted([abs(x) for x in distances])
    radius = min(distances)
    print("radius: ",radius)
    #print(img_names)
    pixelperMetric = math.ceil((2*radius)/width)
    print("PPM: ", pixelperMetric)

    cv2.circle(image, (mean_y,mean_x), radius=1, color=(255, 0, 255), thickness=-1)
    cv2.circle(image, (mean_y,mean_x), radius=radius, color=(255, 0, 255), thickness=1)
    cv2.imshow('g_d.jpg', image)
    if cv2.waitKey() & 0xff == 27: quit()
        
    return None

def decide_contour(mean, std, mean_thresh = 100,std_thresh = 40):

    if mean >= mean_thresh and std <= std_thresh:
        # return "wide1"
        return "wide"
    elif mean < mean_thresh and std <= std_thresh:
        # return "wide2"
        return "wide"
    elif std > std_thresh:
        return "tight"

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def panel_digitalisation(b=4.748, h=4.233, pixelperMetric=40):
    
    # img = cv2.imread(full_img)
    gray = cv2.cvtColor(full_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    (cnts, _) = contours.sort_contours(cnts)
    cnts_1=cnts[0]
    detected_circles = cv2.HoughCircles(gray,  
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
                param2 = 30, minRadius = 1, maxRadius = 40)
    pixelsPerMetric = None

    for c in cnts:
        if cv2.contourArea(c) < 100:
            continue
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        (tl, tr, br, bl) = box
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
        if pixelsPerMetric is None:
            pixelsPerMetric = dB / width
            #print(pixelsPerMetric)
            #p=math.floor(pixelsPerMetric)
            #print(p)

    p = pixelperMetric
    print("PPM: ", p)
    l=9.333
    b=13.812
    s=13.433
    

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
    cx19, cy19 = 1, 9.28
    cx20, cy20 = 0.85, 9.44


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

    list1=[(260+c2,300+ycp1),(260+xcp2,300+ycp2),(260+ccx1,300+ccy1),(260+ccx2,300+ccy2),(260+ccx3,300+ccy3),(260+ccx4,300+ccy4),(260+ccx5,300+ccy5),(260+ccx6,300+ccy6),(260+ccx7,300+ccy7),(260+ccx8,300+ccy8),(260+ccx9,300+ccy9),(260+ccx10,300+ccy10),(260+ccx11,300+ccy11),(260+ccx12,300+ccy12),(260+ccx13,300+ccy13),(260+ccx14,300+ccy14),(260+ccx15,300+ccy15),(260+ccx16,300+ccy16)
        ,(260+ccx17,300+ccy17),(260+ccx18,300+ccy18),(260+ccx19,300+ccy19),(260+ccx20,300+ccy20),(260+0,300+c1),(260+c2,300+c1)]
    '''
    panelPoints=[]
    new_points=[]

    #coordinates=Polygon([(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
    #       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)])

    #list1=[(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
    #       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)]

    #list1=[(184, 0), (40, 43), (47, 63), (54, 78), (60, 93), (65, 111), (68, 125), (72, 143),
    #       (75, 163), (77, 175), (76, 187), (74, 199), (72, 213), (70, 224), (68, 234), (66, 246), (61, 257), (58, 265), (51, 278), (42, 288), (33, 295), (24, 301), (0, 311), (184, 311)]


    Q1 = scale(coordinates, xfact = -1, origin = (1, 0))
    panelPoints=(list((Q1.exterior.coords)))
    panelPoints.reverse()
    #print(panelPoints)




    mav_val=0
    for points in panelPoints:
    if points[0]<mav_val:
        mav_val=points[0]

    for points in panelPoints:
    point_x=points[0]-mav_val
    point_y=points[1]
    new_points.append((point_x, point_y))

    print('\n\n')
    print(new_points)

    '''




    img=cv2.line(full_img, list1[0], list1[1], (0,0,0), 2)
    img=cv2.line(full_img, list1[1], list1[2], (0,0,0), 2)
    img=cv2.line(full_img, list1[2], list1[3], (0,0,0), 2)
    img=cv2.line(full_img, list1[3], list1[4], (0,0,0), 2)

    img=cv2.line(full_img, list1[4], list1[5], (0,0,0), 2)

    img=cv2.line(full_img, list1[5], list1[6], (0,0,0), 2)
    img=cv2.line(full_img, list1[6], list1[7], (0,0,0), 2)
    img=cv2.line(full_img, list1[7], list1[8], (0,0,0), 2)
    img=cv2.line(full_img, list1[8], list1[9], (0,0,0), 2)
    img=cv2.line(full_img, list1[9], list1[10], (0,0,0), 2)
    img=cv2.line(full_img, list1[10], list1[11], (0,0,0), 2)
    img=cv2.line(full_img, list1[11], list1[12], (0,0,0), 2)
    img=cv2.line(full_img, list1[12], list1[13], (0,0,0), 2)
    img=cv2.line(full_img, list1[13], list1[14], (0,0,0), 2)
    img=cv2.line(full_img, list1[14], list1[15], (0,0,0), 2)
    img=cv2.line(full_img, list1[15], list1[16], (0,0,0), 2)
    img=cv2.line(full_img, list1[16], list1[17], (0,0,0), 2)
    img=cv2.line(full_img, list1[17], list1[18], (0,0,0), 2)
    img=cv2.line(full_img, list1[18], list1[19], (0,0,0), 2)
    img=cv2.line(full_img, list1[19], list1[20], (0,0,0), 2)
    img=cv2.line(full_img, list1[20], list1[21], (0,0,0), 2)
    img=cv2.line(full_img, list1[21], list1[22], (0,0,0), 2)
    img=cv2.line(full_img, list1[22], list1[23], (0,0,0), 2)
    img=cv2.line(full_img, list1[23], list1[0], (0,0,0), 2)
    '''
    img=cv2.line(full_img, list1[24], list1[25], (0,0,0), 2)
    img=cv2.line(full_img, list1[25], list1[26], (0,0,0), 2)
    img=cv2.line(full_img, list1[26], list1[27], (0,0,0), 2)
    img=cv2.line(full_img, list1[27], list1[28], (0,0,0), 2)
    img=cv2.line(full_img, list1[28], list1[29], (0,0,0), 2)
    img=cv2.line(full_img, list1[29], list1[30], (0,0,0), 2)
    img=cv2.line(full_img, list1[30], list1[31], (0,0,0), 2)
    img=cv2.line(full_img, list1[31], list1[32], (0,0,0), 2)
    img=cv2.line(full_img, list1[32], list1[33], (0,0,0), 2)
    img=cv2.line(full_img, list1[33], list1[34], (0,0,0), 2)
    img=cv2.line(full_img, list1[34], list1[35], (0,0,0), 2)
    img=cv2.line(full_img, list1[35], list1[36], (0,0,0), 2)
    img=cv2.line(full_img, list1[36], list1[37], (0,0,0), 2)
    img=cv2.line(full_img, list1[37], list1[38], (0,0,0), 2)
    img=cv2.line(full_img, list1[38], list1[39], (0,0,0), 2)
    img=cv2.line(full_img, list1[39], list1[40], (0,0,0), 2)
    img=cv2.line(full_img, list1[40], list1[41], (0,0,0), 2)
    img=cv2.line(full_img, list1[41], list1[42], (0,0,0), 2)
    img=cv2.line(full_img, list1[42], list1[43], (0,0,0), 2)
    img=cv2.line(full_img, list1[43], list1[44], (0,0,0), 2)
    img=cv2.line(full_img, list1[44], list1[45], (0,0,0), 2)
    img=cv2.line(full_img, list1[45], list1[46], (0,0,0), 2)
    img=cv2.line(full_img, list1[46], list1[47], (0,0,0), 2)
    img=cv2.line(full_img, list1[47], list1[48], (0,0,0), 2)
    img=cv2.line(full_img, list1[48], list1[49], (0,0,0), 2)
    img=cv2.line(full_img, list1[49], list1[50], (0,0,0), 2)
    img=cv2.line(full_img, list1[50], list1[51], (0,0,0), 2)
    img=cv2.line(full_img, list1[51], list1[52], (0,0,0), 2)
    img=cv2.line(full_img, list1[52], list1[53], (0,0,0), 2)
    img=cv2.line(full_img, list1[53], list1[54], (0,0,0), 2)
    img=cv2.line(full_img, list1[54], list1[0], (0,0,0), 2)
    '''
    cv2.imshow('new-2.jpg', full_img)
    k=cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

def threshold(width=0.955,image="img1.jpg") ->int:
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray.jpg",image_gray)
    # if cv2.waitKey() & 0xff == 27: quit()

    mean, std = image_gray.mean(), image_gray.std()
    chosen_contour = decide_contour(mean, std)
    #print(chosen_contour)
    blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
    # cv2.imshow("blurred.jpg",blurred)
    # if cv2.waitKey() & 0xff == 27: quit()
    wide = cv2.Canny(blurred, 10, 200)
    # cv2.imshow("wide.jpg",wide)
    # if cv2.waitKey() & 0xff == 27: quit()
    mid = cv2.Canny(blurred, 30, 150)
    tight = cv2.Canny(blurred, 240, 250)

    if chosen_contour=="tight":
        _, final_chosen_thresh_image = cv2.threshold(tight, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("_tight.jpg",tight)
        if cv2.waitKey() & 0xff == 27: quit()

    else:
        _, final_chosen_thresh_image = cv2.threshold(wide, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("_wide.jpg",wide)
        if cv2.waitKey() & 0xff == 27: quit()
        # threshold value 127 chosen as most of the values in the image tight are either very close to 255 or to 0
        # set of all points in tight where pixel is white after binarizing it
    r, c = np.where(final_chosen_thresh_image == 255)
    # print(r,c)
    if len(r)==0 or len(c)==0:
        distance_transform(width=0.955,image=image)
    
    else:

        xmin, ymin, xmax, ymax = c.min(), r.min(), c.max(),  r.max()
        img = cv2.rectangle(image,(xmin, ymin),(xmax, ymax),(0,255,0),1)


        pixelperMetric = math.ceil((xmax-xmin)/width)

        print(pixelperMetric)
        cv2.imshow("1_wide.jpg",full_img)
        if cv2.waitKey() & 0xff == 27: quit() 
        
        panel_digitalisation(pixelperMetric=24)
    
    
    
        return pixelperMetric
    return None

distance_transform(0.955,image)


