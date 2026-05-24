import numpy as np
from scipy import optimize

# bisect & brentq 1-dimensional root-finding methods.

def equations(v):

    x, y, z = v

    return [
        x + y-z - 5,
        x**2 + y**2+ z - 13,
        x + y**3 -z**4 -20
    ]


sol = optimize.fsolve(
    equations,
    [1,1, 1]
)

print(sol)