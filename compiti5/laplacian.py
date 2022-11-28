from sympy import symbols, exp, sqrt, simplify, pprint
from sympy.vector import CoordSys3D, laplacian


x_a, y_a, z_a = symbols("x_a, y_a, z_a", real=True)
a = symbols("a", real=True)

C = CoordSys3D('C')


res = laplacian(exp(-sqrt((C.x - x_a) ** 2 + (C.y - y_a) ** 2 + (C.z - z_a) ** 2) / a))



pprint(simplify(res))

