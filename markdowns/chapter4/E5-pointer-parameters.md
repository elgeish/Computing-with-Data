# Pointer Parameters

```C++ runnable
#include <iostream>
using namespace std;

// The function below accepts an address and 
// an integer n and communicates back by writing
// the first n non-negative even integers in 
// the specified address
void write_seq(int *a, int n) {
  for (int i = 0; i < n; ++i) {
    a[i] = i * 2;
  }
}

// The function below accepts an address and 
// an integer n and negates the n integers
// that are stored in the specified address
void negate_seq(int *a, int n) {
  for (int i = 0; i < n; ++i) {
    a[i] = -a[i];
  }
}

int main() {
  int a[10] = {};
  
  write_seq(a, 10);  // assign even numbers to the array 
  negate_seq(a, 10);  // negate values of a
  
  for (const auto &element : a) {
    cout << element << " ";
  }
  cout << endl;
  
  return 0;
}
```
