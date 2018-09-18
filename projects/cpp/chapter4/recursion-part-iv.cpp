#include <iostream>
using namespace std;

int factorial(int n) {
  cout << "entering factorial(" << n << ')' << endl;
  
  if (n == 1) {
    cout << "leaving factorial(1) with return value 1" << endl;
    
    return 1;
  }
  
  int result = n * factorial(n - 1);
  cout << "leaving factorial(" << n <<
    ") with return value " << result << endl;
  
  return result;
}

int main() {
  cout << factorial(3) << endl;
  
  return 0;
}
