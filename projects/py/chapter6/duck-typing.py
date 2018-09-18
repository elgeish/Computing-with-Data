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
