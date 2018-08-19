# Tuples

A tuple is an immutable sequence of objects of potentially different types.
Each object can be referred to using the square bracket index notation.
Tuples are defined using parenthesis (or the built-in function `tuple`):

```python runnable
a = (1, 2) # tuple of two integers
b = 1, 2 # alternative way to define a tuple
a[0] = 3 # error: modifying an immutable tuple after its creation

a = (1, 2)  # tuple of two integers
b = (1, "one")  # tuple of an integer and a string
c = (a, b)  # tuple containing two tuples
print(b[1])  # prints the second element of b
print(c[0])  # prints the first element of c

# Example: unpacking
t = (1, 2, 3)  # tuple of three integers
(a, b, c) = t  # copy first element of t to a, second to b, etc.
a, b, c = t  # alternative syntax to accomplish the same thing
print(a)
print(b)
print(c)

# Example: nested tuples
t = (1, (2, 3))  # tuple containing an integer and a tuple
# copy the first element of t to a, second to (b, c)
(a, (b, c)) = t
a, (b, c) = t
print(a)
print(b)
print(c)

# Example: erroneous unpacking
a, b, c = t  # error: not enough values to unpack
```
