#include <iostream>
using namespace std;

struct Point {
  double x;
  double y;
};

int main() {
  // create an array of two points
  Point points[2];
  
  // initialize the array to (0,1) and (2,3)
  points[0].x = 0;
  points[0].y = 1;
  points[1].x = 2;
  points[1].y = 3;
  
  // points is a pointer that refers to the start of the array
  // print points[0] using -> syntax
  cout << points->x << ' ' << points->y << endl; 
  
  // print points[1] using . syntax
  cout << points[1].x << ' ' << points[1].y << endl;
}
