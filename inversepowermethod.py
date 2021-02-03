import numpy as np
A = np.matrix([[1,2],[2,1]])
n = 0
def power(A1,s):
    x_t = np.matrix([0,1]).transpose()
    r1 = -1
    n = 0
    while True:
        n += 1
        p = A1*x_t
        n0 = max(abs(p))[0,0]
        if abs(r1 - (1/n0 + s)) < 10**(-4):
            return (1/n0 + s), n
            break
        x_t = p/n0
s = -2.33
k = s*np.eye(2)
inv = np.linalg.inv(A-k)
print(power(inv,s))
