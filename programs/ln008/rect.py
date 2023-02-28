class Shape:
   def __init__(self):
      print("instantiating a shape object")

class Rectangle(Shape):
   def __init__(self,a,b):
      super().__init__()
      self.xdim = a
      self.ydim = b
   def area(self):
      return self.xdim*self.ydim

