# Handling Exceptions - Part III

```python runnable
import math

# Custom exception: either type or value error
class InvalidTypeOrValueError(Exception):
  def __init__(self, a_val, a_type):  # custom constructor
    # calls super class constructor (Python 3 syntax)
    super().__init__("incorrect type and value. " + 
      "val: " + str(a_val) + " " + "type: " + str(a_type))
    self.val = a_val
    self.type = a_type


def foo(x):
  if not isinstance(x, int) or x<=0:
    raise InvalidTypeOrValueError(x,type(x))
  return(x + math.log(x))


try: 
  foo(-3) 
  foo(3)
except InvalidTypeOrValueError as e:
  print("Incorrect type or value in sequence of foo() calls: ")
  print(e.args)
```
