# Arrays

```C++
// Example 1
int a[10]; // define an array of 10 integers

a[0] = 1;  // assign 1 to the first element
a[3] = 2;  // assign 2 to the fourth element

int b = a[3]; // assign to b the contents of the fourth element

// Example 2
// using an array as a pointer
int a[10];  

*a = 3; // assign a value of 3 to the first element 
*(a + 2) = 4; // assign a value of 4 to the third element

// using a pointer as an array
int *pA = a + 1; // pA points to the second element of a

pA[1] = 5;  // assign a value of 5 to the third element of a

// Example 3
// define an array of size 10 containing the integers 0, 1,..., 9
int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
// array size may be omitted in this case
int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
// define an array of size 10 initialized to default
// values (0 for int)
int a[10] = {};
// define an array of size 10 initialized to 1, 0,..., 0
int a[10] = {1};

// Example 4
const int N = 3;
double a[N];  // ok
int m = 3;
double b[m];  // error

// Example 5
int a[10] = {};
a[13] = 3; // dangerous bug - possible erratic behavior

// Example 6
// a is 3 by 4 table of integers initialized to default values
// (0 in the case of int variables)
int a[3][4] = {};
a[0][0] = 2; // assign 2 to first row, first column element
a[0][1] = 3; // assign 3 to first row, second column element
a[1][2] = 4; // assign 4 to second row, third column element
// b is 3 by 4 by 5
int b[3][4][5] = {};
b[0][0][0] = 2; // first row, first column, first layer element
b[0][1][2] = 2; // first row, second column, third layer element
```
