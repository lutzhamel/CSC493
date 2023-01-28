class Rect:
   def __init__(self, x, y):
      self.xdim = x
      self.ydim = y

   def area (self):
      return self.xdim * self.ydim  # accessing internal identity via self

r = Rect(2.0, 4.0)
a = r.area ()
assert (a == 8.0)

