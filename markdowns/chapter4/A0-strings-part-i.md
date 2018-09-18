# Strings - Part I

```C++ runnable
#include <string>
using namespace std;

int main() {
  string s1;  // define an empty string
  string s2 = "hello world"; // define a string with content
  int sz = s2.size(); // assign size of string s2 to variable
  char a = s2[1];  // access second character of s2 ('e') 
  string s3 = s2 + s2; // concatenate s2 with itself
  bool b = s2.empty();  // true if s2 is an empty string
  
  return 0;
}
```
