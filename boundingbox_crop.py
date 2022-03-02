import os, sys, glob
import math, imutils, json, cv2, urllib, requests, numpy as np, base64, scipy as sp, scipy.ndimage as nd, matplotlib.pyplot as plt, scipy.misc 
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from skimage import io
from urllib.request import urlopen
from skimage import data 


width=0.955


def houghcircle() ->None:
    
    # image_url='https://ik.imagekit.io/2360uyb96/demo/preview/79b756c3-bb5c-4eb1-9d56-62bc1a719a26'
    # url = 'https://od-v2.api.dhana.com/models/coin-detection-v2/predict_image_url?image_url=' + image_url
    # myobj = {'image_url': image_url}
    # x = requests.post(url ,data = myobj)

    # bounding_boxes_data=x.json()
    # final_value=0
    # final_data=None
    # result = None
    # print(bounding_boxes_data['data']['bounding-boxes'][0]['coordinates'])
    # bounding_box = bounding_boxes_data['data']['bounding-boxes'][0]['coordinates']

    # req = urllib.request.urlopen(image_url)
    # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    # img = cv2.imdecode(arr, -1)


    # w = bounding_box['right']-bounding_box['left']
    # h = bounding_box['bottom']-bounding_box['top']
    # image = img[bounding_box['top']:bounding_box['top']+h, bounding_box['left']:bounding_box['left']+w]
    images = []
    for img in glob.glob("BoundingboxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        #print(image)
        images.append(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        gray = cv2.blur(gray, (5, 5))
        detected_circles = cv2.HoughCircles(gray, 
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                    param2 = 30, minRadius = 10, maxRadius = 40)

        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
                print(math.ceil((2*r)/width))
                cv2.circle(image, (a, b), r, (0, 255, 0), 1)
                # Draw a small circle (of radius 1) to show the center.
                #cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
                cv2.imwrite(img_names+".jpg", image)
                #if cv2.waitKey() & 0xff == 27: quit()

                   

                   
def laplace_of_gaussian(gray_img, sigma=0.25, kappa=0.5, pad=False):
    """
    Applies Laplacian of Gaussians to grayscale image.

    :param gray_img: image to apply LoG to
    :param sigma:    Gauss sigma of Gaussian applied to image, <= 0. for none
    :param kappa:    difference threshold as factor to mean of image values, <= 0 for none
    :param pad:      flag to pad output w/ zero border, keeping input image size
    """
    assert len(gray_img.shape) == 2
    img = cv2.GaussianBlur(gray_img, (0, 0), sigma) if 0. < sigma else gray_img
    img = cv2.Laplacian(img, cv2.CV_64F)
    rows, cols = img.shape[:2]
    # min/max of 3x3-neighbourhoods
    min_map = np.minimum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    max_map = np.maximum.reduce(list(img[r:rows-2+r, c:cols-2+c]
                                     for r in range(3) for c in range(3)))
    # bool matrix for image value positiv (w/out border pixels)
    pos_img = 0 < img[1:rows-1, 1:cols-1]
    # bool matrix for min < 0 and 0 < image pixel
    neg_min = min_map < 0
    neg_min[1 - pos_img] = 0
    # bool matrix for 0 < max and image pixel < 0
    pos_max = 0 < max_map
    pos_max[pos_img] = 0
    # sign change at pixel?
    zero_cross = neg_min + pos_max
    # values: max - min, scaled to 0--255; set to 0 for no sign change
    value_scale = 255. / max(1., img.max() - img.min())
    values = value_scale * (max_map - min_map)
    values[1 - zero_cross] = 0.
    # optional thresholding
    if 0. <= kappa:
        thresh = float(np.absolute(img).mean()) * kappa
        values[values < thresh] = 0.
    log_img = values.astype(np.uint8)
    if pad:
        log_img = np.pad(log_img, pad_width=1, mode='constant', constant_values=0)
    return log_img


def log_houghcircle() ->None:

    images = []
    for img in glob.glob("CamouflageDataset/*.png"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = laplace_of_gaussian(gray)
        #gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        gray = cv2.blur(gray, (3, 3))
        detected_circles = cv2.HoughCircles(gray, 
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                    param2 = 30, minRadius = 10, maxRadius = 40)

        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
                print(math.ceil((2*r)/width))
                cv2.circle(image, (a, b), r, (0, 255, 0), 1)
                # Draw a small circle (of radius 1) to show the center.
                #cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
                cv2.imwrite(img_names+".jpg", image)
                #if cv2.waitKey() & 0xff == 27: quit()


def log_contour() ->None:
    images = []
    for img in glob.glob("BoundingBoxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #         cv2.THRESH_BINARY_INV,11,2)
        # gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        gray = cv2.blur(gray, (3, 3))
        # edged = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
        # edged = cv2.Canny(gray, 50, 100)
        # edged = cv2.dilate(edged, None, iterations=1)
        # edged = cv2.erode(edged, None, iterations=1)
        #log = laplace_of_gaussian(gray)
        cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        (cnts, _) = contours.sort_contours(cnts)
        image1 = cv2.drawContours(image, cnts, -1, (0, 255, 0), 1)
        pixelsPerMetric = None

        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
        for c in cnts:
            if cv2.contourArea(c) > 10:

                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                box = perspective.order_points(box)
                (tl, tr, br, bl) = box
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                cv2.circle(image1, (int(tltrX), int(tltrY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(blbrX), int(blbrY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(tlblX), int(tlblY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(trbrX), int(trbrY)), 1, (255, 0, 0), 1)
                # draw lines between the midpoints
                cv2.line(image1, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                    (255, 0, 255), 1)
                cv2.line(image1, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                    (255, 0, 255), 1)

                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                if pixelsPerMetric is None:
                    pixelsPerMetric = dB / width
                    print(math.floor(pixelsPerMetric))
                    
                

                cv2.imwrite(img_names+'.jpg',image)
                #if cv2.waitKey() & 0xff == 27: quit()


def denoise()->None:
    images = []
    for img in glob.glob("BoundingboxDataset/*.jpg"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)
        #dst = cv2.fastNlMeansDenoisingColored(image,None,5,5,7,21)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #         cv2.THRESH_BINARY_INV,11,2)
        # gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        gray = cv2.blur(gray, (3, 3))
        gray = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
        edged = cv2.Canny(gray, 50, 100)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contourCnts = imutils.grab_contours(cnts)
        (contourCntSort, _) = contours.sort_contours(contourCnts)
        pixelsPerMetric = None


        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
        for c in contourCntSort:
            if cv2.contourArea(c) > 10:

                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                box = perspective.order_points(box)
                (tl, tr, br, bl) = box
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                cv2.circle(image, (int(tltrX), int(tltrY)), 1, (255, 0, 0), 1)
                cv2.circle(image, (int(blbrX), int(blbrY)), 1, (255, 0, 0), 1)
                cv2.circle(image, (int(tlblX), int(tlblY)), 1, (255, 0, 0), 1)
                cv2.circle(image, (int(trbrX), int(trbrY)), 1, (255, 0, 0), 1)
                # draw lines between the midpoints
                cv2.line(image, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                    (255, 0, 255), 1)
                cv2.line(image, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                    (255, 0, 255), 1)

                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                if pixelsPerMetric is None:
                    pixelsPerMetric = dB / width
                    print(math.floor(pixelsPerMetric))
                    
                

                cv2.imwrite(img_names+'.jpg',image)
                #if cv2.waitKey() & 0xff == 27: quit()


def grabcut() ->None:
    images = []
    for img in glob.glob("BoundingboxDataset/*.jpg"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)
        mask = np.zeros(image.shape[:2],np.uint8)
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        rect = (50,50,450,290)
        cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        image = image*mask2[:,:,np.newaxis]
        cv2.imshow(img_names+'.jpg',image)
        if cv2.waitKey() & 0xff == 27: quit()


def colour_segmentation() ->None:
    images = []
    for img in glob.glob("BoundingboxDataset/*.jpg"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)
        lowerBound=np.array([33,80,40])
        upperBound=np.array([102,255,255])

        #cam= cv2.VideoCapture(0)
        kernelOpen=np.ones((5,5))
        kernelClose=np.ones((20,20))

        #font=cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

        while True:
            #ret, img=image.read()
            #img=cv2.resize(img,(340,220))

            #convert BGR to HSV
            imgHSV= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            # create the Mask
            mask=cv2.inRange(imgHSV,lowerBound,upperBound)
            #morphology
            maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
            maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

            maskFinal=maskClose
            conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            
            cv2.drawContours(image,conts,-1,(255,0,0),3)
            for i in range(len(conts)):
                x,y,w,h=cv2.boundingRect(conts[i])
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255), 2)
                cv2.cv.PutText(cv2.cv.fromarray(image), str(i+1),(x,y+h),(0,255,255))
            cv2.imshow("maskClose",maskClose)
            cv2.imshow("maskOpen",maskOpen)
            cv2.imshow("mask",mask)
            cv2.imshow("cam",image)
            if cv2.waitKey() & 0xff == 27: quit()


def watershed() ->None:
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("BoundingboxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        #print(img_names)   
        image= cv2.imread(img)
        images.append(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), cv2.BORDER_DEFAULT)
        #gray = cv2.blur(gray, (9, 9))
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # noise removal
        kernel = np.ones((3,3),np.uint8)
        opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
        
        # sure background area
        sure_bg = cv2.dilate(opening,kernel,iterations=3)
        
        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
        cv2.imshow("out",dist_transform)
        if cv2.waitKey() & 0xff == 27: quit()
        draw = image[dist_transform == 1] = [255,0,0]
        ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    
        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg,sure_fg)
        # Marker labelling
        ret, markers = cv2.connectedComponents(sure_fg)
        
        # Add one to all labels so that sure background is not 0, but 1
        markers = markers+1
        
        # Now, mark the region of unknown with zero
        markers[unknown==255] = 0
        markers = cv2.watershed(image,markers)
        #image[markers == -1] = [255,0,0]
        markers1 = markers.astype(np.uint8)
        cnts = cv2.findContours(dist_transform.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        (cnts, _) = contours.sort_contours(cnts)
        image1 = cv2.drawContours(image, cnts, -1, (0, 255, 0), 1)
        pixelsPerMetric = None

        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
        for c in cnts:
            if cv2.contourArea(c) > 10:

                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                box = perspective.order_points(box)
                (tl, tr, br, bl) = box
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                cv2.circle(image1, (int(tltrX), int(tltrY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(blbrX), int(blbrY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(tlblX), int(tlblY)), 1, (255, 0, 0), 1)
                cv2.circle(image1, (int(trbrX), int(trbrY)), 1, (255, 0, 0), 1)
                # draw lines between the midpoints
                cv2.line(image1, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                    (255, 0, 255), 1)
                cv2.line(image1, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                    (255, 0, 255), 1)

                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                if pixelsPerMetric is None:
                    pixelsPerMetric = dB / width
                    print(math.floor(pixelsPerMetric))
                    cv2.imshow(img_names+'.jpg',image)
                    if cv2.waitKey() & 0xff == 27: quit()


def distance_transform() ->None:
    images = []
    #image = cv2.imread("output1.png")
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    # for img in glob.glob("descaledBoundingboxQuarter/*"):
    #     img_names = os.path.basename(img).split(".")[0]
    #     image= cv2.imread(img)
    #     images.append(image)
        
    image= cv2.imread("output1.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    #gray = cv2.blur(gray, (9, 9))
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)

    draw = image[dist_transform == 1] = [255,0,0]
    #dist_transform = dist_transform.T
    #print(dist_transform)
    binary_matrix = np.sum(dist_transform == 1,axis=1)
    cv2.imshow("asa", dist_transform)
    if cv2.waitKey() & 0xff == 27: quit() 
    x = dist_transform==1
    # #print(x)
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
    #print(mean_x,mean_y)
    final_ycoords=[]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j] == True and mean_y == j:
                final_ycoords.append(i)
                #print(x[j])
    #     if x[i]==True and mean_ycoords==i:
    #         final_ycoords.append(i)
    #print(final_ycoords)

    # find the mean x coordinate and mean y coordinates of all the TRUE points.
    # take y coordinates of the mean and find all the TRUE points which has the same y coordinates. [set of coordinates]
    # cal dist. of those points[set of coordinates] with mean, and take the points which has a smallest distance(which will be the coin) and subtract them to get the radius. 
    first , last = None, None
    for i in range(len(binary_matrix)):
        if binary_matrix[i]>0:
            first = i
            break

    for j in range(len(binary_matrix)-1,0,-1):
        if binary_matrix[j]>0:
            last = j
            break

    pixelperMetric = (math.ceil((last-first)/width))
    print(pixelperMetric)
    return None


def threshold() ->None:
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    # for img in glob.glob("descaledBoundingboxQuarter/*"):
    #     img_names = os.path.basename(img).split(".")[0]
    #     image= cv2.imread(img)
    #     images.append(image)
    image = cv2.imread("output1.jpg")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean, std = image_gray.mean(), image_gray.std()
    chosen_contour = decide_contour(mean, std)
    blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)

    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 240, 250)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
    tight = cv2.dilate(tight, kernel)
    #_, cnts, _ = cv2.findContours(tight.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if chosen_contour=="tight":
        _, final_chosen_thresh_image = cv2.threshold(tight, 127, 255, cv2.THRESH_BINARY)
    
    else:
        _, final_chosen_thresh_image = cv2.threshold(wide, 127, 255, cv2.THRESH_BINARY)

        # threshold value 127 chosen as most of the values in the image tight are either very close to 255 or to 0
        # set of all points in tight where pixel is white after binarizing it
    r, c = np.where(final_chosen_thresh_image == 255)
    xmin, ymin, xmax, ymax = c.min(), r.min(), c.max(),  r.max()

    #print(xmax-xmin) #width of the coin.
    # [xmin, ymin, xmax, ymax] are the tight bounding box coordinates around the coin

    img = cv2.rectangle(image,(xmin, ymin),(xmax, ymax),(0,255,0),1)
    cv2.imshow('_box.jpg', img)
    # cv2.imshow("normal"+img_names+'.jpg',image)
    if cv2.waitKey() & 0xff == 27: quit()


def decide_contour(mean, std, mean_thresh = 100,std_thresh = 40):

    if mean >= mean_thresh and std <= std_thresh:
        # return "wide1"
        return "wide"
    elif mean < mean_thresh and std <= std_thresh:
        # return "wide2"
        return "wide"
    elif std > std_thresh:
        return "tight"


def contrast() ->None:

    img = cv2.imread('test.jpg', 1)
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    # cv2.imshow('CLAHE output', cl)
    # if cv2.waitKey() & 0xff == 27: quit()

    limg = cv2.merge((cl,a,b))
    # cv2.imshow('limg', limg)
    # if cv2.waitKey() & 0xff == 27: quit()

    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    # cv2.imshow('final', final)
    # if cv2.waitKey() & 0xff == 27: quit()


def getContours(img, imgContour):    

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    finalContours = []
    
    # for each contour found
    for cnt in contours:
        # find its area in pixel^2
        area = cv2.contourArea(cnt)
        print("Contour area: ", area)

        # fixed assuming you are searching for the biggest object
        # value can be found via previous print
        minArea = 18000
        
        if (area > minArea):

            perimeter = cv2.arcLength(cnt, False)
            
            # smaller epsilon -> more vertices detected [= more precision]
            # improving bounding box precision - original value 0.02 * perimeter
            epsilon = 0.002*perimeter
            # check how many vertices         
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            print(len(approx))
            
            finalContours.append([len(approx), area, approx, cnt])

    # leaving this part if you have more objects to detect
    # not needed when minArea has been chosen to detect only one object
    # sorting the final results in descending order depending on the area
    finalContours = sorted(finalContours, key = lambda x:x[1], reverse=True)
    print("Final Contours number: ", len(finalContours))
    
    for con in finalContours:
        cv2.drawContours(imgContour, con[3], -1, (0, 0, 255), 3)

    return imgContour, finalContours


def hsv():
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("descaledBoundingboxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
        #object_image = cv2.imread("test1.png")

        # hsv_image = cv2.cvtColor(object_image, cv2.COLOR_BGR2HSV)
        # cv2.imshow('HSV Image', hsv_image)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_white = np.array([180,180,180])
        higher_white = np.array([255,255,255])
        white_range = cv2.inRange(hsv, lower_white, higher_white)
        

        cv2.imwrite(img_names+"_hsv1.jpg", white_range)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def hsvContours():
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("descaledBoundingboxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        cnts = cv2.findContours(hsv.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        (cnts, _) = contours.sort_contours(cnts)
        cv2.drawContours(image, cnts, -1, (0, 255, 0), 1)
        cv2.imshow(img_names+"_hsv1.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def dilation():
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("threshold_contours/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
        kernel = np.ones((2,2), np.uint8)

        img_erosion = cv2.erode(image, kernel, iterations=2)
        img_dilation = cv2.dilate(image, kernel, iterations=1)
        
        #cv2.imshow('Input', img)
        #cv2.imwrite(img_names+"_erode.jpg", img_erosion)
        cv2.imwrite(img_names+'_dilate.jpg', img_dilation)


def main(argv):
    default_file = '7.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_GRAYSCALE)
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    dst = cv2.Canny(src, 50, 200, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    
    lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    
    
    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
    
    cv2.imshow("Source", src)
    #cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
    cv2.waitKey()
    return 0

# if __name__ == "__main__":
#     main(sys.argv[1:])
#distance_transform()

def dilate_erode():

    img = cv2.imread("test.png")
    # img.shape gives back height, width, color in this order
    original_height, original_width, color = img.shape 
    print('Original Dimensions : ', original_width, original_height)

    # resizing to see the entire image
    scale_percent = 30
    width = int(original_width * scale_percent / 100)
    height = int(original_height * scale_percent / 100)
    print('Resized Dimensions : ', width, height)

    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Starting image", resized)
    cv2.waitKey()

    # blurring
    imgBlur = cv2.GaussianBlur(resized, (7, 7), 1)
    # graying
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    # inizialing thresholds
    threshold1 = 14
    threshold2 = 17

    # canny
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    # showing the last produced result
    cv2.imshow("Canny", imgCanny)
    cv2.waitKey()

    kernel = np.ones((2, 2))
    imgDil = cv2.dilate(imgCanny, kernel, iterations = 3)
    imgThre = cv2.erode(imgDil, kernel, iterations = 3)

    imgFinalContours, finalContours = getContours(imgThre, resized)

    # show the contours on the unfiltered resized image
    cv2.imshow("Final Contours", imgFinalContours)
    cv2.waitKey()
    cv2.destroyAllWindows()


def canny():
    images = ["test.png"]
    for scale_percent in range(30,51,5):
        for threshold1 in range(5, 21):
            for threshold2 in range(10,31):
                for gauss_kernel in range(1,11,2):
                    for std in [0,1,2]:
                        for kernel_size in range(2,6):
                            for iterations_dialation in [2,3]:
                                for iterations_erosion in [2,3]:
                                    for img in images:
                                        name = img[3:]
                                        img = cv2.imread(img)

                                        original_height, original_width, color = img.shape 
                                        width = int(original_width * scale_percent / 100)
                                        height = int(original_height * scale_percent / 100)

                                        dim = (width, height)
                                        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

                                        imgBlur = cv2.GaussianBlur(resized, (gauss_kernel, gauss_kernel), std)

                                        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

                                        imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

                                        plt.subplot(231),plt.imshow(resized), plt.axis('off')
                                        plt.title('Original '+ str(name))    

                                        plt.subplot(232),plt.imshow(imgCanny,cmap = 'gray')
                                        plt.title('Canny Edge-detector\n thr1 = {}, thr2 = {}'.format(threshold1, threshold2)), plt.axis('off')

                                        kernel_s = (kernel_size, kernel_size)
                                        kernel = np.ones(kernel_s)

                                        imgDil = cv2.dilate(imgCanny, kernel, iterations = iterations_dialation)
                                        plt.subplot(233),plt.imshow(imgDil, cmap = 'gray'), plt.axis('off')
                                        plt.title("Dilated\n({},{}) iterations = {}".format(kernel_size, kernel_size,
                                                                                            iterations_dialation))

                                        kernel_erosion = np.ones(())
                                        imgThre = cv2.erode(imgDil, kernel, iterations = iterations_erosion)
                                        plt.subplot(234),plt.imshow(imgThre, cmap = 'gray'), plt.axis('off')
                                        plt.title('Eroded\n({},{}) iterations = {}'.format(kernel_size, kernel_size, 
                                                                                        iterations_erosion))

                                        imgFinalContours, finalContours = getContours(imgThre, resized)

                                        plt.subplot(235), plt.axis('off')
                                        plt.title("Contours")

                                        plt.subplot(236), plt.axis('off')
                                        plt.title('Contours')

                                        plt.tight_layout(pad = 0.1)

                                        plt.imshow(imgFinalContours) 

                                    #  plt.savefig("my/results/"
                                    #              +name[:6]+"_scale_percent({})".format(scale_percent)+
                                    #              "_threshold1({})".format(threshold1)
                                    #             +"_threshold2({})".format(threshold2)
                                    #             +"_gauss_kernel({})".format(gauss_kernel)
                                    #             +"_std({})".format(std)
                                    #             +"_kernel_size({})".format(kernel_size)
                                    #             +"_iterations_dialation({})".format(iterations_dialation)
                                    #             +"_iterations_erosion({})".format(iterations_erosion)
                                    #             +".jpg")
                                        plt.title(name)


def ar_ppm():
    realWorldwidthlist = [(14,598),(141,598),(100,472),(14,472)]
    widthInPixelslist = [5.11,5.11,5.11,5.11]
    realWorldWidth = realWorldwidthlist[1][0] - realWorldwidthlist[0][0]
    widthInPixels = widthInPixelslist[1]
    # print(realWorldWidth)
    # print(widthInPixels)
    pixelPerMetric = realWorldWidth//widthInPixels

    return pixelPerMetric
#ar_ppm()

def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect
    

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped


def four_transform():
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("AngledImages/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
        # image = cv2.imread("test12.jpg")
        height, width = image.shape[:2]
        print("Height: ", height, " Width: ", width)
        height = height//1.5
        # width = width//2
        pts = np.array(eval("[(0, 0), (%d, 0), (0, %d), (%d, %d)]"%(width,height,width,height)), dtype = "float32")
        # print(pts)
        
        warped = four_point_transform(image, pts)

        cv2.imshow("Original", image)
        cv2.imwrite("Warped.jpg", warped)
        cv2.waitKey(0)
        os.remove("Warped.jpg")
    return None

threshold()