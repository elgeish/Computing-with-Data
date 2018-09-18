#include <vector>
#include <iostream>
using namespace std;

int main() {
  vector<int> v;

  for (int i = 0; i < 10; ++i) { // store 1..10
    v.push_back(i);
  }

  for (const auto &x : v) { // print all elements
    cout << x << ' ';
  }
  cout << endl;
  
  return 0;
}
