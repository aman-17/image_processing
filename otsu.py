import cv2 
import numpy as np
import glob
import os
from maxrect import get_maximal_rectangle,rect2poly
from maxrect import get_intersection, get_maximal_rectangle, rect2poly
from matplotlib import pyplot as plt

from skimage.data import page
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)

'''


image = cv2.imread('31.jpeg')
# Otsu's thresholding after Gaussian filtering


# plot all the images and their histograms
#images = [blur, 0, th3]
#plt.subplot(3,3,0*3+3),plt.imshow(images[0*3+2],'gray')

#image = cv2.imread(img) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 

contour, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

#binary_global = image > threshold_otsu(image)

window_size = 25
thresh_niblack = threshold_niblack(image, 25, k=0.8)
print(thresh_niblack)
thresh_sauvola = threshold_sauvola(image, window_size=window_size)

binary_niblack = image > thresh_niblack
binary_sauvola = image > thresh_sauvola


#cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
#blur = cv2.GaussianBlur(image,(5,5),0)

#ret, threshed_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),0,255,cv2.THRESH_BINARY)

#ret, threshed_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret, threshed_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret, threshed_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
                #127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh_niblack, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
contours = contours_sorted[0]
polydp_of_contour = cv2.approxPolyDP(contours, 0.009 * cv2.arcLength(contours, True), True)

cv2.drawContours(image, [polydp_of_contour], 0, (0, 0, 255), 5)
cv2.drawContours(image, [contours], 0, (0, 255, 0), 3)

cv2.imshow('out', image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 

'''
img = cv2.imread('31.jpeg',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
binary_global = img > threshold_otsu(img)

window_size = 25
thresh_niblack = threshold_niblack(img, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(img, window_size=window_size)

binary_niblack = img > thresh_niblack
binary_sauvola = img > thresh_sauvola

#plt.figure(figsize=(8, 7))
#plt.subplot(2, 2, 1)
#plt.imshow(image, cmap=plt.cm.gray)
#plt.title('Original')
#plt.axis('off')

#plt.subplot(2, 2, 2)
#plt.title('Global Threshold')
#plt.imshow(binary_global, cmap=plt.cm.gray)
#plt.axis('off')

#plt.set_dpi(100)
#plt(num=None, figsize=(8, 6), dpi=200, facecolor = 'w', edgecolor = 'k')
#plt.figure(figsize=(10,10))
#plt.subplot(2, 2, 1)
#plt.imshow(binary_niblack, cmap=plt.cm.gray)
#plt.title(' ')
#plt.axis('off')
#plt.savefig('result.jpeg')


#plt.subplot(2, 2, 4)
plt.figure(figsize=(10,10))
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
#plt.title('Sauvola Threshold')
plt.axis('off')
plt.savefig('result1.jpeg')
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]

#plt.subplot(3,3,2*3+3),plt.imshow(images[2*3+2],'gray')


plt.show()

