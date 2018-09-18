#include <iostream>
#include <cmath>
using namespace std;

struct Point {
  double x;
  double y;
};

struct Vector {
  Point start;
  Point end;
};

// pass by const reference; the function doesn't modify p1 or p2
Point subtract_points(const Point &p1, const Point &p2) {
  Point delta;
  
  delta.x = p1.x - p2.x;
  delta.y = p1.y - p2.y;
  
  return delta;
}

double length(const Vector &v) {
  Point diff = subtract_points(v.start, v.end);
  
  return sqrt(diff.x * diff.x + diff.y * diff.y);
}

int main() {
  Vector v;
  
  v.start.x = 1;
  v.start.y = 0;
  v.end.x = 2;
  v.end.y = 1;
  
  cout << "length of the vector is: " << length(v) << endl;	
}
