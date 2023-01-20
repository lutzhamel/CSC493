class Person:
   def __init__(self, name, age, profession):
      self.name = name
      self.age = age
      self.profession = profession


joe = Person("Joe", 32, "Cook")

match joe:
   case Person(name=n,age=a,profession=p):
      pass
   case _:
      raise ValueError("match error")

assert (n=="Joe" and a==32 and p=="Cook")
