import math

#========FB3=============
p=10
l=7.276
b=12.506
s=12.151

x0=b-s
c1=math.ceil(p*l)
c2=math.ceil(p*b)
c3=math.ceil(p*s)
c4=math.ceil(p*x0)
list1=[(0,0),(c4,c1),(c2,c1),(c2,0)]
print(list1)

#============FB4============

p=10
l=7.771
b=12.312
s=12.151

x0=b-s
c1=math.ceil(p*l)
c2=math.ceil(p*b)
c3=math.ceil(p*s)
c4=math.ceil(p*x0)
list1=[(c4,0),(0,c1),(c2,c1),(c2,0)]
print(list1)

#===========FB5=============

p=10
l=15.048
b=4.945
s=4.637
xp=7.773

c1=math.ceil(p*l)
c2=math.ceil(p*b)
c3=math.ceil(p*s)
c4=math.ceil(p*xp)
c5=math.ceil(p*(b-0.4))

list1=[(0,0),(0,c1),(c2,c1),(c5,c1-c4),(c3,0)]
print(list1)

#=============NR=============
p=10
l=1.5
b=13.9

c1=math.ceil(p*l)
c2=math.ceil(p*b)

list1=[(0,0),(0,c1),(c2,c1),(c2,0)]
print(list1)

