import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expi
from scipy.constants import elementary_charge as e, physical_constants
from numpy import euler_gamma as gamma
a = physical_constants["Bohr radius"][0]

S = 1

def Q(R):
    return e ** 2 / R * (
        1 + 5/8 * R / a - 3/4 * R ** 2 / a ** 2 - 1/6 * R ** 3 / a ** 3
    ) * np.exp(- 2 * R / a)

def A(R):
    return e ** 2 / R * (
        (
            1 + 6/5 * (gamma + np.log(R / a))
        ) * S ** 2
        - R / a * (
            11/8 + 103/20 * R / a + 49/15 * R**2 / a**2 + 11/15 * R**3 / a ** 3
        ) * np.exp(-2 * R / a)
        + 6/5 * (
            1 - R / a + 1/3 * R ** 2 / a ** 2) * np.exp(R / a) *
            ((1 - R / a + 1/3 * R ** 2 / a ** 2) * np.exp(R / a) *
            expi(-4 * R / a) - 2 * S * expi(- 2 * R / a)
        )
    )



x = np.linspace(1e-11, 3e-9, 1000)


plt.plot(x, Q(x))
plt.plot(x, A(x))
plt.show()