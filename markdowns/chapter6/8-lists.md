# Lists

Lists are similar to tuples, but they're mutable, and they're defined using
square brackets (or the built-in function `list`):

```python runnable
a = [1, 2, 3]  # list containing three integers
b = [a, "hello"]  # list containing a list and a string
b.append(4)  # modify existing list by appending an element
print(a)
print(b)

# Example: inserting, removing, and sorting elements
a = [1, 2, 3] 
a.insert(1, 100)  # insert 100 before index 1
print(a)
a.remove(2)  # remove first occurrence of 2
print(a)
a.sort()  # sort list
print(a)
a.extend([20, 21, 23])  # extend list with an additional list
print(a)
b = sorted(a)
print(b)

# Example: deleting an element
a = ['hello', ', ', 'world']
print(len(a))
del a[1]
print(len(a))
print(a)

# Example: the + operator
print([1, 2, 3] + [4, 5] + [6])
```
