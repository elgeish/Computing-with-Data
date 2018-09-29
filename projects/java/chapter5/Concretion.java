interface Interface {
  int foo();
}

class Concretion implements Interface {
  public int foo() {
    return 1;
  }
}
