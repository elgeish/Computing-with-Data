#include <iostream>
using namespace std;

class Point {
private:
  // fields are accessible only to methods belonging to point
  double x;
  double y;

public:
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

  // overload addition operator (+)
  Point operator+(const Point &p) const {
    Point result;
    
    result.x = this->x + p.x;
    result.y = this->y + p.y;
    
    return result;
  }
};

ostream& operator<<(ostream& os, const Point &p) {
  os << '(' << p.get_x() << ',' << p.get_y() << ')';
  
  return os; // to support operator chaining
}

int main() {
  Point p1(1,2);
  Point p2(2,3);
  Point p3 = p1 + p2;  // calls the overloaded + operator
  
  // calls the overloaded << operator thrice for points
  // and thrice for spaces and end-of-line delimiters
  cout << p1 << ' ' << p2 << ' ' << p3 << endl;
  
  return 0;
}
