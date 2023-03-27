fn f(x: i32, y: i32) -> String {
   match (x, y) {
       (x, y) if x > y => "GT".to_string(),
       (x, y) if x < y => "LT".to_string(),
       _ => panic!("not a valid tuple"),
   }
}

