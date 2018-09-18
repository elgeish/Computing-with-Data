// Example 1
int *pa;
int *pb;  // pa and pb are pointers to int variables
float *fx;
float *fy;  // fx and fy are pointers to float variables

// Example 2
int a = 2;
int *b; // uninitialized pointer - may contain unexpected address
int *c = &a; // address of variable a is assigned to pointer c
int d = *c; // value at address c is assigned to d (d = 2)
// define a new pointer e that points to the same memory as c
int *e = c; 
float f = 3.0f;
float *fp = &f;  // ok
int *a = &f;  // problem: a is of type int* but points to float

// Example 3
int a = 2;
int *b = &a; // pointer b points to a
int **c = &b; // double pointer c points to b
// c now holds the address of b, which holds the address of a
int *d = *c; // contents of b (address of a) is assigned to d
int e = *(*c); // contents of a (2) is assigned to e
