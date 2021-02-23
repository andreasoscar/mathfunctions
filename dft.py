import scipy.linalg
import numpy as np
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
P = []
for i in range(8):
    P.append([i/8,math.exp(i/8)])
print(P)
