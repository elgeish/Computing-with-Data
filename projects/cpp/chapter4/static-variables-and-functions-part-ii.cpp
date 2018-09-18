#include<iostream>
using namespace std;

int count_calls() {
  // initialization occurs only once when program is loaded
  static int counter = 0;
  
  return ++counter; // pre-increments then returns
}

int main() {
  count_calls();
  count_calls(); 
  cout << "number of calls: "<< count_calls() << endl;
  
  return 0;
}
