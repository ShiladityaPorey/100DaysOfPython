# ============================================================
#           SCIPY OPTIMIZE : MASTER LEARNING FILE
# ============================================================
#
#
# ============================================================
#
# Recommended Workflow:
#
# 1. Run ONE section at a time.
# 2. Modify parameters.
# 3. Observe convergence behavior.
# 4. Try bad initial guesses intentionally.
# 5. Plot functions before solving.
# 6. Inspect solver diagnostics.
#
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import (
    root_scalar,
    fsolve,
    minimize,
    least_squares,
    curve_fit,
    root,
    brentq,
    bisect,
    newton
)


# ============================================================
# SECTION 1 : BASIC ROOT FINDING
# ============================================================
#
# Solve:
#
# x exp(-x) = 0.1
#
# ============================================================


def f(x):
    return x*np.exp(-x) - 0.1


# ------------------------------------------------------------
# Plot function first
# ------------------------------------------------------------

x = np.linspace(0.01,10,1000)
y = f(x)

plt.figure(figsize=(6,4))
plt.plot(x,y,label='f(x)')
plt.axhline(0,color='black',linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Root Finding Example')
plt.legend()
plt.grid()
plt.show()


# ------------------------------------------------------------
# Solve using root_scalar
# ------------------------------------------------------------

# source: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html

sol = root_scalar(
    f,
    bracket=[1,10]
)
#finds only ONE root at a time ****

print("\nroot_scalar solution")
print(sol)

print("\nRoot =", sol.root)
print("Converged =", sol.converged)
print("Iterations =", sol.iterations)
print("Function calls =", sol.function_calls)


# ============================================================
# SECTION 2 : DIFFERENT ROOT METHODS
# ============================================================



# ------------------------------------------------------------
# Brent Method
# ------------------------------------------------------------

# source: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brent.html

sol_brent = root_scalar(
    f,
    bracket=[1,10],
    method='brentq'
)

print("\nBrent Method Root =", sol_brent.root)


# ------------------------------------------------------------
# Bisection Method
# ------------------------------------------------------------

# source: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html

sol_bisect = root_scalar(
    f,
    bracket=[1,10],
    method='bisect'
)

print("Bisection Root =", sol_bisect.root)


# ------------------------------------------------------------
# Newton Method
# ------------------------------------------------------------

# source : https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html

sol_newton = root_scalar(
    f,
    x0=2, 
    method='newton'
)

print("Newton Root =", sol_newton.root)


# ============================================================
# SECTION 3 : USING brentq DIRECTLY
# ============================================================


root1 = brentq(f,0.01,10)

print("Root =", root1)


# ============================================================
# SECTION 4 : USING newton DIRECTLY
# ============================================================

root2 = newton(f,1)

print("Root =", root2)


# ============================================================
# SECTION 5 : COUPLED EQUATIONS WITH fsolve
# ============================================================
#
# Solve:
#
# x + y = 5
# x^2 + y^2 = 13
#
# ============================================================


def equations(v):

    x, y = v

    return [
        x + y - 5,
        x**2 + y**2 - 13
    ]


initial_guess = [1,1]

solution = fsolve(
    equations,
    initial_guess
)

print("Solution =", solution)


# ============================================================
# SECTION 6 : USING root FOR VECTOR SYSTEMS
# ============================================================



sol_root = root(
    equations,
    [1,1]
)

print("Solution =", sol_root.x)
print("Success =", sol_root.success)
print("Message =", sol_root.message)


# ============================================================
# SECTION 7 : COSMOLOGY STYLE EXAMPLE
# ============================================================
#
# Mimics reheating-type systems.
#
# ============================================================


C = 35


def reheating_system(v):

    Nreh, Treh = v

    return [
        Nreh + np.log(Treh) - C,
        Treh - np.exp((30-Nreh)/2)
    ]


sol_cosmo = fsolve(
    reheating_system,
    [10,1e10]
)

print("Nreh, Treh =", sol_cosmo)


# ============================================================
# SECTION 8 : FUNCTION MINIMIZATION
# ============================================================
#
# Minimize:
#
# (x-3)^2 + 1
#
# ============================================================


def fmin(x):
    return (x - 3)**2 + 1


sol_min = minimize(
    fmin,
    x0=0
)

print(sol_min)
print("Minimum at x =", sol_min.x)


# ============================================================
# SECTION 9 : MULTI-DIMENSIONAL MINIMIZATION
# ============================================================



def chi2(v):

    x, y = v

    return (x-2)**2 + (y-1)**2


sol_multi = minimize(
    chi2,
    [0,0]
)

print("Minimum at =", sol_multi.x)


# ============================================================
# SECTION 10 : DIFFERENT MINIMIZATION METHODS
# ============================================================


methods = [
    'Nelder-Mead',
    'Powell',
    'BFGS'
]

for method in methods:

    sol = minimize(
        fmin,
        x0=0,
        method=method
    )

    print(f"\nMethod = {method}")
    print("Minimum =", sol.x)


# ============================================================
# SECTION 11 : BOUNDED MINIMIZATION
# ============================================================


sol_bound = minimize(
    fmin,
    x0=0,
    bounds=[(0,10)]
)

print("Minimum =", sol_bound.x)


# ============================================================
# SECTION 12 : LEAST SQUARES
# ============================================================



def residuals(v):

    x, y = v

    return [
        x + y - 5,
        x**2 + y**2 - 13
    ]


sol_ls = least_squares(
    residuals,
    [1,1]
)

print("Solution =", sol_ls.x)


# ============================================================
# SECTION 13 : curve_fit
# ============================================================


xdata = np.linspace(0,10,20)

ydata = 3*xdata + 2 + np.random.normal(0,1,20)


# ------------------------------------------------------------
# Model function
# ------------------------------------------------------------


def model(x,m,c):
    return m*x + c


params, covariance = curve_fit(
    model,
    xdata,
    ydata
)

print("Parameters =", params)


# ------------------------------------------------------------
# Plot fit
# ------------------------------------------------------------

plt.figure(figsize=(6,4))
plt.scatter(xdata,ydata,label='Data')
plt.plot(xdata,model(xdata,*params),label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve_fit Example')
plt.legend()
plt.grid()
plt.show()


# ============================================================
# SECTION 14 : IMPORTANT DIAGNOSTICS
# ============================================================


print("Success =", sol_multi.success)
print("Message =", sol_multi.message)
print("Function evaluations =", sol_multi.nfev)
print("Function value =", sol_multi.fun)


# ============================================================
# SECTION 15 : FAILURE MODES
# ============================================================
#
# VERY IMPORTANT SCIENTIFIC LESSON
#
# Things that can fail:
#
# - bad initial guesses
# - multiple roots
# - discontinuities
# - divergence
# - overflow
# - underflow
# - nonphysical solutions
# - local minima
#
# Never trust a numerical solver blindly.
#
# ============================================================



print("Always verify physicality of solutions.")


# ============================================================
# SECTION 16 : PROFESSIONAL WORKFLOW
# ============================================================
#
# Correct workflow:
#
# 1. Plot function
# 2. Understand physics
# 3. Choose good initial guess
# 4. Solve numerically
# 5. Check convergence
# 6. Verify physical branch
# 7. Test multiple guesses
#
# ============================================================



print("Good scientific computing requires physical intuition.")


# ============================================================
# SECTION 17 : NEXT STEP
# ============================================================
#
# After scipy.optimize:
#
# Learn:
#
# scipy.integrate
#
# especially:
#
# - quad
# - solve_ivp
#
# ============================================================

print("\n" + "="*60)
print("END OF SCIPY OPTIMIZE MASTER FILE")
print("="*60)
