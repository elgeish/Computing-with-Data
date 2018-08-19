# Example: create 3 dicts with three key-value pairs:
# ('Na', 11), ('Mg', 12), and ('Al', 13)
d = dict((('Na', 11), ('Mg', 12), ('Al', 13)))
e = {'Na': 11, 'Mg': 12, 'Al': 13}
f = dict(Na=11, Mg=12, Al=13)
print(d == e == f)  # check equivalence
print(d.keys())  # print all keys (unordered)
print(d.values())  # print all respective values

# Example: create a dict with two key-value pairs
d = {'Na': 11, 'Mg': 12, 'Al': 13}
print(d['Na'])  # retrieve value corresponding to key 'Na'
print('Li' in d)  # check if 'Li' is a key in dict d

# Example: create a dictionary with two key-value pairs
d = {'Na': 11, 'Mg': 12, 'Al': 13}
d['Li'] = 3 # add the key value pair ('Li', 3)
del d['Na']  # remove key-value pair corresponding to key 'Na'
print(d)  # print dictionary

# Example: create a dictionary from two lists: keys and values
keys = ['Na', 'Mg', 'Al']
values = [11, 12, 13]
d = dict(zip(keys, values))
print(d)

# Example: iterate over all items in a dictionary
d = dict(Na=11, Mg=12, Al=13)
# iterate over all items in d
for key, value in d.items():
  print(key, value)

# Example: a double lookup (an anti-pattern)
d = dict(Na=11, Mg=12, Al=13)
for key in d: # similar to for key in iter(d):
  print(key, d[key])

# Example: a double lookup (again)
counts = dict(apples=3, oranges=5, bananas=1)
key = 'apples'
if key in counts: # first lookup
  print(counts[key]) # second lookup
else:
  print(0)

# Example: avoiding double lookups
counts = dict(apples=3, oranges=5, bananas=1)
key = 'apples'
print(counts.get(key, 0)) # single lookup
