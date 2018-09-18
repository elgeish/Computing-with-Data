# Static Variables and Functions - Part I

```C++ runnable
#include <iostream>
using namespace std;

class Point {
private:
  double x;
  double y;
  static int num_objects;
  
public:
  Point() {
    // increments counter when a new object is created
    ++num_objects;
  }
  
  // even though this method does not modify any members,
  // static member functions cannot be qualified as const
  static int get_num_points() {
    return num_objects;
  }
};

// defines the static field num_objects and initializes it to 0
int Point::num_objects = 0; 

int main() {
  Point p1;
  Point p2;
  Point p3;
  
  cout << "number of point objects: " 
       << Point::get_num_points() << endl;
  
  return 0;
}
```
