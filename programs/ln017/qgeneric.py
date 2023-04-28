
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__ (self):
       return self.name+"("+str(self.age)+")"

people = [
   Person("Liz",32),
   Person("Joe",20),
   Person("Jessica",22),
   Person("Peter",18)
]

def order_age (a,b):
   return a.age <= b.age

def quicksort(arr, order):
    match arr:
        case []:
            return []
        case [a]:
            return [a]
        case (pivot,*rest):
            less = [x for x in rest if order(x, pivot)]
            greater = [x for x in rest if not order(x, pivot)]
            return quicksort(less, order) + [pivot] + quicksort(greater, order)

# sort people by their age
sorted = quicksort(people, order_age)
for p in sorted:
   print(p)


      