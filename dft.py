import scipy.linalg
import numpy as np
import matplotlib.pyplot as plt
import math
def dftinv(x):
    #F: inverse fourier matrix
    F = scipy.linalg.dft(len(x))
    F = np.linalg.inv(F)
    y = (math.sqrt(len(x)))*np.dot(F,x)
    return y
def dft(x):
    #F: Fourier matrix
    F = scipy.linalg.dft(len(x))
    y = (1/math.sqrt(len(x)))*np.dot(F,x)
    return y
c,d,n = 0,7/8,8
P = []
t_x = []
for i in range(8):
    P.append(math.exp(i/8))
    t_x.append(i/8)
def interpolate(t,m):
    xvalues = np.matrix(P).transpose()
    y = dft(xvalues)
    print(y)
    P_t = y[0].item(0).real / math.sqrt(n)
    P_temp = 0
    for k in range(1,m):
        P_temp += (y[k].item(0).real*math.cos((2*math.pi*k*(t-c))/(d-c)) - y[k].item(0).imag*math.sin((2*math.pi*k*(t-c))/(d-c)))
    P_t += (P_temp*(2/math.sqrt(n)) + (y[n//2].item(0).real/math.sqrt(n))*math.cos((n*math.pi*(t-c)/(d-c))))
    return P_t
x = np.linspace(0,7/8,8)
y = []
for i in x:
    tj = c + i*(d-c)
    y.append(interpolate(tj,4))
# plt.plot(x,y)
# x = []
# y = []
# for i in range(0,8):
#     x.append([i/8])
#     y.append(np.exp(i/8))
# plt.scatter(x,y)
# x = np.linspace(0,7/8,1000)
# y = []
# for i in x:
#     tj = c + i*(d-c)
#     y.append(interpolate(tj,2))
# plt.plot(x,y)
# x = np.linspace(0,7/8,1000)
# y = []
# for i in x:
#     tj = c + i*(d-c)
#     y.append(interpolate(tj,3))
# plt.plot(x,y)
plt.show()
