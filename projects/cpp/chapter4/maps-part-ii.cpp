#include <map>
#include <string>
#include <iostream>
using namespace std;

int main() {
  map<string,int> names;

  names["John"] = 3;
  names["Jane"] = 6;

  cout << "names[\"John\"]: " << names["John"] << endl;
  cout << "names[\"Jane\"]: " << names["Jane"] << endl;

  return 0;
}
