import numpy as np
import os

# Example: the save and load functions
m = np.array([[1, 2, 3], [4, 5, 6]])
file_name = "matrix.npy"
np.save(file_name, m)
print("File Size in Bytes:", os.stat(file_name).st_size)
loaded = np.load(file_name)
print(loaded)

# Example: the savez and savez_compressed functions
file_name = "output.npz"
for save in np.savez, np.savez_compressed:
  save(file_name, foo=np.array([1, 2]), bar=np.array([3, 4]))
  arrays = np.load(file_name)
  print("Using {}, {} bytes:".format(
    save.__name__,
    os.stat(file_name).st_size))
  for key, value in arrays.items(): # unordered
    print("\t{}: {}".format(key, value))
  print() # empty line

# Example: the savetxt and loadtxt functions
def print_file(file_name):
  with open(file_name) as f:
    for line in f:
      print(line, end='')

file_name = "array.txt" 
np.savetxt(file_name, np.array([[1, 3], [2, 4]]))
loaded = np.loadtxt(file_name)
print("Using numpy.loadtxt:\n{}".format(loaded))
print("Text File Content:")
print_file(file_name)
