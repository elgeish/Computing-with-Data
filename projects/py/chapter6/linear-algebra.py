import numpy as np

# Example: the mean function for ndarrays, columns, and rows
m = np.array([[0, 1], [2, 3]])
# global average
print("np.mean(m) =", np.mean(m))
# average of columns
print("np.mean(m, axis=0) =", np.mean(m, axis=0))
# average of rows
print("np.mean(m, axis=1) =", np.mean(m, axis=1))

# Example: matrix inverse and multiplication
m = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) + np.identity(3)
print("m =\n" + str(m))
m_inv = np.linalg.inv(m)
print("inverse of m =\n" + str(m_inv))
print("m times its inverse =\n" + str(np.dot(m, m_inv)))

# Example: the matrix object
m = np.mat([[0, 1], [2, 3]])
print("m =\n" +  str(m))
print("m[:, 0] =\n" + str(m[:, 0])) # column vector
print("m[0, :] =\n" + str(m[0, :])) # row vector
# compute bilinear form v^T * A * v (matrix multiplication)
print("m[0, :] * m * m[:, 0] =")
print(m[0, :] * m * m[:, 0])

# Example: set operations
a = np.array(['a', 'b', 'a', 'b'])
b = np.array(['c', 'd'])

print("a =", a)
print("np.unique(a) =", np.unique(a))
print("np.union1d(a, b) =", np.union1d(a, b))
print("np.intersect1d(a, b) =", np.intersect1d(a, b))

# Example: generating ndarrays containing pseudo-random numbers
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
