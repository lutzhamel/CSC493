fn main() {
   let value: i32 = (1..10).reduce(|acc, e| acc + e).unwrap();
   assert_eq!(value, 45);
 }

 