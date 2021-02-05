import numpy as np
import math
K = np.matrix([[1,2],[2,1]])
xt = np.matrix([-1,0]).transpose()
def inv_power(x0,A,r):
    x_n = x0
    n = 0
    while True:
        n += 1
        n0 = x_n/math.sqrt(x_n[0]**2+x_n[1]**2)
        x_n = np.linalg.solve(A,n0)
        ginv = n0.transpose().dot(x_n)
        if abs(ginv - r) < 10**(-4):
            return ginv, n
            break
print(inv_power(xt,K,-1))
