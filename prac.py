class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Maker: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
    
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")
    
class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Load capacity: {self.load_capacity}")
        
        
car1 = Car("Toyota", "Corolla", 2020, 4)
truck1 = Truck("Ford", "F-150", 2022, 5000)

car1.display_info()
truck1.display_info()