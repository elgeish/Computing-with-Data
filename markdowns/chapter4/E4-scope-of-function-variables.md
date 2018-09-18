# Scope of Function Variables

```C++ runnable
#include <iostream>
#include <string>
using namespace std;

// return a * b
int multiply_two(int a, int b) {
  int c = a * b;
  
  return c;
}

int main() {
  cout << multiply_two(2, 3) << endl; // prints 6
  
  int b = 4;
  int c = 5;
  
  cout << multiply_two(b, c) << endl; // prints 20
  cout << c << endl;  // print value of local c (5)
  
  return 0;
}
```
