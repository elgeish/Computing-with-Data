class Parent { // superclass
  private int a;
  
  public Parent(final int a) {
    this.a = a;
  }
}

class Child extends Parent { // subclass
  private int b;
  
  public Child(final int a, final int b) {
    super(a); // call to constructor of class Parent
    this.b = b;
  }
}

public class InheritanceExample {
  public static void main(final String[] args) {
    // Define an object of class Parent
    final Parent a = new Parent(3);
    // Define an object of class Child
    final Child b = new Child(1, 3);
    // Polymorphism: a Parent object refers to a Child object
    final Parent c = b;
    final Child d;
    
    if (c instanceof Child) { // check if c points to class Child
      // Cast the object referred to by c to type Child
      d = (Child) c;
    }
  }
}
