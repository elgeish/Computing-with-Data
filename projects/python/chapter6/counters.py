from collections import Counter
counts = Counter(apples=3, oranges=5, bananas=1)
print(counts)

# Example: split the text into a list of words then count them
counts = Counter('to be or not to be'.split())
print(counts)
print(counts['question'])  # counters can be used as sparse vectors

# Example: repeat the keys as many times as their respective counts
print(tuple(counts.elements())) # unordered

# Example: get the n most common elements
tuple(counts.most_common(2)) # unordered

# Example: addition and subtraction
other = Counter('love or war'.split())
# accumulate two counters together
print(dict(counts + other))
# subtract counts (and only keep positive counts)
print(dict(counts - other))
