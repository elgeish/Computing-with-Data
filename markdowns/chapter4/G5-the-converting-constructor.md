# The Converting Constructor

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

int main() {
  Element na(11);
  Element mg = 12; // alternative form
  
  cout << mg.get_atomic_number() << endl; // prints 12

  return 0;
}
```
