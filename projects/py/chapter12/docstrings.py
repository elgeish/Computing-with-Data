class Point(object):
  "A point in a two-dimensional space"

  def __init__(self, x=0, y=0):
    """
    Initializes the point object to the origin by default,
    or otherwise the initializes to the passed x,y arguments.
    """
    self.x = x
    self.y = y
  def __del__(self):
    "Prints a message when an object is destroyed."
    print("destructing a point object")
  def displayPoint(self):
    "Prints the object by displaying its x and y coordinates."
    print("x: %f, y: %f" % (self.x, self.y))


help(Point)  # shows class doctring
help(Point.displayPoint)  # shows method docstring
