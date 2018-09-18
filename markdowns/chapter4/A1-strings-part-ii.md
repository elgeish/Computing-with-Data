# Strings - Part II

```C++ runnable
#include <string>
using namespace std;

int main() {
  int a = 123;
  string s = to_string(a);  // assign "123" to s
  int i = stoi(s);  // assign integer 123 to i
  double d = stod(s); // assign floating point 123.0 to d
  
  return 0;
}
```
