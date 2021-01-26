import math
from numpy import matrix
from numpy import linalg
#x_1 = x, x_2 = y, x_3 = z
x,y,z = 1,2,3
F = matrix([["x**2 - 2*x + y**2 - z + 1"],["x*(y**2) - x - 3*y + y*z + 2"],["x*(z**2)-3*z + y*(z**2) + x*y"]])
J = matrix([["2*x - 2", "2*y", "-1"],["y**2 - 1", "x - z - 3", "y"],["z**2 + y", "x + z**2", "2*x*z + 2*y*z - 3"]])
J_inv = J.I
print(J_inv)
