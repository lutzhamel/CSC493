# curried function
def cost(tax):
   return lambda price : price+(price*tax/100.0)

# partially evaluate function with tax rate
macost = cost(6.25)
ricost = cost(7.0)

# show that the results are functions
assert callable(macost)
assert callable(ricost)

# use the functions
assert (macost(100.0) == 106.25)
assert (ricost(100.0) == 107.0)

