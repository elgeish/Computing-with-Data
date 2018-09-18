s = {1, 2, 3, 2}  # duplicity in sets is ignored
print(s)

# Example: set operations
a = set([1, 2, 3]) # make a set from a list
b = set((2, 3, 4)) # make a set from a tuple
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # set-difference
print(a.isdisjoint(b), a.issubset(b), a.issuperset(b))
