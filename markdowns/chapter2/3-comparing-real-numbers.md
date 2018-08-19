# Comparing Real Numbers

Comparing whether or not two real numbers are identical is problematic
due to rounding errors. See the below C++ example for an illustration:

```C++ runnable
// { autofold
#include <iostream>
#include <math.h>

using namespace std;
// }

int main() {
  cout << (sqrt(3) * sqrt(3) - 3) << endl
       << (sqrt(3) * sqrt(3) == 3) << endl
       << (fabs(sqrt(3) * sqrt(3) - 3) < 0.0000001) << endl;
}
```
