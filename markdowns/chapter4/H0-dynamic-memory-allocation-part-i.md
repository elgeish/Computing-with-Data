# Dynamic Memory Allocation - Part I

```C++ runnable
int main() {
  // pd points to a dynamically allocated double variable
  double *pd = new double;
  
  // free the allocated memory
  delete pd;

  return 0;
}
```
