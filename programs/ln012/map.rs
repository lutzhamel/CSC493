use std::vec::Vec;

fn main() {
    let a : Vec<i32> = vec![1,2,3,4,5,6,7,8,9,10]
        .iter()
        .map(|x| x % 2)
        .map(|x| if x == 0 { -1 } else { 1 })
        .collect();

    assert_eq!(a, vec![1, -1, 1, -1, 1, -1, 1, -1, 1, -1]);
}

