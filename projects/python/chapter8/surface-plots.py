import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 3 * x ** 2 + 5 * y ** 2


x_grid = np.linspace(-2, 2, 30)
y_grid = np.linspace(-2, 2, 30)
xx, yy = np.meshgrid(x_grid, y_grid)
zz = f(xx, yy)
surf_figure = plt.figure()
figure_axes = Axes3D(surf_figure)
figure_axes.plot_surface(xx, yy, zz, rstride=1, cstride=1, cmap="Blues")
plt.show()
