import math
import scipy.linalg as la
import numpy as np
import matplotlib.pyplot as plt

A = [[1,4],[-4,1]]
eigvals,eigvecs = la.eig(A)

new = []
old = []

norm1 = [0,0]
norm1dup = []
norm2 = [0,0]
norm2dup = []
norminf = [0,0]
norminfdup = []

x, y = -1.001, 0
for k in range(2000):
    x += 0.001
    y = 1
    old.append([x,y])
    old.append([x,-y])
    a, a_inv = np.matmul(A, [x, y]), np.matmul(A, [x, -y])
    new.append(a)
    new.append(a_inv)
    if abs(a[0]) + abs(a[1]) > abs(norm1[0]) + abs(norm1[1]):
        norm1 = a
        norm1dup = [a]
        norm1dup.append(a)
        norm1dup.append([-a[0], -a[1]])
    if abs(a[0]) + abs(a[1]) == abs(norm1[0]) + abs(norm1[1]):
        norm1dup.append(a)
        norm1dup.append([-a[0], -a[1]])
    if math.sqrt(a[0]**2 + a[1]**2) > math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2 = a
        norm2dup = [a]
        norm2dup.append(a_inv)
    if math.sqrt(a[0]**2 + a[1]**2) == math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2dup.append(a)
        norm2dup.append(-a_inv)

    if max(abs(a[0]), abs(a[1])) > max(abs(norminf[0]), abs(norminf[1])):
        norminf = a
        norminfdup = [a]

    if max(abs(a[0]), abs(a[1])) == max(abs(norminf[0]), abs(norminf[1])):
        norminfdup.append(a)
        norminfdup.append(a_inv)

x, y = 0, -1.001
for k in range(2000):
    y += 0.001
    x = 1
    old.append([x,y])
    old.append([-x,y])
    a, a_inv = np.matmul(A, [x, y]), np.matmul(A, [-x, y])
    new.append(a)
    new.append(a_inv)

    if abs(a[0]) + abs(a[1]) > abs(norm1[0]) + abs(norm1[1]):
        norm1 = a
        norm1dup = []
    if abs(a[0]) + abs(a[1]) == abs(norm1[0]) + abs(norm1[1]):
        norm1dup.append(a)
        norm1dup.append([a[1], -a[0]])
        norm1dup.append([-a[1], a[0]])

    if math.sqrt(a[0]**2 + a[1]**2) > math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2 = a
        norm2dup = [a]
        norm2dup.append(a_inv)
    if math.sqrt(a[0]**2 + a[1]**2) == math.sqrt(norm2[0]**2 + norm2[1]**2):
        norm2dup.append(a)
        norm2dup.append(a_inv)
    if max(abs(a[0]), abs(a[1])) > max(abs(norminf[0]), abs(norminf[1])):
        norminf = a
        norminfdup = [a]
        norminfdup.append(a_inv)
    if max(abs(a[0]), abs(a[1])) == max(abs(norminf[0]), abs(norminf[1])):
        norminfdup.append(a)
        norminfdup.append(a_inv)
        norminfdup.append(-a_inv)

x,y = np.array(new).T
plt.scatter(x,y)
x,y = np.array(old).T
plt.scatter(x,y)
#plt.scatter(norm1[0],norm1[1],color = 'g')
#plt.scatter(norm2[0],norm2[1],color = 'r')
plt.scatter(norminf[0],norminf[1],color='r')
#for i in norm1dup:
#    plt.scatter(i[0],i[1],color = 'g')
# for i in norm2dup:
#     plt.scatter(i[0],i[1],color = 'r')
for i in norminfdup:
    plt.scatter(i[0],i[1],color = 'r')

plt.show()
