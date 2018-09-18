class Point:
  '''Represents a point in a 2-D coordinate space.'''
  num_points = 0

  def __init__(self, x, y):
    Point.num_points += 1
    self.x = x
    self.y = y

  def __del__(self):
    Point.num_points -= 1
    print("destructing a Point object")
    print("{} points left".format(Point.num_points))


class NamedPoint(Point):
  '''Represents a named point in a 2-D coordinate space.'''
  num_points = 0

  def __init__(self, x, y, name):
    # call superclass constructor
    super().__init__(x, y)
    NamedPoint.num_points += 1
    self.name = name

  def __del__(self):
    super().__del__()
    NamedPoint.num_points -= 1
    print("destructing a NamedPoint object")
    print("{} named points left".format(NamedPoint.num_points))


np = NamedPoint(0, 0, "origin point")
print("number of named points:", NamedPoint.num_points)
print("x = {0.x}, y = {0.y}, name = {0.name}".format(np))
