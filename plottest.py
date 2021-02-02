import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
import random
data = []
while len(data) < 300:
    x = round(random.uniform(-1,1),2)
    y = round(random.uniform(-1,1),2)
    if abs(x)+abs(y) == 1:
        new_x = x + 2*y
        new_y = 2*x + y
        data.append([new_x,new_y])
x, y = np.array(data).T
plt.scatter(x,y)
plt.show()
