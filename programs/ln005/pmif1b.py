def print_components(value):
    match value:
        case (x, y, z): 
            print("Components of triple: " + str(x) + "," + str(y) + "," + str(z))
        case (x, y): 
            print("Components of pair: " + str(x) + "," + str(y))
        case _: 
            print("Error: Not a triple or pair")

print_components((1, 2))

