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

  // mark the non-member function overloading << as a friend
  friend ostream& operator<<(ostream &os, const Point &p);
};

ostream& operator<<(ostream &os, const Point &p) {
  // access private fields since << is a friend of Point
  os << '(' << p.x << ',' << p.y << ')';
  
  return os;
}

int main() {
  Point p(1,2);

  cout << p << endl;
  
  return 0;
}
