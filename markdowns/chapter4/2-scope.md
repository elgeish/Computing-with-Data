# Scope

```C++
// Example 1
{
  int a = 2;
  a = a + 1; // ok, a is recognized
  {
    int b = a; // ok, a is still in scope
  }
  a = b; // error, b is out of scope and is undefined
}
a = a + 1; // error, a is out of scope

// Example 2
int a = 2;

{
  int a = 3;  // inner a (a=3) masks the outer a (a=2)
  int b = a;  // b is assigned the value 3
}

// inner a is out of scope and outer a is no longer masked
int c = a; // c is assigned the value of the outer a (a=2) 
int d = b; // error: b is no longer in scope

// Example 3
int a = 42; // global variable

int main() {
  int a = 13; // local variable
  int b = a + 1; // 14
  int c = ::a + 1; // 43

  return 0;
}
```
