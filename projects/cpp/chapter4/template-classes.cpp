#include <iostream>
using namespace std;

template<class T>
class Point {
private:
  T x;
  T y;

public:
  void set_x(const T &x) {
    this->x = x;
  }

  void set_y(const T &y) {
    this->y = y;
  }

  T get_x() const {
    return x;
  }

  T get_y() const {
    return y;  
  }

  void reflect() {
    x = -x;
    y = -y; 
  }
};

int main() {
  Point<int> p;

  p.set_x(1);
  p.set_y(2);
  cout << '(' << p.get_x() << ',' << p.get_y() << ')' << endl;
  
  p.reflect();
  cout << '(' << p.get_x() << ',' << p.get_y() << ')' << endl;
  
  return 0;
}
