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
