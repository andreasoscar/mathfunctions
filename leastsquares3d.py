import numpy as np
import math
from gramschmidt import gramschmidt,ortho
A = [[1,0,1],[1,0,1],[1,1,0],[1,1,0],[1,1,2]]
b = np.matrix([3,2,3,4,6]).transpose()
Q, R = gramschmidt(ortho(np.matrix(A)),np.matrix(A))
result = np.linalg.solve(R,Q.transpose()*b)
c0,c1,c2 = result.item(0),result.item(1),result.item(2)
print(c0,c1,c2)
def residual():
    sum = 0
    b = [3,2,3,4,6]
    k = 0
    for i in A:
        print(i)
        sum += (b[k] - (c0 + c1*i[1] + c2*i[2]))**2
        k += 1
    return math.sqrt(sum)
print(residual())
