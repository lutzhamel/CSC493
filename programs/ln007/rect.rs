struct Rectangle {
    xdim: f32,
    ydim: f32,
}

impl Rectangle {
    fn area(&self) -> f32 {
        self.xdim * self.ydim
    }
}

fn main() {
    let r = Rectangle { xdim: 2.0, ydim: 4.0 };
    let a = r.area();
    assert!(a == 8.0);
}
