# The Empty Class

When working with records or data transfer objects (DTO), all that you need
is a bunch of data members grouped together into a class. In Python, that
can be easily achieved using an empty class definition:

```python runnable
class Element:
  '''Represents an element in the periodic table.'''
  pass


na = Element()
na.atomic_number = 11
na.name = 'Sodium'

print(f'Atomic Number: {na.atomic_number}; Name: {na.name}')
```
