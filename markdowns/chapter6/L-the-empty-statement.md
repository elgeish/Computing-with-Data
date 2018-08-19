# The Empty Statement

The empty statement, `pass`, is another example of Python syntax that one might
find confusing at first glance:

```python runnable
budget = 13
costs = [5, 3, 2]
for i, cost in enumerate(costs):
  pass # TODO: put off until tomorrow
else:
  print('Remaining budget:', budget)
```
