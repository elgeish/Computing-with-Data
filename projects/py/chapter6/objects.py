# variables are dynamically typed
x = 3
x = "three" # ok in Python

x = [1, 2, 3]  # x is a list
y = x  # both x and y refer to the same list
y.append(4)  # appending to y impacts x as well
print(x)

s = "three"
# call upper, a member method of the string object
t = s.upper()
print(t)
