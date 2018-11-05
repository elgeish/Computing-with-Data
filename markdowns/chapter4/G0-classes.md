# Classes

```C++ runnable
#include <iostream>
using namespace std;

class Point {
private:
  // fields are accessible only to methods belonging to point
  double x;
  double y;

public:
  void set_x(double a_x) {
    this->x = a_x; // set the member x to the value a_x
  }
  
  void set_y(double a_y) {
   this->y = a_y;
  }
  
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
  
  // negate x and y (method implemented outside class body)
  void reflect();
};

void Point::reflect() {
  x = -x; // alternatively, this->x = - this->x
  y = -y; // alternatively, this->y = - this->y
}

int main() {
  Point p;
  
  p.set_x(1);
  p.set_y(2);
  cout << '(' << p.get_x() << ',' << p.get_y() << ')' << endl;
  
  p.reflect();
  cout << '(' << p.get_x() << ',' << p.get_y() << ')' << endl;
  
  return 0;
}
```
