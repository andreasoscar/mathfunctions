import numpy as np
import math
import matplotlib.pyplot as plt
k2 = [_ for _ in range(1,11)]
xk2 = []
for i in k2:
    x = math.pi*(2*i-1)/(2*10)
    xk2.append(math.cos(x))
def gety(x):
    return math.exp(-x**2)
P2 = []
for i in xk2:
    P2.append([i,gety(i)])
def lagrange2(i,x):
    täljare = 1
    nämnare = 1
    for j in range(0,10):
        if i != j:
            täljare = täljare * (x-P2[j][0])
            nämnare = nämnare * (P2[i][0]-P2[j][0])
    return täljare/nämnare
xv = []
yv = []
xv1 = []
yv1 = []
i = -1
while i <= 1:
    sum = 0
    for j in range(0,10):
        sum += P2[j][1] * lagrange2(j,i)
    yv1.append(abs(gety(i)-sum))
    xv1.append(i)
    i += 0.01
k1 = plt.scatter(xv1,yv1)
plt.show()
