l = [x for x in range(1,10+1)]
it = map(lambda x : x % 2, l)
a = list(map(lambda x : 1 if x else -1, it))

assert(a == [1,-1,1,-1,1,-1,1,-1,1,-1])

