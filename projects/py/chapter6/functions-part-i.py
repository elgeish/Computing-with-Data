def scale(vector, factor):
  return [x * factor for x in vector]

print(scale([1, 2, 3], 2))
print(scale({1, 2, 3}, 2)) # unordered
print(scale(factor=2, vector=(1, 2, 3)))
# the * operator works with lists and tuples as well,
# but it has different semantics:
print(scale([(1, 2, 3)], 2))

# Example: recursion
from collections import Sequence

def scale(vector, factor, recursively=False):
  if recursively:
      # call scale recursively for sequence elements
      return [scale(x, factor, True) if isinstance(x, Sequence)
              else (x * factor) for x in vector]
  else:
    return [x * factor for x in vector]

print(scale([(1, 2, 3)], 2))  # recursively is False by default
print(scale([(1, 2, 3)], 2, recursively=True))

# Example: recursion (two functions)
def scale_recursively(vector, factor):
  return [scale_element(x, factor) for x in vector]

def scale_element(element, factor):
  if isinstance(element, Sequence):
    return scale_recursively(element, factor)
  else:
    return element * factor

print(scale_recursively([1, [2, 3]], 2))

# Example: nested functions
def scale_recursively(vector, factor):
  def scale_element(element):
    if isinstance(element, Sequence):
      return scale_recursively(element, factor)
    else:
      return element * factor
  return [scale_element(x) for x in vector]

print(scale_recursively([1, [2, 3]], 2))

# Example: currying
def create_line_printer(prefix):
  def print_suffix(suffix):
    print(prefix, suffix)
  return print_suffix

write = create_line_printer('[currying example]')
write('this is useful for behavior reuse')
write('and for testing multiple behaviors')
write = create_line_printer('[a prefix to test]')
write('the call of write(x) did not change')
write('even though the prefix had changed')

# Example: passing a function as a parameter
def sort_by_second(pairs):
  def get_second(pair):
    return pair[1]
  return sorted(pairs, key=get_second)

pairs = ((1, 3), (4, 2))
print(sort_by_second(pairs))

# Example: passing a callable object as a parameter
pairs = ((1, 3), (4, 2))
from operator import itemgetter
print(sorted(pairs, key=itemgetter(1)))
