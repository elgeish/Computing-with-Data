from collections import Counter

# Example: a simple, mundane transformation to a list
words = ['apple', 'banana', 'carrot']
modes = []
for word in words:
  counter = Counter(word)
  # most_common(n) returns a list and the *
  # operator expands it before calling append(x)
  modes.append(*counter.most_common(1))
print(modes)

# Example: the Pythonic way (using a list comprehension)
print([Counter(w).most_common(1)[0] for w in words])

# Example: select and transform
print([Counter(w).most_common(1)[0] \
       for w in words if len(w) > 5])

# Example: mimicing nested for loops and multiple conditionals
x = (0, 1, 2, 7)
y = (9, 0, 5)
print([(a, b) for a in x for b in y if a != 0 and b != 0])
# alternatively
print([(a, b) for a in x if a != 0 for b in y if b != 0])
