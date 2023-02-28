def print_components(value):
    if type(value) == tuple and len(value) == 3:
        print("Components of triple: "+str(value[0])+","+str(value[1])+","+str(value[2]))
    elif type(value) == tuple and len(value) == 2:
        print("Components of pair: "+str(value[0])+","+str(value[1]))
    else:
        print("Error: Not a triple or pair")

print_components((1,2))

