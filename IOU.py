def polygonArea(X, Y, n):
	area = 0.0
	j = n - 1
	for i in range(0,n):
		area += (X[j] + X[i]) * (Y[j] - Y[i])
		j = i 
	return int(abs(area / 2.0))

X = [1268,1154,1154,1175,1176,1173,1170,1164,1136,1293,1296,1268]
Y = [655,655,811,845,875,900,937,948,956,957,689,655]
n = len(X)
xx0 = polygonArea(X, Y, n)

def polygonArea1(X1, Y1, n1):
	area = 0.0
	j = n1 - 1
	for i in range(0,n):
		area += (X1[j] + X1[i]) * (Y1[j] - Y1[i])
		j = i 
	return int(abs(area / 2.0))

X1 = [1277,1161,1178,1193,1203,1203,1198,1181,1129,1293,1307,1277]
Y1 = [633,669,714,755,811,848,893,932,960,959,669,633]
n1 = len(X1)
x0 = polygonArea1(X1, Y1, n1)

from shapely.geometry import Polygon

#p = Polygon([(1268,655),(1154,655),(1154,811),(1175,845),(1176,875),(1173,900),(1170,937),(1164,948),(1136,956),(1293,957),(1296,689),(1268,655)])
#q = Polygon([(1277,633),(1161,669),(1178,714),(1193,755),(1277,811),(1203,848),(1203,893),(1198,932),(1277,960),(1181,959),(1129,669),(1293,633)])

p = Polygon([(1268,655),(1154,655),(1154,811),(1175,845),(1176,875),(1173,900)])
q = Polygon([(1277,633),(1161,669),(1178,714),(1193,755),(1277,811)])
#print(p.intersects(q))  # True
y = p.intersection(q).area
print(p.intersection(q).area)  # 1.0
x = p.intersection(q)
#print(x)

iou = y/(x0+xx0-y)
print(iou)

'''
import numpy as np
import cv2

image = cv2.imread('F1.jpeg')

gt=[39, 63, 203, 112]
pred=[54, 66, 198, 114]

def bb_intersection_over_union(boxA, boxB):
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	iou = interArea / float(boxAArea + boxBArea - interArea)
	return iou

cv2.rectangle(image, tuple(gt[:2]), tuple(gt[2:]), (0, 255, 0), 2)
cv2.rectangle(image, tuple(pred[:2]), tuple(pred[2:]), (0, 0, 255), 2)

iou = bb_intersection_over_union(gt, pred)
cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
print(iou)

cv2.imshow("Image", image)
cv2.waitKey(0)


from shapely.geometry import box, Polygon

# Define Each polygon 
pol1_xy = [[130, 27], [129, 27], [129, 27], [130, 26]]
pol2_xy = [[130, 27], [127, 27], [129, 27], [130, 26]]
polygon1_shape = Polygon(pol1_xy)
polygon2_shape = Polygon(pol2_xy)

# Calculate Intersection and union, and tne IOU
polygon_intersection = polygon1_shape.intersection(polygon2_shape).area
polygon_union = polygon1_shape.union(polygon2_shape).area
IOU = polygon_intersection / polygon_union

print(IOU)
'''



