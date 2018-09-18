# For-Loops - Part III

```C++ runnable
#include <iostream>
using namespace std;

int main() {
  int i;
  int j;
  const int N = 10;
  int a_table[N][N];  // NxN 2D array
  
  // initialize table to hold the values 0, 1, ..., 99
  for (i = 0; i < N; ++i) {
    for (j = 0; j < N; ++j) {
      a_table[i][j] = i * N + j;
    }
  }
  
  // print the table
  for (i = 0; i < N; ++i) {
    for (j = 0; j < N; ++j) {
      cout << a_table[i][j] << ' ';
    }
    cout << endl;
  }
  
  return 0;
}
```
