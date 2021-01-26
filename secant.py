from math import *
import math
p = []
def secant(f_new,f_old,x0,x1,tol):
    x = x1
    x_old = x0
    r = 1.12998049865083
    x_new = 0
    while abs(x-x_old) >= tol:
        x_new = x - (eval(f_new)*(x-x_old))/(eval(f_new)-eval(f_old))
        x_old = x
        x = x_new
        p.append(abs(r-x))
    print(x)
secant("exp(x) + sin(x) - 4", "exp(x_old) + sin(x_old) - 4",1,1.5,0.000001)
for i in range(0,len(p)-1):
    print(p[i+1]/p[i])
