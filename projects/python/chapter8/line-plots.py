import matplotlib.pyplot as plt
from numpy import array

x_grid = array(range(1, 100)) / 30.0
plt.figure()  # open a figure
plt.plot(x_grid, x_grid, "k-")  # draws a solid line
plt.plot(x_grid, x_grid ** 2, "k--")  # draws a dashed line
plt.plot(x_grid, x_grid ** 3, "k.")  # draws a dotted line
plt.xlabel(r"$x$")
plt.ylabel(r"$y=f(x)$")
plt.title("Linear, Quadratic, and Cubic Growth")
plt.show()
