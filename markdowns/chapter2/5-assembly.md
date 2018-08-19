# Use of Assembly Language in High-Level Languages

This example simply executes the RDTSC assembly instruction, which reads
the CPU's timestamp counter, then stores the higher 32 bits into the `EDX`
register and the lower ones into the `EAX` register. The value of `EAX` is then
assigned to the `timeStampCounter` variable in C++ and printed out:

```C++ runnable
// { autofold
#include <iostream>

using namespace std;
// }

int main() {
  uint timeStampCounter = 0;
  asm("rdtsc": "=a" (timeStampCounter));
  std::cout << timeStampCounter << std::endl;
  return 0;
}
```
