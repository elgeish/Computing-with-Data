# Preprocessor and Namespaces - Part II

```C++
// Example 1
// include a header file written by the programmer
#include "my_header_file.h"

// call my_function, which is a function defined in
// the header file my_header_file.h
int main() {
  my_function();
  
  return 0;
}

// Example 2
#define WIDTH 80

int page_width = WIDTH;
int two_page_width = 2 * WIDTH;

// This code below is similar but harder to comprehend 
// and maintain
int three_page_width = 3 * 80;
int four_page_width = 4 * 80;

// Example 3
#include <iostream>
#define arraysize(array) (sizeof(array) / sizeof(*array))

int main() {
  int a[10];
  
  std::cout << arraysize(a); // prints the size of the array (10) 

  return 0;
}

// Example 4
#include "my_header_file1.h"
#include "my_header_file2.h"
// constants or functions in my_header_file3 are defined twice

// Example 5
#ifndef _MY_HEADER_3_GUARD
#define _MY_HEADER_3_GUARD

// copy original contents of my_header_file3.h here

#endif

// Example 6
// option 1: Prefix cout by the namespace name and ::
std::cout << 3;  // print 3 (cout is defined std namespace)

// option 2: Using namespace std allows dropping the std:: prefix
using namespace std;
cout << 3;
```
