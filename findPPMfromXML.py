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
import os, glob, requests
import random


width = 0.955
medium = 28.5
path_xml = '/Users/amanrangapur/Desktop/labels/'
path = '/Users/amanrangapur/Desktop/labels/*png'
images = []
areas_ann = []
areas_mrcnn = []
accuracy_arr = []
f = open('dh-34-panel.json')
data = json.load(f)
d=data["xs"]["f"]["h3"]



def getCoinBoundriesMRCNN(filename):
    url = 'http://13.59.24.196:8080/predict_bounding_box_from_upload_image?input_data=' + filename
    name_img= os.path.basename(filename)
    files= {'input_data': (name_img, open(filename,'rb'),'image/jpeg') }
    x = requests.post(url, files = files)
    bounding_boxes_data=x.json()
    final_data=None
    final_data=bounding_boxes_data['message'][0]
    # print(final_data)
    return final_data


def ppmfromxml():

    for img in glob.glob(path):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        boundaries = getCoinBoundriesMRCNN(img)
        images.append(image)
        xml_path = img_names+".xml"
        tree = ET.parse(path_xml+xml_path)
        root = tree.getroot()
        xmin = (root[5][4][0].text)
        xmax = (root[5][4][2].text)

        # pixelsPerMetric_ann=math.ceil((int(xmax)-int(xmin))/width)
        pixelsPerMetric_ann = random.randint(10,25)
        print("Annotations-PPM of ",img,": ",pixelsPerMetric_ann)
        pixelsPerMetric_mrcnn=math.ceil((boundaries[2]-boundaries[0])/medium)
        print("MRCNN-PPM of ",img,": ",pixelsPerMetric_mrcnn)


        ann_c0=math.ceil(pixelsPerMetric_ann*float(d['h']))
        ann_c1=math.ceil(pixelsPerMetric_ann*float(d['b']))
        ann_ccx1=math.ceil(pixelsPerMetric_ann*float(d['cx1']))
        ann_ccx2=math.ceil(pixelsPerMetric_ann*float(d['cx2']))
        ann_ccx3=math.ceil(pixelsPerMetric_ann*float(d['cx3']))
        ann_ccx4=math.ceil(pixelsPerMetric_ann*float(d['cx4']))
        ann_ccx5=math.ceil(pixelsPerMetric_ann*float(d['cx5']))
        ann_ccx6=math.ceil(pixelsPerMetric_ann*float(d['cx6']))
        ann_ccx7=math.ceil(pixelsPerMetric_ann*float(d['cx7']))
        ann_ccx8=math.ceil(pixelsPerMetric_ann*float(d['cx8']))
        ann_ccx9=math.ceil(pixelsPerMetric_ann*float(d['cx9']))
        ann_ccx10=math.ceil(pixelsPerMetric_ann*float(d['cx10']))
        ann_ccx11=math.ceil(pixelsPerMetric_ann*float(d['cx11']))
        ann_ccx12=math.ceil(pixelsPerMetric_ann*float(d['cx12']))
        ann_ccx13=math.ceil(pixelsPerMetric_ann*float(d['cx13']))
        ann_ccx14=math.ceil(pixelsPerMetric_ann*float(d['cx14']))
        ann_ccx15=math.ceil(pixelsPerMetric_ann*float(d['cx15']))
        ann_ccx16=math.ceil(pixelsPerMetric_ann*float(d['cx16']))

        ann_ccy1=math.ceil(pixelsPerMetric_ann*float(d['cy1']))
        ann_ccy2=math.ceil(pixelsPerMetric_ann*float(d['cy2']))
        ann_ccy3=math.ceil(pixelsPerMetric_ann*float(d['cy3']))
        ann_ccy4=math.ceil(pixelsPerMetric_ann*float(d['cy4']))
        ann_ccy5=math.ceil(pixelsPerMetric_ann*float(d['cy5']))
        ann_ccy6=math.ceil(pixelsPerMetric_ann*float(d['cy6']))
        ann_ccy7=math.ceil(pixelsPerMetric_ann*float(d['cy7']))
        ann_ccy8=math.ceil(pixelsPerMetric_ann*float(d['cy8']))
        ann_ccy9=math.ceil(pixelsPerMetric_ann*float(d['cy9']))
        ann_ccy10=math.ceil(pixelsPerMetric_ann*float(d['cy10']))
        ann_ccy11=math.ceil(pixelsPerMetric_ann*float(d['cy11']))
        ann_ccy12=math.ceil(pixelsPerMetric_ann*float(d['cy12']))
        ann_ccy13=math.ceil(pixelsPerMetric_ann*float(d['cy13']))
        ann_ccy14=math.ceil(pixelsPerMetric_ann*float(d['cy14']))
        ann_ccy15=math.ceil(pixelsPerMetric_ann*float(d['cy15']))
        ann_ccy16=math.ceil(pixelsPerMetric_ann*float(d['cy16']))

        ann_list1=[(0,0),(0,ann_c0),(ann_ccx16,ann_ccy16),(ann_ccx15,ann_ccy15),(ann_ccx14,ann_ccy14),(ann_ccx13,ann_ccy13),(ann_ccx12,ann_ccy12),
        (ann_ccx11,ann_ccy11),(ann_ccx10,ann_ccy10),(ann_ccx9,ann_ccy9),(ann_ccx8,ann_ccy8),(ann_ccx7,ann_ccy7),(ann_ccx6,ann_ccy6),(ann_ccx5,ann_ccy5),
        (ann_ccx4,ann_ccy4),(ann_ccx3,ann_ccy3),(ann_ccx2,ann_ccy2),(ann_ccx1,ann_ccy1),(ann_c1,0)]



        ann_vertices = [[0,0],[0,ann_c0],[ann_ccx16,ann_ccy16],[ann_ccx15,ann_ccy15],[ann_ccx14,ann_ccy14],[ann_ccx13,ann_ccy13],[ann_ccx12,ann_ccy12],
        [ann_ccx11,ann_ccy11],[ann_ccx10,ann_ccy10],[ann_ccx9,ann_ccy9],[ann_ccx8,ann_ccy8],[ann_ccx7,ann_ccy7],[ann_ccx6,ann_ccy6],[ann_ccx5,ann_ccy5],
        [ann_ccx4,ann_ccy4],[ann_ccx3,ann_ccy3],[ann_ccx2,ann_ccy2],[ann_ccx1,ann_ccy1],[ann_c1,0]]

        mrcnn_c0=math.ceil(pixelsPerMetric_mrcnn*float(d['h']))
        mrcnn_c1=math.ceil(pixelsPerMetric_mrcnn*float(d['b']))

        mrcnn_ccx1=math.ceil(pixelsPerMetric_mrcnn*float(d['cx1']))
        mrcnn_ccx2=math.ceil(pixelsPerMetric_mrcnn*float(d['cx2']))
        mrcnn_ccx3=math.ceil(pixelsPerMetric_mrcnn*float(d['cx3']))
        mrcnn_ccx4=math.ceil(pixelsPerMetric_mrcnn*float(d['cx4']))
        mrcnn_ccx5=math.ceil(pixelsPerMetric_mrcnn*float(d['cx5']))
        mrcnn_ccx6=math.ceil(pixelsPerMetric_mrcnn*float(d['cx6']))
        mrcnn_ccx7=math.ceil(pixelsPerMetric_mrcnn*float(d['cx7']))
        mrcnn_ccx8=math.ceil(pixelsPerMetric_mrcnn*float(d['cx8']))
        mrcnn_ccx9=math.ceil(pixelsPerMetric_mrcnn*float(d['cx9']))
        mrcnn_ccx10=math.ceil(pixelsPerMetric_mrcnn*float(d['cx10']))
        mrcnn_ccx11=math.ceil(pixelsPerMetric_mrcnn*float(d['cx11']))
        mrcnn_ccx12=math.ceil(pixelsPerMetric_mrcnn*float(d['cx12']))
        mrcnn_ccx13=math.ceil(pixelsPerMetric_mrcnn*float(d['cx13']))
        mrcnn_ccx14=math.ceil(pixelsPerMetric_mrcnn*float(d['cx14']))
        mrcnn_ccx15=math.ceil(pixelsPerMetric_mrcnn*float(d['cx15']))
        mrcnn_ccx16=math.ceil(pixelsPerMetric_mrcnn*float(d['cx16']))

        mrcnn_ccy1=math.ceil(pixelsPerMetric_mrcnn*float(d['cy1']))
        mrcnn_ccy2=math.ceil(pixelsPerMetric_mrcnn*float(d['cy2']))
        mrcnn_ccy3=math.ceil(pixelsPerMetric_mrcnn*float(d['cy3']))
        mrcnn_ccy4=math.ceil(pixelsPerMetric_mrcnn*float(d['cy4']))
        mrcnn_ccy5=math.ceil(pixelsPerMetric_mrcnn*float(d['cy5']))
        mrcnn_ccy6=math.ceil(pixelsPerMetric_mrcnn*float(d['cy6']))
        mrcnn_ccy7=math.ceil(pixelsPerMetric_mrcnn*float(d['cy7']))
        mrcnn_ccy8=math.ceil(pixelsPerMetric_mrcnn*float(d['cy8']))
        mrcnn_ccy9=math.ceil(pixelsPerMetric_mrcnn*float(d['cy9']))
        mrcnn_ccy10=math.ceil(pixelsPerMetric_mrcnn*float(d['cy10']))
        mrcnn_ccy11=math.ceil(pixelsPerMetric_mrcnn*float(d['cy11']))
        mrcnn_ccy12=math.ceil(pixelsPerMetric_mrcnn*float(d['cy12']))
        mrcnn_ccy13=math.ceil(pixelsPerMetric_mrcnn*float(d['cy13']))
        mrcnn_ccy14=math.ceil(pixelsPerMetric_mrcnn*float(d['cy14']))
        mrcnn_ccy15=math.ceil(pixelsPerMetric_mrcnn*float(d['cy15']))
        mrcnn_ccy16=math.ceil(pixelsPerMetric_mrcnn*float(d['cy16']))

        mrcnn_list1=[(0,0),(0,mrcnn_c0),(mrcnn_ccx16,mrcnn_ccy16),(mrcnn_ccx15,mrcnn_ccy15),(mrcnn_ccx14,mrcnn_ccy14),(mrcnn_ccx13,mrcnn_ccy13),(mrcnn_ccx12,mrcnn_ccy12),
        (mrcnn_ccx11,mrcnn_ccy11),(mrcnn_ccx10,mrcnn_ccy10),(mrcnn_ccx9,mrcnn_ccy9),(mrcnn_ccx8,mrcnn_ccy8),(mrcnn_ccx7,mrcnn_ccy7),(mrcnn_ccx6,mrcnn_ccy6),(mrcnn_ccx5,mrcnn_ccy5),
        (mrcnn_ccx4,mrcnn_ccy4),(mrcnn_ccx3,mrcnn_ccy3),(mrcnn_ccx2,mrcnn_ccy2),(mrcnn_ccx1,mrcnn_ccy1),(mrcnn_c1,0)]

        mrcnn_vertices = [[0,0],[0,mrcnn_c0],[mrcnn_ccx16,mrcnn_ccy16],[mrcnn_ccx15,mrcnn_ccy15],[mrcnn_ccx14,mrcnn_ccy14],[mrcnn_ccx13,mrcnn_ccy13],[mrcnn_ccx12,mrcnn_ccy12],
        [mrcnn_ccx11,mrcnn_ccy11],[mrcnn_ccx10,mrcnn_ccy10],[mrcnn_ccx9,mrcnn_ccy9],[mrcnn_ccx8,mrcnn_ccy8],[mrcnn_ccx7,mrcnn_ccy7],[mrcnn_ccx6,mrcnn_ccy6],[mrcnn_ccx5,mrcnn_ccy5],
        [mrcnn_ccx4,mrcnn_ccy4],[mrcnn_ccx3,mrcnn_ccy3],[mrcnn_ccx2,mrcnn_ccy2],[mrcnn_ccx1,mrcnn_ccy1],[mrcnn_c1,0]]

        ann_numberOfVertices = len(ann_vertices)
        ann_sum1 = 0
        ann_sum2 = 0
        for i in range(0,ann_numberOfVertices-1):
            ann_sum1 = ann_sum1 + ann_vertices[i][0] *  ann_vertices[i+1][1]
            ann_sum2 = ann_sum2 + ann_vertices[i][1] *  ann_vertices[i+1][0]
        
        ann_sum1 = ann_sum1 + ann_vertices[ann_numberOfVertices-1][0]*ann_vertices[0][1]   
        ann_sum2 = ann_sum2 + ann_vertices[0][0]*ann_vertices[ann_numberOfVertices-1][1]   
        
        ann_area = math.ceil(abs(ann_sum1 - ann_sum2) / 2)
        # print("Annotations Area ", "of ",img,": ",ann_area)
        areas_ann.append(ann_area)

        mrcnn_numberOfVertices = len(mrcnn_vertices)
        mrcnn_sum1 = 0
        mrcnn_sum2 = 0
        
        for i in range(0,mrcnn_numberOfVertices-1):
            mrcnn_sum1 = mrcnn_sum1 + mrcnn_vertices[i][0] *  mrcnn_vertices[i+1][1]
            mrcnn_sum2 = mrcnn_sum2 + mrcnn_vertices[i][1] *  mrcnn_vertices[i+1][0]
        mrcnn_sum1 = mrcnn_sum1 + mrcnn_vertices[mrcnn_numberOfVertices-1][0]*mrcnn_vertices[0][1]
        mrcnn_sum2 = mrcnn_sum2 + mrcnn_vertices[0][0]*mrcnn_vertices[mrcnn_numberOfVertices-1][1]
        mrcnn_area = math.ceil(abs(mrcnn_sum1 - mrcnn_sum2) / 2)
        # print("MRCNN Area ", "of ",img,": ",mrcnn_area)
        areas_mrcnn.append(areas_mrcnn)
        accuracy = (mrcnn_area/ann_area)
        # if accuracy>100:
        #     accuracy = 200-accuracy
        # else:
        #     accuracy=accuracy
        print("Threshold: ",accuracy)
        accuracy_arr.append(accuracy)

        if accuracy<6.8:
            img=cv2.line(image, ann_list1[0], ann_list1[1], (0,255,0), 6)
            img=cv2.line(image, ann_list1[1], ann_list1[2], (0,255,0), 6)
            img=cv2.line(image, ann_list1[2], ann_list1[3], (0,255,0), 6)
            img=cv2.line(image, ann_list1[3], ann_list1[4], (0,255,0), 6)
            img=cv2.line(image, ann_list1[4], ann_list1[5], (0,255,0), 6)
            img=cv2.line(image, ann_list1[5], ann_list1[6], (0,255,0), 6)
            img=cv2.line(image, ann_list1[6], ann_list1[7], (0,255,0), 6)
            img=cv2.line(image, ann_list1[7], ann_list1[8], (0,255,0), 6)
            img=cv2.line(image, ann_list1[8], ann_list1[9], (0,255,0), 6)
            img=cv2.line(image, ann_list1[9], ann_list1[10], (0,255,0), 6)
            img=cv2.line(image, ann_list1[10], ann_list1[11], (0,255,0), 6)
            img=cv2.line(image, ann_list1[11], ann_list1[12], (0,255,0), 6)
            img=cv2.line(image, ann_list1[12], ann_list1[13], (0,255,0), 6)
            img=cv2.line(image, ann_list1[13], ann_list1[14], (0,255,0), 6)
            img=cv2.line(image, ann_list1[14], ann_list1[15], (0,255,0), 6)
            img=cv2.line(image, ann_list1[15], ann_list1[16], (0,255,0), 6)
            img=cv2.line(image, ann_list1[16], ann_list1[17], (0,255,0), 6)
            img=cv2.line(image, ann_list1[17], ann_list1[18], (0,255,0), 6)
            img=cv2.line(image, ann_list1[18], ann_list1[0], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[19], ann_list1[20], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[20], ann_list1[21], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[21], ann_list1[22], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[22], ann_list1[23], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[23], ann_list1[24], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[24], ann_list1[25], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[25], ann_list1[26], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[26], ann_list1[27], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[27], ann_list1[28], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[28], ann_list1[29], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[29], ann_list1[30], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[30], ann_list1[31], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[31], ann_list1[32], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[32], ann_list1[33], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[33], ann_list1[34], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[34], ann_list1[35], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[35], ann_list1[36], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[36], ann_list1[37], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[37], ann_list1[38], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[38], ann_list1[39], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[39], ann_list1[40], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[40], ann_list1[41], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[41], ann_list1[42], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[42], ann_list1[43], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[43], ann_list1[44], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[44], ann_list1[45], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[45], ann_list1[46], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[46], ann_list1[47], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[47], ann_list1[48], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[48], ann_list1[49], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[49], ann_list1[50], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[50], ann_list1[51], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[51], ann_list1[52], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[52], ann_list1[53], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[53], ann_list1[54], (0,255,0), 6)
            # img=cv2.line(image, ann_list1[54], ann_list1[0], (0,255,0), 6)

            cv2.imshow('ann.jpg', img)
            k=cv2.waitKey(0) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()




    

    # average_acc = sum(accuracy_arr)/len(accuracy_arr)
    # print("Average Threshold: ", average_acc)


    # print("Max Area: ",max(areas))
    # print("Min Area: ",min(areas))
    # total = accuracy_arr.sum()
    # avg = accuracy_arr/189
    return None



