# Smart Pointers - Part I

```C++ runnable
#include<memory>
using namespace std;

int main() {
  // creates smart pointers to double variables,
  // each holds a value of 4.2
  shared_ptr<double> pd1 = make_shared<double>(4.2);  
  shared_ptr<double> pd2(new double(4.2)); // alternatively
  
  // pd2 is reassigned to a new memory location,
  // older memory content is no longer pointed to
  // and is therefore freed up automatically
  pd2 = make_shared<double>(8.4);

  // several shared_ptr objects may point to the same memory
  shared_ptr<double> pd3 = pd2;
  
  return 0;
}
```
