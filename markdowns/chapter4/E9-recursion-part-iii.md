# Recursion - Part III

In the example below, the recursive function contains a stopping condition
(`n == 1`), which stops the recursion when met:

```C++ runnable
#include <iostream>
using namespace std;

int factorial(int n) {
  if (n == 1) {
    return 1;
  }
  
  return n * factorial(n - 1);
}

int main() {
  cout << factorial(3) << endl; // prints 6
  
  return 0;
}
```
