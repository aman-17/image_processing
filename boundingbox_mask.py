import os, sys
import math
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import imutils
from skimage import io
import numpy as np
import json
import cv2
import urllib
import requests
from urllib.request import urlopen
import base64
import urllib


width=0.955
image_url='https://i.postimg.cc/vHX5ddTt/1mb1.png'
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
img = cv2.imdecode(arr, -1)

width = bounding_box['right']-bounding_box['left']
height = bounding_box['bottom']-bounding_box['top']


mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (bounding_box['left'], bounding_box['top']), (bounding_box['right'], bounding_box['bottom']), 255, -1)
masked_image = cv2.bitwise_and(img, img, mask=mask)
gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)
image1 = cv2.drawContours(masked_image, cnts, -1, (0, 255, 0), 1)

cv2.imshow('output',masked_image)

#cv2.imwrite('output.jpg',masked_image)
if cv2.waitKey() & 0xff == 27: quit()
