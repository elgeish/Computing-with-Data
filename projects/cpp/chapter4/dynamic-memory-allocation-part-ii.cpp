int main() {
  Point *pp1 = new Point; // the default constructor
  Point *pp2 = new Point(1, 2); // an overloaded constructor

  delete pp1;
  delete pp2;
  
  return 0;
}
