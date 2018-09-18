# Example: if-else
x = 3
if x > 0:
  # if block
  print("x is positive")
  sign = 1
elif x == 0:
  # elif (else-if) block
  print("x equals zero")
  sign = 0
else:
  # else block
  print("x is negative")
  sign = -1
print(sign)  # new block

# Example: for-loops
a = [1, 2, 3, -4]
for x in a:
  # start of the for block
  print(x)

print(x)  # new block, but x is still in scope!

# Example: the enumerate function
a = [1, 2, 3, -4]
for i, x in enumerate(a):
  print('a at', i, '=', x)

# Example: a loop combined with a conditional
a = [1, 2, 3, -4]
abs_sum = 0
for x in a:
  if x > 0:
    abs_sum += x
  else:
    abs_sum += -x
print(abs_sum)

# Example: alternatively, the Pythonic way to replace the above
print(sum(abs(x) for x in a))

# Example: else as a completion clause
s = 'Jane is 42 years old'
for c in s:
  if c.isdigit():
    print('Found:', c)
    break
else:
  print('No digit was found!')

# Example: when the else completion clause is executed
budget = 13
costs = [5, 3, 2]
for i, cost in enumerate(costs):
  print('Item', i, 'for', cost, 'unit(s) of cost: ', end='')
  budget -= cost
  if budget > 0:
    print('acquired')
  else:
    print('insufficient funds')
    break
else:
  print('Remaining budget:', budget)
