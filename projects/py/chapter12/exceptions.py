import math

def foo(x):
  if not isinstance(x, int):
    raise TypeError("arguments to foo must be integers")
  if x <= 0:
    raise ValueError("arguments to foo must be positive")
  return(x + math.log(x))


foo(-3)  # exception triggered and program halted 
foo(3)  # never executed
