import sympy

from sympy.abc import x, y, z, phi, zeta, eta

from sympy import symbols, sqrt, tan, atan2, Matrix, simplify, pprint, solve
from sympy.vector import CoordSys3D

x_a, y_a, z_a = symbols("x_a y_a z_a", real=True)
x_b, y_b, z_b = symbols("x_b y_b z_b", real=True)
R = symbols("R", real=True, positive=True)


# R = CoordSys3D('R')

# r =   MatrixSymbol("r", 3, 1)
# r_a = MatrixSymbol("r_a", 3, 1)
# r_b = MatrixSymbol("r_b", 3, 1)

# zeta = (sqrt((r - r_a) * (r - r_a).T) + sqrt((r - r_b) * (r - r_b).T)) / sqrt((r_a - r_b) * (r_a - r_b).T)
# eta = (sqrt((r - r_a) * (r - r_a).T) - sqrt((r - r_b) * (r - r_b).T)) / sqrt((r_a - r_b) * (r_a - r_b).T)
# phi = atan2(r[2], r[0])

# zeta = (sqrt((x-x_a)**2 + (y-y_a)**2 + (z-z_a)**2) + sqrt((x-x_b)**2 + (y-y_b)**2 + (z-z_b)**2)) / R
# eta = (sqrt((x-x_a)**2 + (y-y_a)**2 + (z-z_a)**2) - sqrt((x-x_b)**2 + (y-y_b)**2 + (z-z_b)**2)) / R
# zeta = (sqrt((x-x_a)**2 + (y-y_a)**2 + (z-z_a)**2) + sqrt((x-x_b)**2 + (y-y_b)**2 + (z-z_b)**2)) / sqrt((x_a-x_b)**2 + (y_a-y_b)**2 + (z_a-z_b)**2)
# eta = (sqrt((x-x_a)**2 + (y-y_a)**2 + (z-z_a)**2) - sqrt((x-x_b)**2 + (y-y_b)**2 + (z-z_b)**2)) / sqrt((x_a-x_b)**2 + (y_a-y_b)**2 + (z_a-z_b)**2)
# phi = atan2(z, x)

res = solve([(x-x_a)**2 + (y-y_a)**2 + (z-z_a)**2 - (R / 2 * (zeta + eta)) ** 2,
    (x-x_b)**2 + (y-y_b)**2 + (z-z_b)**2 - (R / 2 * (zeta + eta) - R * eta) ** 2,
    z - tan(phi) * x], (x, y, z))


# m = Matrix([zeta, eta, phi])

# inv_j = simplify(m.jacobian([x,y,z])).inv()
# det = m.jacobian([x,y,z]).det()

# det.subs([(zeta, symbols("zeta")), (eta, symbols("eta")), (phi, symbols("phi"))])
# # det = simplify(m.jacobian(r).det())

# # pprint(cse(det))
# pprint(det)