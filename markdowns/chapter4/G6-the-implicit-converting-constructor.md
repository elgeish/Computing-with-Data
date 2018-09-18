# The Implicit Converting Constructor

```C++ runnable
#include <iostream>
using namespace std;

class Element {
private:
  int atomic_number;

public:
  Element(int an_atomic_number) :
    atomic_number(an_atomic_number) {}
  
  int get_atomic_number() const {
    return atomic_number;
  }
};

// calling this function with an int parameter causes
// the converting constructor to be called
void print_element(Element x) {
  cout << x.get_atomic_number() << endl;
}

int main() {
  print_element(12); // prints 12
  
  return 0;
}
```
