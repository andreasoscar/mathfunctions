import numpy as np
A = np.matrix([[3,1,2],[6,1,3],[6,0,1]])
C = np.matrix([1,1,1]).transpose()
I = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
x = np.matrix([0,1,1]).transpose()
G = I - A
for i in range(50):
    print(i)
    x = np.dot(G,x) + C
print(x)
v,ve = np.linalg.eig(G)
print(max(v))
