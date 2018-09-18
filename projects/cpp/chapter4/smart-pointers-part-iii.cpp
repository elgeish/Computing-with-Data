#include <iostream>
#include <memory>
using namespace std;

int main() {
  int n = 10;
  // smart pointer to an array of int variables
  unique_ptr<int[]> array(new int[n]);

  for (int i=0; i<n; ++i) {
    array[i] = i;
  }

  for (int i=0; i<n; ++i) {
    cout << array[i] << ' ';
  }
  cout << endl;

  return 0;
}
