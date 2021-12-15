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

x1=0.42
x2=0.26


p1= 0.17

img=cv2.imread('artestimage2.jpg')

h, w, _ = img.shape
print('width: ', w)
print('height:', h)

width_of_box1 = x1*w
width_of_box2 = x2*w

print(width_of_box1)
print(width_of_box2)

ppm = math.ceil(abs(width_of_box2-width_of_box1)) #/p1
print("PPM: ", ppm)


