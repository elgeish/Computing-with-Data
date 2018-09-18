# For-Loops - Part I

```C++ runnable
#include <iostream>
using namespace std;

int main() {
  int an_array[10];
  int i;
  
  // initialize an_array to hold 0, 1, ..., 9
  // 10 iterations are executed, corresponding to
  // i = 0, 1, ..., 9 
  for (i = 0; i < 10; ++i) {
    an_array[i] = i;
  }
  
  // print the values of the array on a single line
  for (i = 0; i < 10; ++i) {
    cout << an_array[i] << ' ';
  }
  cout << endl;
  
  return 0;
}
```
