# Hashable Objects

In addition to the requirement that each key may appear at most once, keys are
required to be hashable:

```python runnable
print(hash("abc"))  
print(hash((1, 2, 3)))
```
