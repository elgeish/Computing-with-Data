# Scalar Data Types

Python's scalar data types and operators are similar to those in C++ and Java.
That said, Python's boolean operators are expressed using keywords: `and`, `or`,
and `not`:

```python runnable
a = 42
b = float(a)
c = str(a)
d = bool(a)
# print the type and value for each object above
for x in a, b, c, d:
  print("type: {}, value: {}".format(type(x), x))

x = True
y = False
print(x and y)
print(x or y)
print(not x)

int("a")
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## ValueError: invalid literal for int() with base 10: 'a'
```
