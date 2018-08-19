# Material Differences between Python 3 and 2

In this section, we describe material differences between the two versions;
see [this article(https://wiki.python.org/moin/Python2orPython3) for more
details about the version change. Lines prefixed with `##` are output lines.

```python
# Example: unicode support

# Python 2.x
print(type(''))  # str
print(type(u''))  # unicode
## <type 'str'>
## <type 'unicode'>

# Python 3.x
print(type(''))  # str
print(type(u''))  # also str
## <class 'str'>
## <class 'str'>


# Example: the print statement

# Python 2.x
print(13, 42)
## (13, 42)

# Python 3.x
# print 13, 42
##  File "<stdin>", line 1
##    print 13, 24
##           ^
## SyntaxError: Missing parentheses in call to 'print'


# Example: the print function

# Python 3.x (or 2.x with the import from 3.x)
# imports from the future must come first in the file
from __future__ import print_function
print('hello from the future')
print(print)  # the print function is an object
print(13, 42)
## hello from the future
## <built-in function print>
## 13 42


# Example: division

# Python 2.x
print(1 / 3)  # floor (integer) division
print(1.0 / 3)  # true division
## 0
## 0.333333333333

# Python 3.x (or 2.x with the import from 3.x)
from __future__ import division
print(1 // 3)  # floor (integer) division
print(1 / 3)  # true division
## 0
## 0.3333333333333333
```
