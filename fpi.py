from math import *
import math
def fpi(f,g,gprime,x0,tol,step):
    x = x0
    k = 0
    if abs(eval(gprime)) >= 1:
        print("Not a valid guess")
    else:
        while abs(eval(f)) > tol:
            if k >= step:
                break
            else:
                k += 1
                x = eval(g)
        print("x = " + ("{:." + str(8) + "f}").format(x))
fpi("-4x-0", "0", "-4",0,0.00000001)
#fpi("exp(x) + sin(x) - 4", "log(4-sin(x))", "-cos(x)/(4-sin(x))",2,0.00000001)
