import math
import matplotlib.pyplot as plt

def f_x(x):
    return math.cos(x)

def Simpson(a, b, n):
    h = (b-a)/(n)
    x_j = []
    for j in range(n):
        x_j.append(a + j*h)
    I = 0
    for j in range(1,n):
        I += 2*f_x(x_j[j]) + 4*f_x(x_j[j] + (h/2))
    I += f_x(a) + 4*f_x(a + (h/2)) + f_x(b)
    I *= h/6
    return I

error = []
n_start = 64
n = []
for i in range(n_start,4095,2*n_start):
    error.append(abs(Simpson(0, 10, i) - math.sin(10)))
    n.append(i)
for i in range(len(error)-1):
    print(error[i+1]/(error[i]))

plt.plot(n,error)
plt.yscale("log")
plt.xscale("log")
plt.show()
