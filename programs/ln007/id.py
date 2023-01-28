class foo:
   def getid (self):
      return id(self)

o = foo()
external_id = id(o)
internal_id = o.getid()
assert(external_id == internal_id)

