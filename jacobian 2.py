import math
import numpy as np
#x_1 = x, x_2 = y, x_3 = z
x,y,z = 1,2,3
F = np.matrix([[eval("x**2 - 2*x + y**2 - z + 1")],[eval("x*(y**2) - x - 3*y + y*z + 2")],[eval("x*(z**2)-3*z + y*(z**2) + x*y")]])
J = np.matrix([[eval("2*x - 2"), eval("2*y"), eval("-1")],[eval("y**2 - 1"), eval("x - z - 3"), eval("y")],[eval("z**2 + y"), eval("x + z**2"), eval("2*x*z + 2*y*z - 3")]])
J_inv = np.linalg.inv(J)
x = np.matrix([x,y,z]).transpose()
for i in range(10):
    x,y,z = x.item(0),x.item(1),x.item(2)
    x = x - np.dot(J_inv,F)
print(x)
