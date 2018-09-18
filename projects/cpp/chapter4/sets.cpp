#include <set>
#include <string>
#include <iostream>
using namespace std;

int main() {
  set<string> s;

  s.insert({"one"});
  s.insert({"two"});
  s.insert({"three"});
  s.insert({"one"});

  for (const auto &x : s) {
    cout << x << ' ';
  }
  cout << endl;

  return 0;
}
