import numpy as np
import math
import matplotlib.pyplot as plt
from gramschmidt import gramschmidt,ortho
P = []

for i in range(0,11):
    x = 2 + 0.2*i
    y = 1 + x + x**2 + x**3 + x**4 + x**5 + x**6 + x**7 + x**8
    P.append([x,y])
A = []
for point in P:
    A.append([1,point[0]])
b = []
for point in P:
    b.append([point[1]])
Q,R = gramschmidt(ortho(np.matrix(A)),np.matrix(A))
result = (np.linalg.solve(R,Q.transpose()*b))
m,k = result.item(0),result.item(1)
x_,y_ = np.array(P).T
plt.scatter(x_,y_)
x = np.linspace(2,4,11)
y = k*x + m
print(k,m)
plt.plot(x,y,'r',label=str('y=' + str(k) + "x" + str(m) + ''))
plt.legend(loc='upper left')
#plt.show()
def residual():
    sum = 0
    for i in P:
        sum += (i[1] - (m + k*i[0]))**2
    return math.sqrt(sum)
print(residual())