# getCoinBoundriesMRCNN('testimg2.jpeg')

 
def getBoundaries():
    for img in glob.glob(path):
        img_names = os.path.basename(img).split(".")[0]
        # image= cv2.imread(img)
        image=path_xml+img_names+'.png'
        images.append(image)
        boundaries = getCoinBoundriesMRCNN(image)
        pixelsPerMetric=math.ceil((boundaries[2]-boundaries[0])/medium)
        print(pixelsPerMetric)
        f = open('dh-34-panel.json')
        data = json.load(f)
        d=data["xs"]["f"]["h3"]


        mrcnn_c0=math.ceil(pixelsPerMetric*float(d['h']))
        mrcnn_c1=math.ceil(pixelsPerMetric*float(d['b']))

        mrcnn_ccx1=math.ceil(pixelsPerMetric*float(d['cx1']))
        mrcnn_ccx2=math.ceil(pixelsPerMetric*float(d['cx2']))
        mrcnn_ccx3=math.ceil(pixelsPerMetric*float(d['cx3']))
        mrcnn_ccx4=math.ceil(pixelsPerMetric*float(d['cx4']))
        mrcnn_ccx5=math.ceil(pixelsPerMetric*float(d['cx5']))
        mrcnn_ccx6=math.ceil(pixelsPerMetric*float(d['cx6']))
        mrcnn_ccx7=math.ceil(pixelsPerMetric*float(d['cx7']))
        mrcnn_ccx8=math.ceil(pixelsPerMetric*float(d['cx8']))
        mrcnn_ccx9=math.ceil(pixelsPerMetric*float(d['cx9']))
        mrcnn_ccx10=math.ceil(pixelsPerMetric*float(d['cx10']))
        mrcnn_ccx11=math.ceil(pixelsPerMetric*float(d['cx11']))
        mrcnn_ccx12=math.ceil(pixelsPerMetric*float(d['cx12']))
        mrcnn_ccx13=math.ceil(pixelsPerMetric*float(d['cx13']))
        mrcnn_ccx14=math.ceil(pixelsPerMetric*float(d['cx14']))
        mrcnn_ccx15=math.ceil(pixelsPerMetric*float(d['cx15']))
        mrcnn_ccx16=math.ceil(pixelsPerMetric*float(d['cx16']))

        mrcnn_ccy1=math.ceil(pixelsPerMetric*float(d['cy1']))
        mrcnn_ccy2=math.ceil(pixelsPerMetric*float(d['cy2']))
        mrcnn_ccy3=math.ceil(pixelsPerMetric*float(d['cy3']))
        mrcnn_ccy4=math.ceil(pixelsPerMetric*float(d['cy4']))
        mrcnn_ccy5=math.ceil(pixelsPerMetric*float(d['cy5']))
        mrcnn_ccy6=math.ceil(pixelsPerMetric*float(d['cy6']))
        mrcnn_ccy7=math.ceil(pixelsPerMetric*float(d['cy7']))
        mrcnn_ccy8=math.ceil(pixelsPerMetric*float(d['cy8']))
        mrcnn_ccy9=math.ceil(pixelsPerMetric*float(d['cy9']))
        mrcnn_ccy10=math.ceil(pixelsPerMetric*float(d['cy10']))
        mrcnn_ccy11=math.ceil(pixelsPerMetric*float(d['cy11']))
        mrcnn_ccy12=math.ceil(pixelsPerMetric*float(d['cy12']))
        mrcnn_ccy13=math.ceil(pixelsPerMetric*float(d['cy13']))
        mrcnn_ccy14=math.ceil(pixelsPerMetric*float(d['cy14']))
        mrcnn_ccy15=math.ceil(pixelsPerMetric*float(d['cy15']))
        mrcnn_ccy16=math.ceil(pixelsPerMetric*float(d['cy16']))

        mrcnn_list1=[(0,0),(0,mrcnn_c0),(mrcnn_ccx16,mrcnn_ccy16),(mrcnn_ccx15,mrcnn_ccy15),(mrcnn_ccx14,mrcnn_ccy14),(mrcnn_ccx13,mrcnn_ccy13),(mrcnn_ccx12,mrcnn_ccy12),
        (mrcnn_ccx11,mrcnn_ccy11),(mrcnn_ccx10,mrcnn_ccy10),(mrcnn_ccx9,mrcnn_ccy9),(mrcnn_ccx8,mrcnn_ccy8),(mrcnn_ccx7,mrcnn_ccy7),(mrcnn_ccx6,mrcnn_ccy6),(mrcnn_ccx5,mrcnn_ccy5),
        (mrcnn_ccx4,mrcnn_ccy4),(mrcnn_ccx3,mrcnn_ccy3),(mrcnn_ccx2,mrcnn_ccy2),(mrcnn_ccx1,mrcnn_ccy1),(mrcnn_c1,0)]

        mrcnn_vertices = [[0,0],[0,mrcnn_c0],[mrcnn_ccx16,mrcnn_ccy16],[mrcnn_ccx15,mrcnn_ccy15],[mrcnn_ccx14,mrcnn_ccy14],[mrcnn_ccx13,mrcnn_ccy13],[mrcnn_ccx12,mrcnn_ccy12],
        [mrcnn_ccx11,mrcnn_ccy11],[mrcnn_ccx10,mrcnn_ccy10],[mrcnn_ccx9,mrcnn_ccy9],[mrcnn_ccx8,mrcnn_ccy8],[mrcnn_ccx7,mrcnn_ccy7],[mrcnn_ccx6,mrcnn_ccy6],[mrcnn_ccx5,mrcnn_ccy5],
        [mrcnn_ccx4,mrcnn_ccy4],[mrcnn_ccx3,mrcnn_ccy3],[mrcnn_ccx2,mrcnn_ccy2],[mrcnn_ccx1,mrcnn_ccy1],[mrcnn_c1,0]]

        mrcnn_numberOfVertices = len(mrcnn_vertices)
        mrcnn_sum1 = 0
        mrcnn_sum2 = 0
        
        for i in range(0,mrcnn_numberOfVertices-1):
            mrcnn_sum1 = mrcnn_sum1 + mrcnn_vertices[i][0] *  mrcnn_vertices[i+1][1]
            mrcnn_sum2 = mrcnn_sum2 + mrcnn_vertices[i][1] *  mrcnn_vertices[i+1][0]
        mrcnn_sum1 = mrcnn_sum1 + mrcnn_vertices[mrcnn_numberOfVertices-1][0]*mrcnn_vertices[0][1]
        mrcnn_sum2 = mrcnn_sum2 + mrcnn_vertices[0][0]*mrcnn_vertices[mrcnn_numberOfVertices-1][1]
        mrcnn_area = math.ceil(abs(mrcnn_sum1 - mrcnn_sum2) / 2)
        areas_mrcnn.append(mrcnn_area)

    print("Max Area: ",max(areas_mrcnn))
    print("Min Area: ",min(areas_mrcnn))
    return None
    
ppmfromxml()

