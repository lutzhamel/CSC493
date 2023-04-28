fn quicksort(arr: &mut [i32]) {
   if arr.len() <= 1 {
       return;
   }

   let pivot = arr[0];
   let mut less = Vec::new();
   let mut greater = Vec::new();

   for &x in &arr[1..] {
       if x <= pivot {
           less.push(x);
       } else {
           greater.push(x);
       }
   }

   quicksort(&mut less);
   quicksort(&mut greater);

   let mut i = 0;

   for &x in &less {
       arr[i] = x;
       i += 1;
   }

   arr[i] = pivot;
   i += 1;

   for &x in &greater {
       arr[i] = x;
       i += 1;
   }
}

fn main() {
   let mut unsorted_arr = vec![5, 3, 8, 4, 2, 7, 1, 10];
   let sorted_arr = vec![1, 2, 3, 4, 5, 7, 8, 10];

   quicksort(&mut unsorted_arr);
   assert_eq!(unsorted_arr, sorted_arr);
}
