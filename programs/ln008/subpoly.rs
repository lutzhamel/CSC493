use std::vec::Vec;

trait Shape { fn draw(&self); }

struct Circle { name: String }
impl Circle { fn new(name: &str) -> Circle { Circle { name: name.to_string() } } }
impl Shape for Circle { fn draw(&self) {println!("Drawing a circle {}", self.name);} }

struct Square { name: String }
impl Square { fn new(name: &str) -> Square { Square { name: name.to_string() } } }
impl Shape for Square { fn draw(&self) { println!("Drawing a square {}", self.name); } }

fn main() {
    let mut v: Vec<Box<dyn Shape>> = Vec::new();
    v.push(Box::new(Circle::new("Circle1")));
    v.push(Box::new(Square::new("Square1")));
    v.push(Box::new(Circle::new("Circle2")));
    for shape in &v {
        shape.draw();
    }
}
