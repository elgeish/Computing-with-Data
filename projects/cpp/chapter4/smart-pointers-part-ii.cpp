#include <memory>
using namespace std;

unique_ptr<int> create_unique_pointer() {
  return unique_ptr<int>(new int(4));
}

int main() {
  unique_ptr<int> pi1(new int(3));
  // error: two unique_ptr pointers pointing to the same memory
  unique_ptr<int> pi2 = pi1; 
  // ok: new unique_ptr takes over as old unique_ptr is destroyed
  unique_ptr<int> pi3 = create_unique_pointer();
  
  return 0;
}
