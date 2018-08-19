# Example: a point in a two-dimensional coordinate space
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __del__(self):
    print ("destructing a Point object")

p1 = Point(3, 4)
p2 = Point(1, 2)
print("p1.x = {0.x}, p1.y = {0.y}".format(p1))
print("p2.x = {0.x}, p2.y = {0.y}".format(p2))

# Example: a class field (num_points) and instance fields (x and y)
class Point:
  '''Represents a point in a two-dimensional coordinate space.'''
  num_points = 0

  def __init__(self, x, y):
    Point.num_points += 1 
    self.x = x
    self.y = y

  def __del__(self):
    Point.num_points -= 1
    print("destructing a Point object")
    print("{} Point objects left".format(Point.num_points))


print(Point.__doc__)
p1 = Point(3, 4)
p2 = Point(1, 2)
print("p1.x = {0.x}, p1.y = {0.y}".format(p1))
print("p2.x = {0.x}, p2.y = {0.y}".format(p2))
print("number of objects:", Point.num_points)
