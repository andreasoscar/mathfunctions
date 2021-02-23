import math
import matplotlib.pyplot as plt
import numpy as np
k2 = [_ for _ in range(1,21)]
xk2 = []
for i in k2:
    x = math.pi*(2*i-1)/(2*20)
    xk2.append(math.cos(x))
def gety(x):
    return math.exp(-x**2)
x1 = np.linspace(-1,1,21)
P1 = []
P2 = []
for i in x1:
    P1.append([i,gety(i)])
for i in xk2:
    P2.append([i,gety(i)])
def lagrange(i,x):
    täljare = 1
    nämnare = 1
    for j in range(0,21):
        if i != j:
            täljare = täljare * (x-P1[j][0])
            nämnare = nämnare * (P1[i][0]-P1[j][0])
    return täljare/nämnare
def lagrange2(i,x):
    täljare = 1
    nämnare = 1
    for j in range(0,20):
        if i != j:
            täljare = täljare * (x-P2[j][0])
            nämnare = nämnare * (P2[i][0]-P2[j][0])
    return täljare/nämnare
yv = []
yv1 = []
xv = []
xv1 = []
i = -1
#lagrange
while i <= 1:
    sum = 0
    for j in range(0,21):
        sum += P1[j][1] * lagrange(j,i)
    yv.append(abs(gety(i)-sum))
    #yv.append(sum)
    xv.append(i)
    i += 0.01
i = -1
while i <= 1:
    sum = 0
    for j in range(0,20):
        sum += P2[j][1] * lagrange2(j,i)
    yv1.append(abs(gety(i)-sum))
    #yv1.append(sum)
    xv1.append(i)
    i += 0.01
k1 = plt.scatter(xv,yv)
k2 = plt.scatter(xv1,yv1)
plt.legend((k1,k2),('lagrange','chebyshev'),loc='upper right')
plt.show()
