class Bird:
    def __init__(self, size, coloration, markings):
        self.size = size
        self.coloration = coloration
        self.markings = markings

observed_bird = Bird("tiny", "red", "black stripes")

match observed_bird:
   case Bird(size="big", coloration="blue", markings="yellow dots"): # pattern match
      print("it is a blue polka")
   case Bird(size="tiny", coloration="red", markings="green stripes"): # pattern match
      print("it is a green striped finch")
   case Bird(size="tiny", coloration="red", markings="black stripes"): # pattern match
      print("it is a striped sparrow")
   case _:
      print("unknown bird")


