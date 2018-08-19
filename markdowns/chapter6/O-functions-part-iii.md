# Functions - Part III

In this part, we explore anonymous functions:

```python runnable
# Example: a lambda expression is a very convenient way to create
# a single-expression anonymous function
pairs = ((1, 3), (4, 2))
print(sorted(pairs, key=lambda p: p[1]))

# Example: a lambda expression can be named and reused
pairs = ((1, 3), (4, 2))
get_second = lambda p: p[1]
print(sorted(pairs, key=get_second))
print('max:', max(pairs, key=get_second))

# Example: a recursive lambda
factorial = lambda x: factorial(x - 1) * x if x else 1
print(factorial(5))

# Example: a lambda with multiple arguments
power = lambda x, y: x ** y
print(power(5, 2))

# Example: a variadic lambda
from math import sqrt
norm = lambda *args: sqrt(sum(x * x for x in args))
print('norm:', norm(1, -2, 2))

# Example: a trick to print a lambda's arguments
norm = lambda *a: 0 if print(a) else sqrt(sum(x * x for x in a))
print('norm:', norm(1, -2, 2))
```
