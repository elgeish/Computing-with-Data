#include <iostream>
#include <string>
using namespace std;

struct Person {
    string name;
    double age;
};

void by_address_of_const(const Person *p) {
    Person x;

    p = &x;
    cout << "modified copy inside function: " << p << endl;
}

int main() {
  Person person;
  Person *pointer = &person;
  
  cout << "before function call: " << pointer << endl;
  by_address_of_const(pointer);
  cout << "after function call: " << pointer << endl;
  
  return 0;
}
