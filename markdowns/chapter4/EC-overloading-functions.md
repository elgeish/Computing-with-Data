# Overloading Functions

```C++ runnable
#include <iostream>
using namespace std;

void print_argument(int a) {
  cout << "One int argument passed: " << a << endl;
}

void print_argument(double a) {
  cout << "One double argument passed: " << a << endl;
}

void print_argument() {
  cout << "No argument passed" << endl;
}

int main() {
  print_argument(); // matches print_argument()
  print_argument(1); // matches print_argument(int)
  print_argument(1.2); // matches print_argument(double)
  
  return 0;
}
```
