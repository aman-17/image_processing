def polygonArea(X, Y, n):
	area = 0.0
	j = n - 1
	for i in range(0,n):
		area += (X[j] + X[i]) * (Y[j] - Y[i])
		j = i 
	return int(abs(area / 2.0))

X = [0, 2, 4]
Y = [1, 3, 7]
n = len(X)
xx0 = polygonArea(X, Y, n)

def polygonArea1(X1, Y1, n1):
	area = 0.0
	j = n1 - 1
	for i in range(0,n):
		area += (X1[j] + X1[i]) * (Y1[j] - Y1[i])
		j = i 
	return int(abs(area / 2.0))

X1 = [0, 8, 7]
Y1 = [1, 3, 9]
n1 = len(X1)
x0 = polygonArea1(X1, Y1, n1)

from shapely.geometry import Polygon

p = Polygon([(1,1),(2,2),(4,2),(3,1)])
q = Polygon([(1.5,2),(3,5),(5,4),(7.5,1)])
#print(p.intersects(q))  # True
y = p.intersection(q).area
print(p.intersection(q).area)  # 1.0
x = p.intersection(q)
#print(x)

iou = y/(x0+xx0-y)
print(iou)
