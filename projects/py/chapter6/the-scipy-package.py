from scipy import sparse
from numpy import *

# create a sparse matrix using LIL format
m = sparse.lil_matrix((5,5))
m[0, 0] = 1
m[0, 1] = 2
m[1, 1] = 3
m[2, 2] = 4
print("m =\n" + str(m))
# convert a to CSR format
b = sparse.csr_matrix(m)
print("b + b =\n" + str(b + b)) # matrix addition
