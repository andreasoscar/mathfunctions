import scipy.linalg
import numpy as np
import matplotlib.pyplot as plt
from numpy import array as arr
import cmath
import math

def dft(x):
    N = len(x)
    S = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp = [((0-1j)*(2*np.pi*i*j)) / N]
            S[i] += x[j] * (1/math.sqrt(N))*np.exp(tmp)
    return S

def dft_inv(x):
    S = np.conjugate(arr(dft(x)).T)
    return S[0].transpose()
x1 = np.matrix([-1,0,0,0]).transpose()
x = dft_inv(x1)
for i in x:
    print(i)

c,d,n = -1,3,8
x_j = []
t_j = []
for i in np.linspace(c,d,n):
    x_j.append(math.exp(i))
    t_j.append(i)
y_j = dft(x_j)
def interpolate(t,m):
    P_t = y_j[0].real / math.sqrt(n)
    P_temp = 0
    v = 1
    for k in range(1,m):
        v += 2
        P_temp += (y_j[k].real*math.cos((2*math.pi*k*(t-c))/(d-c))-(y_j[k].imag*math.sin((2*math.pi*k*(t-c))/(d-c))))
    if m != 4:
        v += 1
        P_temp += (y_j[m].real*math.cos((2*math.pi*(m)*(t-c))/(d-c)))
    if m==4:
        v += 1
        P_t += (P_temp*(2/math.sqrt(n)) + (y_j[m].real/math.sqrt(n))*math.cos((n*math.pi*(t-c)/(d-c))))
    else:
        P_t += (P_temp*(2/math.sqrt(n)))
    #print(v)
    return P_t
y1 = []
y2 = []
y3 = []
f1 = []
f2 = []
f3 = []
for i in np.linspace(c,d-((d-c)/n),1000):
    y1.append(interpolate(i,4))
    f1.append(abs(math.exp(i) - interpolate(i,4)))
    y2.append(interpolate(i,2))
    f2.append(abs(math.exp(i) - interpolate(i,2)))
    y3.append(interpolate(i,3))
    f3.append(abs(math.exp(i) - interpolate(i,3)))
plt.plot(np.linspace(c,d,1000),f1, color='g')
#plt.plot(np.linspace(c,d,1000),y1)
plt.plot(np.linspace(c,d,1000),f2, color='r')
plt.plot(np.linspace(c,d,1000),f3, color='b')
#plt.scatter(t_j,x_j)
plt.show()
