import numpy as np

# Example: ndarry objects
# create 2x3 ndarray of floats from a list of lists
m = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print("m.shape =", m.shape)
print("m.dtype =", m.dtype)
print("m =\n" + str(m))
m = m.astype(np.int32)  # cast the ndarray from float to int
print("m =\n" + str(m))

# Example: other ways to create ndarry objects
m1 = np.zeros((2, 3)) # create a 2x3 ndarray of zeros
m2 = np.identity(3) # the 3x3 identity matrix
m3 = np.ones((2, 3, 2)) # create a 2x3x4 ndarray of ones
print("m1 =\n" + str(m1))
print("m2 =\n" + str(m2))
print("m3 =\n" + str(m3))

# Example: ndarry operations
m1 = np.identity(3)
m2 = np.ones((3, 3))
print("2 * m1 =\n" + str(2 * m1))
print("m1 + m2 =\n" + str(m1 + m2))

# Example: the sublist notation in the one-dimensional case
a = np.array(range(9))
print("a[:] =", a[:])
print("a[3] =", a[3])
print("a[3:6] =", a[3:6])
a[3:6] = -1
print("a =", a)

# Example: the logical condition in the one-dimensional case
a = np.array(range(7))
# create an bool (mask) ndarray of True/False
print("a < 3 =", a < 3)
# refer to all elements that are lower than 3
print("a[a < 3] =", a[a < 3])
a[a < 3] = 0  # replace elements lower than 3 by 0
print("a =", a)

# Example: the sublist notation in the two-dimensional case
m = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("m =\n" + str(m))
print("m[:, 1] =\n", m[:, 1]) # second column
# first two rows of the 2nd column
print("m[0:2, 1] =\n", m[0:2, 1])
# first 2 rows of the first two columns
print("m[0:2, 0:2] =\n" + str(m[0:2, 0:2]))

# Example: the logical condition in the two-dimensional case
m = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("m =\n" + str(m))
print("m < 3 =\n" + str(m < 3))
print("m[m < 3] =\n", m[m < 3])
m[m < 3] = 0
print("m =\n" + str(m))

# Example: another way to refer a subset of a two-dimensional ndarray
m = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("m =\n" + str(m))
# first row
print("m[0] =\n", m[0])
# first and third rows
print("m[[0, 2]] =\n" + str(m[[0, 2]]))
# third and first rows
print("m[[2, 0]] =\n" + str(m[[2, 0]]))
# refer to the (0, 2) and (1, 0) elements
print("m[[0, 1], [2, 0]] =\n", m[[0, 1], [2, 0]])

# Example: assignment
a = np.array(range(9))
b = a[0:4] # b refers to elements 0-3
b[1] = 42 # modify second element of b
print(a) # a is modified as well
