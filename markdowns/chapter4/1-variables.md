# Variables

```C++
// Example 1
int age; // age is a variable of type int (integer)
// two double variables
double height;
double weight;

// Example 2
int age = 32; // integer variable holding 32
double height; // unassigned variable
float pi = 3.14; // new float variable
float pi_squared = pi * pi; // new float variable

height = (5 * 30.48) + (10 * 2.54); // assigs a value to height

// Example 3
int a = 2;
const int b = 3; // more readable
int const c = 5; // alternative form

a = 6;  // ok
b = 6;  // error (b cannot be modified)

// Example 4
double height = 58.0;
double weight = 155.2;
auto bmi = weight / (height * height); // inferred type (double)
```
