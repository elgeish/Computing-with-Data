# Inheritance

```C++ runnable
#include <iostream>
using namespace std;

class Point {
private:
  // fields are accessible only to methods belonging to point
  double x;
  double y;

public:
  // empty constructor, called by the statement: Point p;
  Point() {}

  // constructor accepting two arguments, called by a 
  // statement such as: Point p(1, 2);
  Point(double a_x, double a_y) : x(a_x), y(a_y) {}

  // get value of x, const implies that the method does not 
  // modify the object
  double get_x() const {
    return x;
  }
  
  // get value of y, const implies that the method does not 
  // modify the object
  double get_y() const {
    return y;
  }

  void set_x(double a_x) {
    this->x = a_x; // set the member x to the value a_x
  }
  
  void set_y(double a_y) {
   this->y = a_y;
  }
};

class NamedPoint : public Point {
private:
  string name;

public:
  // empty constructor calls point constructor
  NamedPoint() : Point() {}
  
  // constructor calls point constructor then initializes name
  NamedPoint(double x, double y, string name) :
    Point(x, y), name(name) {}
  
  string get_name() {
    return name;
  }
  
  void set_name(string a_name) {
    this->name = a_name;
  }
};

int main() {
  NamedPoint p(0, 0, "origin");
  
  p.set_name("FIRST POINT");
  p.set_x(2);  // calls a base class method
  cout << p.get_name() << ": " << '(' << p.get_x() << ',' <<
    p.get_y() << ')' << endl;

  
  return 0;
}
```
