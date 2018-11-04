# Handling Exceptions - Part II

```python runnable
import math

def foo(x):
  if not isinstance(x, int):
    raise TypeError("arguments to foo must be integers")
  if x <= 0:
    raise ValueError("arguments to foo must be positive")
  return(x + math.log(x))

try: 
  foo(-3)  # exception triggered and program halted 
  foo(3)  # never executed
except TypeError:  # handle TypeError exceptions
  print("Incorrect Type in sequence of foo() calls")
except ValueError:  # handle ValueError exceptions
  print("Non-positive value in sequence of foo() calls")
else: 
  print("no exceptions handled")  
finally:
  print("always handled")  
print("program resumes execution and is not terminated")
```
