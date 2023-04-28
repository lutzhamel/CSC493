# declarative version of quicksort
def quicksort(arr):
    match arr:
        case []:
            return []
        case [a]:
            return [a]
        case (pivot,*rest):
            less = [x for x in rest if x <= pivot]
            greater = [x for x in rest if x > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)

unsorted_arr = [5, 3, 8, 4, 2, 7, 1, 10]
sorted_arr = [1, 2, 3, 4, 5, 7, 8, 10]
assert(quicksort(unsorted_arr) == sorted_arr)

