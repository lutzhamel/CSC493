class Cup:
   pass

class CoffeeCup(Cup):
   pass

class TeaCup(Cup):
   pass

import inspect
from pprint import pprint as pp
pp(inspect.getclasstree(inspect.getmro(TeaCup)))
#inspect.getclasstree(inspect.getmro(TeaCup)) # Insert your Class instead of IOError.
