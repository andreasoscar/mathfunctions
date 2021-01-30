import numpy as np
G = np.matrix([[-2,-1,-2],[-6,0,-3],[-6,0,0]])
C = np.matrix([1,1,1]).transpose()
x_n = np.matrix([0,1,1]).transpose()
i = 1
while i < 50:
    x_n = np.dot(G,x_n) + C
    i += 1
print(x_n)
