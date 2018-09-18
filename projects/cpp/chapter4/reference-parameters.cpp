#include <iostream>
using namespace std;

// The function modifies variables in the calling environment by
// receiving parameters of type reference, and then modifying 
// the variables that are referred to.
void set(int &a, int &b, int &c) {
  a = 1;
  b = 2;
  c = 3;
}

int main() {
  int a = 0;
  int b = 0;
  int c = 0;
  
  // print initial values
  cout << a << ' ' << b << ' ' << c << endl;
  // modify the local a, b, c by passing references to them.
  set(a, b, c);
  // print values of a, b, c
  cout << a << ' ' << b << ' ' << c << endl;
  
  return 0;
}
