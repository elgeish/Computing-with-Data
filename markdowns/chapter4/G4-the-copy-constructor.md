# The Copy Constructor

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

  // copy constructor
  Point(const Point& p) {
    x = p.x;
    y = p.y;
  }
};

int main() {
  Point p1(1, 2); // new object using a constructor
  Point p2(p1);  // new object using the copy constructor
  
  return 0;
}
```
