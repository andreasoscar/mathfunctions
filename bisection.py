import math
import re
print("a b tol dec")
a,b,tol,dec = [eval(x) for x in input().split()]
def f(x):
    return math.cos(x)**2 + 6 - x
if f(a)*f(b) >= 0:
    print("unable to evaluate")
else:
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(c) == 0:
            break
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
print(("{:." + str(dec) + "f}").format((a+b)/2))
