#include <iostream>
using namespace std;

class Element {
private:
  int atomic_number;

public:
  // note the use of the explicit keyword below
  explicit Element(int an_atomic_number) :
    atomic_number(an_atomic_number) {}
  
  int get_atomic_number() const {
    return atomic_number;
  }
};

int main() {
  Element na(11);
  Element mg = 12; // error
  
  cout << na.get_atomic_number() << endl; // prints 11

  return 0;
}
