# Overflow

Overflow occurs when a number has a big absolute value that's outside
the range of possible binary representations. In the case of integers, this
occurs when the number of bits in the representation is too small to represent
the corresponding number. When overflow occurs, the number is replaced by either
the closest binary representation or is marked as an overflow and considered
unavailable. Here's an example in R:

```R runnable
print(10 ^ 100)   # no overflow
print(10 ^ 500)   # overflow, marked by Inf value 
## 1e+100
## Inf
```
