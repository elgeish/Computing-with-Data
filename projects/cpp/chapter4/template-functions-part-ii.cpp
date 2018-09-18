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

template <class T, class S>
bool precedes(const T &a, const S &b) {
  return a < b;
}

int main() {
  // instructs cout to print true and false instead of 1 and 0
  cout.setf(ios::boolalpha);
  
  cout << precedes<int, double>(1, 42) << endl;
  cout << precedes(9.1, 3) << endl;
  cout << precedes(1.5f, 1.3) << endl;

  Element na = 11;
  Element mg = 12;

  cout << precedes(na, mg) << endl;
  
  return 0;
}
