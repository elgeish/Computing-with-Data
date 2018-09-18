# Template Functions - Part I

```C++ runnable
#include <iostream>
using namespace std;

class Element {
private:
  int atomic_number;

public:
  Element(int atomic_number) :
    atomic_number(atomic_number) {}
  
  int get_atomic_number() const {
    return atomic_number;
  }

  bool operator<(const Element &x) const {
    return this->atomic_number < x.atomic_number;
  }
};

// note the use of the template keyword below:
template <class T>
// note the use of const T& to avoid copying the return value
const T& get_min(const T &a, const T &b) {
  return a < b ? a : b;
}

int main() {
  // calls the template function, replacing T with int
  cout << get_min<int>(1, 2) << endl;
  // calls the template function, replacing T with double
  cout << get_min<double>(9.1, 2.5) << endl;
  // calls the template function with an inferred type (int)
  cout << get_min(13, 42) << endl;

  Element na = 11;
  Element mg = 12;

  // calls the template function, replacing T with Element
  // note that the replacement type, Element, is inferred
  cout << get_min(na, mg).get_atomic_number() << endl;
  
  return 0;
}
```
