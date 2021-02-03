import numpy as np
A = np.matrix([[1,2],[2,1]])
x_n = np.matrix([-1,0]).transpose()
r2 = 3
n = 0
while True:
    n += 1
    p = A*x_n
    n0 = max(abs(p))[0,0]
    if abs(n0-r2) < 10**(-4):
        print(n0)
        break
    x_n = p/n0
print(n)
