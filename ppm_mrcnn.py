from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import math
from shapely.affinity import scale
from shapely.ops import transform
from shapely.geometry import Polygon
import json
from pprint import pprint
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os, glob, requests
import random


width = 0.955
medium = 29


def getTshirtBoundriesMRCNN(image):
    url = 'https://mrcnn-fast-api-dev01.cloud.dsphere.network/predict_bounding_box_url?image_url=' + image
    myobj = {'image_url': image}
    x = requests.post(url , data = myobj)
    bounding_boxes_data=x.json()
    final_data=bounding_boxes_data['message'][0]
    return final_data

def pixelPerMetric(image):
    boundingBox = getTshirtBoundriesMRCNN(image)
    pixelPerMetric = math.ceil((boundingBox[2] - boundingBox[0])/medium)
    print(pixelPerMetric)
    return pixelPerMetric

pixelPerMetric("https://i.postimg.cc/MKRmKPDx/test3.jpg")



