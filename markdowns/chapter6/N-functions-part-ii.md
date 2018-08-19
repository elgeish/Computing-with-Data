# Functions - Part II

Here are a few more examples of functions in Python:

```python runnable
# Example: nested functions - variable scope (erroneous)
# calling create_accumulator fails with the following error message:
# "local variable 'tally' referenced before assignment"
def create_accumulator(seed=0):
  tally = seed
  def accumulate(x):
    tally += x # local to accumulate(x)
    return tally
  return accumulate

# Example: nested functions - variable scope (the nonlocal statement)
def create_accumulator(seed=0):
  tally = seed
  def accumulate(x):
    nonlocal tally # the fix
    tally += x
    return tally
  return accumulate

accumulate = create_accumulator()
print(accumulate(2))
print(accumulate(3))
print(accumulate(5))

# Example: the global statement
tally = 0
def accumulate(x):
  global tally
  tally += x
  return tally

print(accumulate(2))
print(accumulate(3))
print(accumulate(5))

# Example: returning multiple objects
def foo(x, y):
  return x + y, x - y

a, b = foo(1, 2)  # unpack the returned tuple into a and b
print(a)
print(b)

# Example: a variadic function
# the syntax *lines makes this function variadic
def print_lines(prefix, *lines):
  for line in lines:
    print(prefix, line)

# call the function with varargs
print_lines('[varargs example]', 'hello', 'world')

# Example: an equivalent to the example above
# no * operator, just an ordinary tuple
def print_lines(prefix, lines):
  for line in lines:
    print(prefix, line)

# call the function with a tuple parameter
print_lines('[tuple example]', ('hello', 'world'))

# Example: unpacking the argument list
def power(base, exponent):
  return base ** exponent

data = [2, 3] # or (2, 3)
print(power(*data))

# Example: unpacking the argument list from a dictionary
def power(base, exponent):
  return base ** exponent

data = {'base': 2, 'exponent': 3}
print(power(**data))

# Example: named parameters packed into a dictionary
def print_latest_championship(**data):
  for team, year in data.items():
    print(team + ':', year)  # dictionaries are unordered

print_latest_championship(cavaliers=2016, warriors=2018)

# Example: combining regular parameters, *args, and **kwargs
def print_latest_championship(prefix, *args, **kwargs):
  for line in args:
    print(prefix, line)
  for team, year in kwargs.items():
    print(prefix, team + ':', year)  # dictionaries are unordered

print_latest_championship(
  '[NBA]',
  'Conference Finals',
  'Team: Year',
  cavaliers=2016,
  warriors=2018)
```
