// Example 1
int i;
double d = 58.3;

i = (int) d; // converts 58.3 to int

// Example 2
int a = 3.2;  // 3.2 is converted to the integer 3
int b;

b = 3.2;  // same casting as above
b = 3.0 / 2.0; // 1.5 is converted to the integer 1 

// Example 3
int a = 1;
int b = 2;
float f = 2.0f; // without the suffix f, 2.0 is a double

// Below, in the division a/f, the integer a is converted
// to a float resulting in a division of two floats: 
// 1.0f/2.0f (which equals 0.5)
float g = a / f;  // g equals 0.5

// Below, there is no type conversion for the division a/b.
// The division of an integer 1 by another integer 2 gives 
// the integer 0, which is then converted to a float 0.0
// that is assigned to h
float h = a / b;  // h equals 0.0
