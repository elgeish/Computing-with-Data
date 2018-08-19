# Rounding

Rounding occurs when a real number `x` cannot be precisely matched
to a fixed- or a floating- point representation. The result of rounding
is typically either the nearest representation of `x` or a truncated version
of `x` obtained by dividing and dropping the remainder. Here's an example in R:

```R runnable
# Round 0.333.. to a nearby floating-point
print(1 / 3, digits = 22) # print 22 digits of fp(1/3)
## 0.3333333333333333148296
```
