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
    true_vec = [1 for i in range(n)]
    A = []
    for i in range(1,n+1):
        xi = []
        for j in range(1,n+1):
            xi.append(5/(i+2*j-1))
        A.append(xi)
    H = np.linalg.solve(A,list(map(sum,A)))
    v.append(n)
    t.append(math.sqrt(sum(true_vec-H)**2))
    #print(n)
    # H = np.linalg.solve(A,np.dot(A,x))
    # print("$" + "\\" + "begin{bmatrix}")
    # for z in range(len(H)):
    #    print(str(H[z][0]) + " & " + "\\" + "\\ ",end='')
    # print("\end{bmatrix}$")
    # print("\\" + "\\")
plt.plot(v,t)
plt.xticks(np.arange(min(v),max(v)+1,1))
plt.show()
