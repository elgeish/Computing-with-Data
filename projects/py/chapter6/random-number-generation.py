import numpy as np

# N(0, 1) Gaussian
print("np.random.normal(size=(2, 2)) =")
print(np.random.normal(size=(2, 2)))
# uniform over [0,1]
print("np.random.uniform(size=(2, 2)) =")
print(np.random.uniform(size=(2, 2)))
# uniform over {1..10}
print("np.random.randint(10, size=(2, 2)) =")
print(np.random.randint(10, size=(2, 2)))
# random permutation over 1..6
print("np.random.permutation(6) =")
print(np.random.permutation(6))
