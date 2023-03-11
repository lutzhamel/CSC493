import java.util.*;
import java.util.Vector;

class Shape {
    static public void draw() { System.out.println("Drawing a shape.");  }
}

class Circle extends Shape {
   private String name;
   Circle(String name) { this.name = name; }
   public void draw() { System.out.println("Drawing a circle "+this.name);  }
}

class Square extends Shape {
   private String name;
   Square(String name) { this.name = name; }
   public void draw() { System.out.println("Drawing a square "+this.name); }
}

class Main {
    public static void main(String[] args) {
      Vector<Shape> v = new Vector<Shape>(3);
      v.add(new Circle("Circle1"));
      v.add(new Square("Square1"));
      v.add(new Circle("Circle2"));
      for (int i = 0; i < v.size(); i++) {
         v.get(i).draw();
      }
    }
}


