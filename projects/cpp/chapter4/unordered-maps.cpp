#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

int main() {
  unordered_multimap<string,int> names;

  names.insert({"John", 3});
  names.insert({"Peter", 2});
  names.insert({"Jane", 6});
  names.insert({"Jane", 2});

  for (const auto &x : names) {
    cout << x.first << ": " << x.second << endl;
  }

  return 0;
}
