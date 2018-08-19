import matplotlib.pyplot as plt
from numpy.random import randn

plt.hist(randn(10000), 50)
plt.xlabel(r"$x$")
plt.ylabel(r"$count$")
plt.title(r"Histogram of 10000 Gaussian $\mathcal{N}(0, 1)$ Samples")
plt.xlim([-4, 4])
plt.show()
