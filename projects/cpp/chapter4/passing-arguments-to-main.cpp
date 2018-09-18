// running the program ./my_prog from the Linux terminal
// calls the appropriate main function with parameters a, 1, b, 2
// ./my_prog a 1 b 2

#include <iostream>
using namespace std;

int main(int argc, char **argv) {
  cout << "argc is: " << argc << endl;
  
  for (int i = 0; i < argc; ++i) {
    cout << "argv[" << i << "] is: " << argv[i] << endl;
  }
  
  return 0;
}
