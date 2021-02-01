import math
n = 5
#sum = 0
#for i in range(1,n+1):
#    s = 0
#    for j in range(1,n+1):
#        s += abs(5/(i+2*j-1))
#    if s > sum:
#        sum = s
x = []
for i in range(1,n+1):
    x.append([1])
print(x)
A = []
for i in range(1,n+1):
    xi = []
    for j in range(1,n+1):
        xi.append(5/(i+2*j-1))
    A.append(xi)
solve(A,x)




