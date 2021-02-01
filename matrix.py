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
    x = []
    for i in range(1,n+1):
        x.append([1])
    #print(x)
    A = []
    for i in range(1,n+1):
        xi = []
        for j in range(1,n+1):
            xi.append(5/(i+2*j-1))
        A.append(xi)
    #print(n)
    #H = np.linalg.solve(A,np.dot(A,x))
    #print("$" + "\\" + "begin{bmatrix}")
    #for z in range(len(H)):
    #    print(str(H[z][0]) + " & " + "\\" + "\\ ",end='')
    #print("\end{bmatrix}$")
    #print("\\" + "\\")
    v.append(n)
    t.append(np.linalg.cond(A,np.inf))
    print(np.linalg.cond(A,np.inf))
height = t
bars = v
y_pos = np.arange(len(bars))

plt.plot(y_pos, height, color = 'blue')
plt.yscale('symlog')
plt.xlabel('Matrix Dimensions')
plt.ylabel('Condition number')
plt.xticks(y_pos, bars)
plt.show()
