import numpy as np
import math
K = np.matrix([[1,2],[2,1]])
xt = np.matrix([-1,0]).transpose()
def power(x0,A,r):
    x_n = x0
    n = 0
    while True:
        n += 1
        n0 = x_n/math.sqrt(x_n[0]**2 + x_n[1]**2)
        x_n = A.dot(x_n)
        g1 = n0.transpose().dot(A).dot(n0)
        if abs(g1-r) < 10**(-4):
            return g1, n
            break
print(power(xt,K,3))
