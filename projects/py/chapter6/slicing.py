a = list(range(10))
print(a[:])  # starting index (0) to end index (9)
print(a[3:])  # index 3 to end (9)
print(a[:3])  # index 0 to 2
print(a[0:10:2])  # index 0 to 9, skipping every other element

# Example: negative values
a = list(range(10))
print(a[::-1])  # start index (0) to end (9) - backwards
print(a[-3:])  # index 3 from the end (7) to the end (9)

# Example: zipping
a = [1, 2, 3]
b = ["one", "two", "three"]
print(list(zip(a, b)))

a = [1, 2, 3]
b = ["one", "two", "three"]
c = ["uno", "dos", "tres"]
print(list(zip()))
print(list(zip(a)))
print(list(zip(a, b, c)))
