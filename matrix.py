import math
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
t,v = [],[]
def inf(a):
    sum = -1
    for i in a:
        s = 0
        for j in i:
            s += abs(j)
        if s > sum:
            sum = s
    return sum
for h in range(6,16):
    n = h
    A = []
    x = np.matrix([1 for i in range(n)]).transpose()
    for i in range(1,n+1):
        xi = []
        for j in range(1,n+1):
            xi.append(5/(i+2*j-1))
        A.append(xi)
    b = np.dot(A,x)
    H = np.linalg.solve(A,b)
    print(n)
    for i in H:
        print(i)
    print()
