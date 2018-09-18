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

  void print() {  // Point::print method defined in base class
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
  void print() {
    cout << name << ' ';
    Point::print();
  }
};

int main() {
  Point p(2,3);
  NamedPoint np(1, 2, "first point");
  
  p.print();  // Point::print is called
  np.print();  // NamedPoint::print is called
  
  return 0;	
}
