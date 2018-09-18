# Maps - Part I

```C++ runnable
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main() {
  multimap<string,int> names;

  // note the use of curly braces to create a pair
  names.insert({"John", 3});
  names.insert({"Peter", 2});
  names.insert({"Jane", 6});
  names.insert({"Jane", 2});

  for (const auto &x : names) {
    cout << x.first << ": " << x.second << endl;
  }
  
  return 0;
}
```
