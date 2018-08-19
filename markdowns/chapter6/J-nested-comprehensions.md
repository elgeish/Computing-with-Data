# Nested Comprehensions

Comprehensions can be nested; the expression that evaluates to an element
in the result can be a comprehension:

```python runnable
# create a 3x5 matrix of 1's
matrix = [[1 for j in range(5)] for i in range(3)]
print(matrix)
```
