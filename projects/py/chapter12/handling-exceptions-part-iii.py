import math

def foo(x):
  if not isinstance(x, int):
    raise TypeError("arguments to foo must be integers")
  if x <= 0:
    raise ValueError(f"arguments to foo must be positive: {x}")
  return(x + math.log(x))


try: 
  foo(-3)  # exception triggered and program halted 
  foo(3)  # never executed
except TypeError:  # handle TypeError exceptions
  print("Incorrect Type in sequence of foo() calls")  
except ValueError as e:  # handle ValueError exceptions
  print("Non-positive value in sequence of foo() calls:")
  print(e.args)
print("program resumes execution and is not terminated")
