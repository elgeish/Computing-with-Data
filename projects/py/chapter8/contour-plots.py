import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return 3 * x ** 2 + 5 * y ** 2


x_grid = np.linspace(-2, 2, 100)
y_grid = np.linspace(-2, 2, 100)
# Create two ndarrays xx, yy containing x and y coordinates
xx, yy = np.meshgrid(x_grid, y_grid)
zz = f(xx, yy)
# Draw contour graph with 6 levels using gray colormap
#   (white=high, black=low)
plt.contourf(xx,
             yy,
             zz,
             6,
             cmap="gray")
# Add black lines to highlight contours levels
plt.contour(xx,
            yy,
            zz,
            6,
            colors = "black",
            linewidth = .5)
plt.show()
