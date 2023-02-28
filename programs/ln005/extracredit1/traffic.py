# define what kind of vehicles come through the toll station
class Car:
   def __init__(self, kind, occupants):
      self.kind = kind  # "ev", "hybrid", "gas"
      self.occupants = occupants  # integer between 1 and 4 inclusive

class Truck:
   def __init__(self, kind):
      self.kind = kind  # "small", "medium", "large"

class Taxi:
   def __init__(self, company, passengers):
      self.company = company  # "YellowCab", "Downtown", "Checkered"
      self.passengers = passengers  # integer between 0 and 3 inclusive

class Bus:
   def __init__(self, capacity, riders):
      self.capacity = capacity  # integer 25 and 50
      self.riders = riders  # integer 0 and max capacity

# a list that holds the actual vehicle objects that went through the 
# toll station
traffic = [
   Car("hybrid", 2),
   Truck("small"),
   Taxi("Downtown", 3),
   Bus(25, 10),
   Car("gas", 1),
   Truck("medium"),
   Taxi("YellowCab", 1),
   Bus(50, 30),
   Car("ev", 4),
   Car("gas", 3),
   Car("hybrid", 1),
   Car("ev", 2),
   Truck("large"),
   Truck("medium"),
   Truck("small"),
   Truck("large"),
   Taxi("YellowCab", 1),
   Taxi("Downtown", 2),
   Taxi("Checkered", 3),
   Taxi("YellowCab", 1),
   Bus(25, 20),
   Bus(50, 40),
   Bus(25, 15),
   Bus(50, 30),
   Car("hybrid", 3),
   Car("gas", 2),
   Car("ev", 1),
   Car("hybrid", 4),
   Truck("medium"),
   Truck("large"),
   Truck("small"),
   Truck("medium"),
   Taxi("Downtown", 1),
   Taxi("Checkered", 2),
   Taxi("YellowCab", 3),
   Taxi("Checkered", 1),
   Bus(50, 45),
   Bus(25, 22),
   Bus(50, 38),
   Bus(25, 18),
   Car("gas", 4),
   Car("hybrid", 2),
   Car("ev", 3),
   Car("gas", 1),
   Truck("small"),
   Truck("medium"),
   Truck("large"),
   Truck("small"),
   Taxi("Downtown", 2),
   Taxi("Checkered", 1),
   Taxi("YellowCab", 3),
   Taxi("YellowCab", 2),
   Bus(50, 50),
   Bus(25, 25),
   Bus(50, 48),
   Bus(25, 20),
   Car("hybrid", 1),
   Car("ev", 4)
]
