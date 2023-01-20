struct Person {
   name: String,
   age: u8,
   profession: String,
}

fn main() {
   let joe = Person {
       name: "Joe".to_string(),
       age: 32,
       profession: "Cook".to_string()
   };

   let Person { name:n, age:a, profession:p } = joe;

   assert!(n == "Joe" && a == 32 && p == "Cook");
}


