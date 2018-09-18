# Recursion - Part I

So far, we have seen examples of `main` calling other functions.
It's possible for any function to call another; for example:

```C++ runnable
#include<iostream>
using namespace std;

void bar() {
  cout << "bar" << endl;
}

void foo() {
  cout << "foo" << ' ';
  bar();
}

int main() {
  // enter foo and print "foo", then enter bar and print "bar"
  foo();
  
  return 0;
}
```
