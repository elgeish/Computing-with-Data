# Dynamic Memory Allocation - Part III

```C++
int main() {
  int n = 2;
  // allocates memory for an array of n objects of type point
  Point *pp = new Point[n];

  delete[] pp; // frees up a dynamically-allocated array
  
  return 0;
}
```
