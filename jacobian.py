import math
import numpy as np
p = [] #true error array
x_n = np.matrix([1,2,3]).transpose()
r = np.matrix([1,1,1]).transpose()
for i in range(10):
    x,y,z = x_n.item(0),x_n.item(1),x_n.item(2)
    F = np.matrix([[eval("x**2 - 2*x + y**2 - z + 1")],[eval("x*(y**2) - x - 3*y + y*z + 2")],[eval("x*(z**2)-3*z + y*(z**2) + x*y")]])
    J = np.matrix([[eval("2*x - 2"), eval("2*y"), eval("-1")],[eval("y**2 - 1"), eval("2*x*y - 3 + z"), eval("y")],[eval("z**2 + y"), eval("x + z**2"), eval("2*x*z + 2*y*z - 3")]])
    x_n = x_n - (J.I)*F
    e = math.sqrt((r.item(0)-x_n.item(0))**2 + (r.item(1)-x_n.item(1))**2 + (r.item(2) - x_n.item(2))**2)
    print(x_n.item(0),x_n.item(1),x_n.item(2),e)
    p.append(e)
for i in range(0,len(p)-1):
    print(p[i+1]/p[i])
print(x_n)
