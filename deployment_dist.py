import os, sys, glob
import math, imutils, json, cv2, urllib, requests, numpy as np, base64, scipy as sp, scipy.ndimage as nd, matplotlib.pyplot as plt, scipy.misc 
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from skimage import io
from urllib.request import urlopen
from skimage import data 


def distance_transform(width=0.955) ->None:
    images = []
    for img in glob.glob("CamouflageDataset/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
    #image= cv2.imread("111.png")
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
        cv2.imshow(img_names+'g_d.jpg', image)
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

def threshold(width=0.955) ->int:
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("CamouflageDataset/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
    #image = cv2.imread("111.png")
        #cv2.imshow("sd", image)
        #if cv2.waitKey() & 0xff == 27: quit()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mean, std = image_gray.mean(), image_gray.std()
        chosen_contour = decide_contour(mean, std)
        #print(chosen_contour)
        blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
        wide = cv2.Canny(blurred, 10, 200)
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
        xmin, ymin, xmax, ymax = c.min(), r.min(), c.max(),  r.max()
        img = cv2.rectangle(image,(xmin, ymin),(xmax, ymax),(0,255,0),1)
        

        pixelperMetric = math.ceil((xmax-xmin)/width)
        print(pixelperMetric)
        cv2.imshow(img_names+"1_wide.jpg",img)
        if cv2.waitKey() & 0xff == 27: quit() 
    
    return pixelperMetric
    
threshold()

