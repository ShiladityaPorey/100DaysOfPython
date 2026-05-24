import numpy as np
from scipy import optimize

# from scipy.optimize import (
#     root_scalar,
#     fsolve,
#     minimize,
#     least_squares,
#     curve_fit,
#     root,
#     brentq,
#     bisect,
#     newton
# )


# ============================================================
# FUNCTION
# ============================================================

def f(x):
    return x*np.exp(-x) - 0.1


# ============================================================
# ROOT_SCALAR  (Automatic method selection)
# ============================================================

sol_root_scalar = optimize.root_scalar(f,bracket=[1,10])

print("\nROOT_SCALAR")
print("Root            =", sol_root_scalar.root)
print("Iterations      =", sol_root_scalar.iterations)
print("Method          =", sol_root_scalar.method)
print("Residual Error  =", abs(f(sol_root_scalar.root)))


# ============================================================
# BISECTION METHOD
# ============================================================

a = 1
b = 10

sol_bisect, result_bisect = optimize.bisect(f,a,b,full_output=True)

# theoretical error bound
error_bisect = (b-a)/(2**result_bisect.iterations)

print("\nBISECTION METHOD")
print("Root                 =", sol_bisect)
print("Iterations           =", result_bisect.iterations)
print("Theoretical Error    =", error_bisect)
#print("Residual Error       =", abs(f(sol_bisect)))


# ============================================================
# NEWTON METHOD
# ============================================================

sol_newton, result_newton = optimize.newton(f,x0=2,full_output=True)

print("\nNEWTON METHOD")
print("Root                 =", sol_newton)
print("Iterations           =", result_newton.iterations)
print("Converged            =", result_newton.converged)
#print("Residual Error       =", abs(f(sol_newton)))

# Newton has no simple theoretical error formula
# because convergence depends on local behavior


# ============================================================
# FSOLVE METHOD
# ============================================================

sol_fsolve, info_fsolve, ier_fsolve, mesg_fsolve = optimize.fsolve(f,x0=2,#1,# 1 gives moreresidual error
    full_output=True
)

print("\nFSOLVE METHOD")
print("Root                 =", sol_fsolve[0])
print("Function Calls       =", info_fsolve['nfev'])
print("Converged Flag       =", ier_fsolve)
print("Message              =", mesg_fsolve)
# print("Residual Error       =", abs(f(sol_fsolve[0])))


# ============================================================
# COMPARISON
# ============================================================

print("\nSUMMARY")

print(f"{'Method':<15} {'Root':<20} {'Residual Error'}")

print("-"*55)

print(f"{'root_scalar':<15} "
      f"{sol_root_scalar.root:<20.12f} "
      f"{abs(f(sol_root_scalar.root)):.3e}")

print(f"{'bisect':<15} "
      f"{sol_bisect:<20.12f} "
      f"{abs(f(sol_bisect)):.3e}")

print(f"{'newton':<15} "
      f"{sol_newton:<20.12f} "
      f"{abs(f(sol_newton)):.3e}")

print(f"{'fsolve':<15} "
      f"{sol_fsolve[0]:<20.12f} "
      f"{abs(f(sol_fsolve[0])):.3e}")