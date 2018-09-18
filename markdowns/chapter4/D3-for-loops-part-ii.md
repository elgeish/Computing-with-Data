# For-Loops - Part II

```C++ runnable
#include <iostream>
using namespace std;

int main() {
  int an_array[10];
  int i = 0;
  
  for (auto &element : an_array) {
    element = i;
    ++i;
  }
  
  for (auto &element : an_array) {
    cout << element << ' ';
  }
  cout << endl;
  
  return 0;
}
```
