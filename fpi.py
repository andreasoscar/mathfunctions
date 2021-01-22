from math import *
import math
data = dict()
p = []
def fpi(f,g,gprime,x0,tol,step):
    x = x0
    r = 0.739085133385334
    k = 0
    while abs(r - x) >= tol:
        if k >= step:
            break
        else:
            k += 1
            x = eval(g)
            p.append(abs(r-x))
    print("n" + " = " + str(k))
    print(abs(eval(gprime)))
    print("x = " + ("{:." + str(12) + "f}").format(x))
fpi("cos(x) - x", "cos(x)", "-sin(x)",0,0.000001,500)
for i in range(0,len(p)-1):
    print(p[i+1]/p[i])
