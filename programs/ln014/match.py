def f(x, y):
   match (x, y):
      case (x, y) if x > y:
         return "GT"
      case (x, y) if x < y:
         return "LT"
      case _:
         raise ValueError("not a valid tuple")

         