import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import RegularGridInterpolator


x = np.array([0,1,2,3])
y = np.array([0,1,2,3])

# % X, Y = np.meshgrid(
# %     x,
# %     y,
# %     indexing='ij'
# % )


# z = f(x,y); f= x**2+ y**2

Z = np.array([
    [0,1,4,9],
    [1,2,5,10],
    [4,5,8,13],
    [9,10,13,18]
])
interp = RegularGridInterpolator(
    (x,y),
    Z
)


# x_fine = np.linspace(0,3,100)
# y_fine = np.linspace(0,3,100)
# X_fine, Y_fine = np.meshgrid(
#     x_fine,
#     y_fine,
#     indexing='ij'
# )


# evaluate at any point:
point = [1,2]
value = interp(point)
print(value)



# ============================================================
# FINE GRID FOR INTERPOLATION
# ============================================================
x_fine = np.linspace(0,3,100)
y_fine = np.linspace(0,3,100)


XX, YY = np.meshgrid(
    x_fine,
    y_fine,
    indexing='ij'
)

# PREPARE INTERPOLATION POINTS
points = np.array([
    XX.ravel(),
    YY.ravel()
]).T

ZZ = interp(points)
ZZ = ZZ.reshape(XX.shape) # flattened into single list.

# for 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(
    111,
    projection='3d'
)

# plot interpolated surface
ax.plot_surface(
    XX,
    YY,
    ZZ,
    alpha=0.7,
    label='Interpolated Surface'
)



# ORIGINAL DATA POINTS
X, Y = np.meshgrid(
    x,
    y,
    indexing='ij'
)

ax.scatter(
    X,
    Y,
    Z,
    s=80,
    color='red',
    label='Known Points'
)



ax.set_xlabel("x")

ax.set_ylabel("y")

ax.set_zlabel("z")


ax.legend()

plt.show()





# ============================================================
# 2D PLOT
# ============================================================

plt.figure(figsize=(7,6))



# COLOR MAP PLOT
im = plt.pcolormesh(
    XX,
    YY,
    ZZ,
    shading='auto'
)


# ORIGINAL DATA POINTS
plt.scatter(
    X,
    Y,
    color='red',
    s=80,
    label='Known Points'
)


# COLOR BAR
cbar = plt.colorbar(im)

cbar.set_label("z value")



# LABELS
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Interpolated Surface")
plt.legend()
plt.show()



# ============================================================
# CONTOUR PLOT
# ============================================================
plt.figure(figsize=(7,6))

contours = plt.contour(
    XX,
    YY,
    ZZ,
    levels=10
)


# LABEL CONTOURS
plt.clabel(
    contours,
    inline=True,
    fontsize=8
)

# LABELS
plt.xlabel("x")

plt.ylabel("y")

plt.title("Contour Plot")


plt.legend()

plt.show()