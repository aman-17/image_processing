import re
from turtle import width
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
import os, glob


width=0.955
path_xml = '/Users/amanrangapur/Desktop/labels/'
path = '/Users/amanrangapur/Desktop/labels/*png'
images = []
areas = []
for img in glob.glob(path):
    img_names = os.path.basename(img).split(".")[0]
    image= cv2.imread(img)
    images.append(image)
    xml_path = img_names+".xml"
    tree = ET.parse(path_xml+xml_path)
    root = tree.getroot()
    xmin = (root[5][4][0].text)
    # print("xmin: ",xmin)

    xmax = (root[5][4][2].text)
    # print("xmax: ",xmax)

    pixelsPerMetric=math.ceil((int(xmax)-int(xmin))/width)
    print(pixelsPerMetric)
    f = open('dh-34-panel.json')
    data = json.load(f)
    d=data["xs"]["f"]["h3"]


    c0=math.ceil(pixelsPerMetric*float(d['h']))
    c1=math.ceil(pixelsPerMetric*float(d['b']))

    ccx1=math.ceil(pixelsPerMetric*float(d['cx1']))
    ccx2=math.ceil(pixelsPerMetric*float(d['cx2']))
    ccx3=math.ceil(pixelsPerMetric*float(d['cx3']))
    ccx4=math.ceil(pixelsPerMetric*float(d['cx4']))
    ccx5=math.ceil(pixelsPerMetric*float(d['cx5']))
    ccx6=math.ceil(pixelsPerMetric*float(d['cx6']))
    ccx7=math.ceil(pixelsPerMetric*float(d['cx7']))
    ccx8=math.ceil(pixelsPerMetric*float(d['cx8']))
    ccx9=math.ceil(pixelsPerMetric*float(d['cx9']))
    ccx10=math.ceil(pixelsPerMetric*float(d['cx10']))
    ccx11=math.ceil(pixelsPerMetric*float(d['cx11']))
    ccx12=math.ceil(pixelsPerMetric*float(d['cx12']))
    ccx13=math.ceil(pixelsPerMetric*float(d['cx13']))
    ccx14=math.ceil(pixelsPerMetric*float(d['cx14']))
    ccx15=math.ceil(pixelsPerMetric*float(d['cx15']))
    ccx16=math.ceil(pixelsPerMetric*float(d['cx16']))

    ccy1=math.ceil(pixelsPerMetric*float(d['cy1']))
    ccy2=math.ceil(pixelsPerMetric*float(d['cy2']))
    ccy3=math.ceil(pixelsPerMetric*float(d['cy3']))
    ccy4=math.ceil(pixelsPerMetric*float(d['cy4']))
    ccy5=math.ceil(pixelsPerMetric*float(d['cy5']))
    ccy6=math.ceil(pixelsPerMetric*float(d['cy6']))
    ccy7=math.ceil(pixelsPerMetric*float(d['cy7']))
    ccy8=math.ceil(pixelsPerMetric*float(d['cy8']))
    ccy9=math.ceil(pixelsPerMetric*float(d['cy9']))
    ccy10=math.ceil(pixelsPerMetric*float(d['cy10']))
    ccy11=math.ceil(pixelsPerMetric*float(d['cy11']))
    ccy12=math.ceil(pixelsPerMetric*float(d['cy12']))
    ccy13=math.ceil(pixelsPerMetric*float(d['cy13']))
    ccy14=math.ceil(pixelsPerMetric*float(d['cy14']))
    ccy15=math.ceil(pixelsPerMetric*float(d['cy15']))
    ccy16=math.ceil(pixelsPerMetric*float(d['cy16']))
    list1=[(0,0),(0,c0),(ccx16,ccy16),(ccx15,ccy15),(ccx14,ccy14),(ccx13,ccy13),(ccx12,ccy12),
    (ccx11,ccy11),(ccx10,ccy10),(ccx9,ccy9),(ccx8,ccy8),(ccx7,ccy7),(ccx6,ccy6),(ccx5,ccy5),
    (ccx4,ccy4),(ccx3,ccy3),(ccx2,ccy2),(ccx1,ccy1),(c1,0)]

    # A = [0,0]
    # B = [4.328,0]
    # C = [4.217,7.389]
    # D = [0,7.393]

    vertices = [[0,0],[0,c0],[ccx16,ccy16],[ccx15,ccy15],[ccx14,ccy14],[ccx13,ccy13],[ccx12,ccy12],
    [ccx11,ccy11],[ccx10,ccy10],[ccx9,ccy9],[ccx8,ccy8],[ccx7,ccy7],[ccx6,ccy6],[ccx5,ccy5],
    [ccx4,ccy4],[ccx3,ccy3],[ccx2,ccy2],[ccx1,ccy1],[c1,0]]

    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0
    
    for i in range(0,numberOfVertices-1):
        sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
        sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
    
    
    sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
    
    sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
    
    area = math.ceil(abs(sum1 - sum2) / 2)
    areas.append(area)

print("Max Area: ",max(areas))
print("Min Area: ",min(areas))

    # print("Area: ",area)



    # image=cv2.line(image, list1[0], list1[1], (0,255,0), 6)
    # image=cv2.line(image, list1[1], list1[2], (0,255,0), 6)
    # image=cv2.line(image, list1[2], list1[3], (0,255,0), 6)
    # image=cv2.line(image, list1[3], list1[4], (0,255,0), 6)
    # image=cv2.line(image, list1[4], list1[5], (0,255,0), 6)
    # image=cv2.line(image, list1[5], list1[6], (0,255,0), 6)
    # image=cv2.line(image, list1[6], list1[7], (0,255,0), 6)
    # image=cv2.line(image, list1[7], list1[8], (0,255,0), 6)
    # image=cv2.line(image, list1[8], list1[9], (0,255,0), 6)
    # image=cv2.line(image, list1[9], list1[10], (0,255,0), 6)
    # image=cv2.line(image, list1[10], list1[11], (0,255,0), 6)
    # image=cv2.line(image, list1[11], list1[12], (0,255,0), 6)
    # image=cv2.line(image, list1[12], list1[13], (0,255,0), 6)
    # image=cv2.line(image, list1[13], list1[14], (0,255,0), 6)
    # image=cv2.line(image, list1[14], list1[15], (0,255,0), 6)
    # image=cv2.line(image, list1[15], list1[16], (0,255,0), 6)
    # image=cv2.line(image, list1[16], list1[17], (0,255,0), 6)
    # image=cv2.line(image, list1[17], list1[18], (0,255,0), 6)
    # image=cv2.line(image, list1[18], list1[0], (0,255,0), 6)

    



    # cv2.imshow(img_names+'g_d.jpg', image)
    # if cv2.waitKey() & 0xff == 27: quit()
    


