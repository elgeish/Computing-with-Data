# If-Else Clauses

```C++
// Example 1
int a;
int abs_a;

cin >> a; // read a from terminal
// replace a by its absolute value and store it in abs_a
if (a < 0) {
  abs_a = -a;  // if a is negative, use -a
} else {
  abs_a = a;  // if a is non-negative, use a
}

// Example 2
int a;
int abs_a;

cin >> a;
abs_a = a;
// negate abs_a if it is negative
if (abs_a < 0) {
  abs_a = -abs_a;
}

// Example 3
int a;

cin >> a;

int abs_a = a < 0 ? -a : a;
```
