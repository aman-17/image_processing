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

# width=0.955
def YOLOImageURL():
    image_url='http://api.demo.dhana.com/api/v1/asset/preview/b39bbd10-b4f9-465b-973f-fcd9682d3b07'
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


    w = bounding_box['right']-bounding_box['left']
    h = bounding_box['bottom']-bounding_box['top']
    image = img[bounding_box['top']:bounding_box['top']+h, bounding_box['left']:bounding_box['left']+w]

    cv2.imwrite('output1.jpg',image)
    # if cv2.waitKey() & 0xff == 27: quit()
    return None

def YOLOImageUpload(filename):
    # assert(os.path.isfile(filename))
    url = 'https://od-v2.api.dhana.com/models/coin-detection-v2/predict?input_data=' + filename
    name_img= os.path.basename(filename)
    files= {'input_data': (name_img, open(filename,'rb'),'image/jpeg') }
    x = requests.post(url, files = files)
    bounding_boxes_data=x.json()
    final_value=0
    final_data=None
    if 'data' in bounding_boxes_data and bounding_boxes_data['data'] is not None and "bounding-boxes" in bounding_boxes_data['data']:
        if len(bounding_boxes_data['data']['bounding-boxes']):
            # Filter and get the bounding_boxes with highest confidence value
            for box in bounding_boxes_data['data']['bounding-boxes']:
                if box['confidence']>final_value:
                    final_value=box['confidence']
                    final_data=box['coordinates']
                    print(final_data)
    return final_data

# filename = cv2.imread("test9.jpg")
# filename = "test9.jpg"
# YOLOImageUpload(filename)
YOLOImageURL()