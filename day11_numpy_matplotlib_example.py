#source: https://numpy.org/doc/stable/reference/routines.math.html
#To install:
#https://www.geeksforgeeks.org/how-to-install-matplotlib-on-macos/
#August 11, 2024
#shiladitya porey


import numpy as np
import matplotlib.pyplot as plt  # Corrected import

print(np.sqrt(4))

xs = np.linspace(1, 10, 100)
ys = (xs**4) 

plt.plot(xs, ys)
plt.show()

