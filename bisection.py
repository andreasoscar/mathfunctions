
from math import *
print("a b tol dec")
a,b,tol,dec = [eval(x) for x in input().split()]
expr = input("f(x) = ")
#n = 0 nbr of iterations 
def f(x):
    return eval(expr)
if f(a)*f(b) >= 0:
    print("unable to evaluate")
else:
    while (b-a)/2 > tol:
        c = (a+b)/2
        n += 1
        if f(c) == 0:
            break
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
    #print(str(n))
    print(("{:." + str(dec) + "f}").format((a+b)/2))
