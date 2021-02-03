import numpy as np
import math
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
import random
data = []
old = []
A = [[1,2],[2,1]]
#w, v = np.linalg.eig(A)
#print(np.linalg.cond())
print(np.linalg.norm(A)*np.linalg.norm(np.linalg.inv(A)))
print(np.linalg.inv(A))


# x,y = -1,0
# for i in range(20000):
#     y = math.sqrt(1-x**2)
#     x += 0.0001
#     old.append([x,y])
#     old.append([x,-y])
#     data.append(np.matmul(A,[round(x,2),round(-y,2)]))
#     data.append(np.matmul(A,[round(x,2),round(y,2)]))
# x, y = np.array(data).T
# plt.scatter(x,y)
# x, y = np.array(old).T
# plt.scatter(x,y)
# #plt.show()
