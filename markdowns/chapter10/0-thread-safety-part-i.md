# Thread Safety - Part I

In this chapter, we will be mainly using Java to explore parallel computing
concepts that, given they're supported, can be easily translated into other
programming languages.

__Note:__ Code examples in this chapter may sacrifice best OOP practices,
like encapsulation, for demonstration purposes and brevity.

```python runnable
# Example 1 - single-threaded logic
def do_work():
  print('Hello, world!')

do_work()

# Example 2 - multi-threaded logic
from threading import Thread

for t in (Thread(target=do_work) for _ in range(10)):
  t.start()
```
