from math import *
import math
p = []
x = 1.3
f = "exp(sin(x)**3) + x**6 - 2*x**4 - x**3 - 1"
fprime = "(x**2)*(-3 - 8*x + 6*x**3) + 3*exp(sin(x)**3) * cos(x) * sin(x)**2"
x_old = 0
x_true = 1.53013350816662
n = 0
p = []
while abs(x-x_old) > 10**(-6):
    x_old = x
    x = x - eval(f)/eval(fprime)
    p.append(abs(x-x_true))
    n += 1
print(x,n)
for i in range(0,len(p)-1):
    print(p[i+1]/p[i])
