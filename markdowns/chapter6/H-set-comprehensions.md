# Set Comprehensions

Set comprehensions work almost exactly the same way as list comprehensions,
except that the result is a set (where repeated elements are not allowed)
and it's expressed using curly braces:

```python runnable
champions = [
  (2014, 'San Antonio Spurs'),
  (2015, 'Golden State Warriors'),
  (2016, 'The Cleveland Cavaliers'),
  (2017, 'Golden State Warriors'),
  (2018, 'Golden State Warriors'),
]
for team in {c[1] for c in champions}: # unordered
    print(team)
```
