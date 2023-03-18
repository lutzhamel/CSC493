from functools import reduce

value = [1, 2, 3]
result = reduce(lambda x, y: x + y, value)

assert result == 6

