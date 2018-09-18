#include <iostream>
using namespace std;

struct Point {
  double x;
  double y;
};

// pass by reference - the function is modifying p
void scale_point(Point &p, double scaling_factor) {
  p.x = p.x * scaling_factor; 
  p.y = p.y * scaling_factor; 
}

// pass by const reference - the function is not modifying p
void print_point(const string &prefix, const Point &p) {
  cout << prefix << '(' << p.x << ',' << p.y << ')' << endl; 
}

// pass by const reference - the function is not modifying p1, p2
Point subtract_points(const Point &p1, const Point &p2) {
  Point delta;
  
  delta.x = p1.x - p2.x;
  delta.y = p1.y - p2.y;
  
  return delta;
}

int main() {
  Point p1;
  Point p2;
  
  p1.x = 1; 
  p1.y = 2;
  p2.x = 3;
  p2.y = 3;
  
  print_point("first point: ", p1);
  print_point("second point: ", p2);
  print_point("delta: ", subtract_points(p1, p2));
  
  // scale second point by a factor of 2
  cout << endl << "scaling the 2nd point to 2x" << endl;
  scale_point(p2, 2);
  
  print_point("first point: ", p1);
  print_point("second point: ", p2);
  print_point("delta:", subtract_points(p1, p2));
  
  return 0;
}
