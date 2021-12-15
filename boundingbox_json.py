import os, sys, glob
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

for filename in glob.glob('BoundingBoxDataset/*.jpg'):
    print(filename)
    image_url='https://ik.imagekit.io/2360uyb96/demo/preview/38c2baf2-6a53-4674-ad32-cc3f1e9eefc2'
    url = 'https://od-v2.api.dhana.com/models/coin-detection-v2/predict?input_data=' + filename
    myobj = {'input_data': filename}
    x = requests.post(url ,data = myobj)
    print(x)

    bounding_boxes_data=x.json()
    print(bounding_boxes_data)
    final_value=0
    final_data=None
    result = None
    print(bounding_boxes_data['data']['bounding-boxes'][0]['coordinates'])
    bounding_box = bounding_boxes_data['data']['bounding-boxes'][0]['coordinates']
    # Data to be written
    dictionary ={
        "image" : filename,
        "right" : bounding_box['right'],
        "left" : bounding_box['left'],
        "top" : bounding_box['top'],
        "bottom": bounding_box['bottom']
    }
   
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
  
# Writing to sample.json
with open("boundingbox_dataset.json", "w") as outfile:
    outfile.write(json_object)