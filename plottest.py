import math
import scipy.linalg as la
import numpy as np
import matplotlib.pyplot as plt

A = [[1,4],[-4,1]] #Change A for different graphs
eigvals,eigvecs = la.eig(A)

new = []
old = []

norm1 = [0,0]
norm1dup = []
norm2 = [0,0]
norm2dup = []
norminf = [0,0]
norminfdup = []

x, y = -1, 0
for k in range(20000):
    x += 0.0001
    y = math.sqrt(1-x**2)
    old.append([x,y])
    old.append([x,-y])
    a, a_inv = np.matmul(A, [round(x,2),round(y,2)]), np.matmul(A, [round(x,2),round(-y,2)])
    new.append(a)
    new.append(a_inv)

    if abs(a[0]) + abs(a[1]) > abs(norm1[0]) + abs(norm1[1]):
        norm1 = a
        norm1dup = [a]
        norm1dup.append([-a[0], -a[1]])
        norm1dup.append([a[0], -a[1]])
        norm1dup.append([-a[0], a[1]])
    if abs(a[0]) + abs(a[1]) == abs(norm1[0]) + abs(norm1[1]):
        norm1dup.append(a)
        norm1dup.append([-a[0], -a[1]])
        norm1dup.append([a[0], -a[1]])
        norm1dup.append([-a[0], a[1]])

    if math.sqrt(a[0]**2 + a[1]**2) > math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2 = a
        norm2dup = [a]
        norm2dup.append([-a[0], -a[1]])
        norm2dup.append([-a[0], -a[1]])
        norm2dup.append([a[0], -a[1]])
        norm2dup.append([-a[0], a[1]])
    if math.sqrt(a[0]**2 + a[1]**2) == math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2dup.append(a)
        norm2dup.append([-a[0], -a[1]])
        norm2dup.append([a[0], -a[1]])
        norm2dup.append([-a[0], a[1]])

    if max(abs(a[0]), abs(a[1])) > max(abs(norminf[0]), abs(norminf[1])):
        norminf = a
        norminfdup = [a]
        norminfdup.append([-a[0], -a[1]])
    if max(abs(a[0]), abs(a[1])) == max(abs(norminf[0]), abs(norminf[1])):
        norminfdup.append(a)
        norminfdup.append([-a[0], -a[1]])

x,y = np.array(new).T
plt.scatter(x,y)
x,y = np.array(old).T
plt.scatter(x,y)
# max = abs(norm1dup[0][1]) + abs(norm1dup[0][1])
# count = 0
# for i in range(1,len(norm1dup)):
#     if max == abs(norm1dup[i][1]) + abs(norm1dup[i][1]):
#         count += 1
# print(count+1,len(norm1dup))
# x,y = np.array(norm1dup).T
# plt.scatter(x,y)
# x,y = np.array(norm2dup).T
# plt.scatter(x,y)
x,y = np.array(norminfdup).T
plt.scatter(x,y)
plt.show()
