# Duck Typing

The interpreter tries to execute the code and if it cannot, a runtime error will
occur:

```python runnable
class Duck:
  def quack(self):
    print("Quack")
  def walk(self):
    print("Shuffle")

class Fox:
  def quack(self):
    print("Quackkkkk")
  def walk(self):
    print("Shuffffle")
  def kill(self):
    print("Yum!")

def foo(x):
  x.quack()
  x.walk()

donald = Duck()
swiper = Fox()
foo(donald)
foo(swiper)
```
