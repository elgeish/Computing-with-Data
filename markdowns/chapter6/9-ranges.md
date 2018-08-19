# Ranges

The built-in function `range` is often used to access a list of evenly-spaced
integers:

```python runnable
print(list(range(0, 10, 1)))
print(tuple(range(0, 10))) # same as tuple(range(0, 10, 1))
print(tuple(range(10))) # same as tuple(range(0, 10))
print(tuple(range(0, 10, 2))) # step size of 2
```
