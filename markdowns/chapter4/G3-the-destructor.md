# The Destructor

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

  ~Point() {} // empty destructor

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
};

int main() {
  Point p(2,-2);  // constructor with two argument is called
  
  cout << '(' << p.get_x() << ',' << p.get_y() << ')' << endl;
  
  return 0;
}
```
