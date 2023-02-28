class Circle:
   def __init__(self, name):
      self.name = name
   def draw(self):
       print("Drawing a circle "+str(self.name))

class Square:
   def __init__(self,name):
      self.name = name
   def draw(self):
      print("Drawing a square "+str(self.name))

v = []
v.append(Circle("Circle1"))
v.append(Square("Square1"))
v.append(Circle("Circle2"))
for i in range(len(v)):
   v[i].draw();



