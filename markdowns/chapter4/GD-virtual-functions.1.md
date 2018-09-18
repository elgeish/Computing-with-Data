# Virtual Functions

```C++ runnable
#include <iostream>
using namespace std;

class Point {
private:
  // fields are accessible only to methods belonging to point
  double x;
  double y;

public:
  // constructor accepting two arguments, called by a 
  // statement such as: Point p(1, 2);
  Point(double a_x, double a_y) : x(a_x), y(a_y) {}

  // Point::print method defined in base class
  // note the use of the virtual keyword below
  virtual void print() {  
    cout << '(' << x << ',' << y << ')' << endl;
  }
};

class NamedPoint : public Point {
private:
  string name;

public:  
  // constructor calls point constructor then initializes name
  NamedPoint(double x, double y, string name) :
    Point(x, y), name(name) {}
  
  // NamedPoint::print method defined in derived class
  // note the use of the virtual keyword below
  virtual void print() {  
    cout << name << ' ';
    Point::print();
  }
};

int main() {
  NamedPoint p(0, 0, "origin");
  Point &refP = p;
  Point *pp = &p;
  
  refP.print(); // dynamic binding calls NamedPoint::print()
  pp->print(); // ditto
  
  return 0;
}
```
