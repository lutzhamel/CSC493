class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

class Person(Address):
    def __init__(self, name, age, street, city, state, zip):
        super().__init__(street, city, state, zip)
        self.name = name
        self.age = age

person = Person("John Doe", 30, "123 Main St", "Anytown", "CA", "12345")

