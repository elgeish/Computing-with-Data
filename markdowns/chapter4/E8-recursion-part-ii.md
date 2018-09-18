# Recursion - Part II

In fact, it's possible for a function to call itself:

```C++ runnable
// recurse() will keep calling itself, going into deeper
// and deeper recursive calls 
// (until the program crashes due to call stack overflow)

void recurse() {
  recurse();
}

int main() {
  recurse();
  
  return 0; // this statement will never be reached
}
```
