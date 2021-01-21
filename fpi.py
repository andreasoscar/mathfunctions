from math import *
def fpi(f,g,gprime,x0,tol):
    x = x0
    if abs(eval(gprime)) > 1:
        print("Not a valid guess")
    else:
        while abs(eval(f)) > tol:
            x = eval(g)
        print("x = " + ("{:." + str(8) + "f}").format(x))
fpi("exp(x) + sin(x) - 4", "log(4-sin(x))", "-cos(x)/(4-sin(x))",2,0.00000001)
