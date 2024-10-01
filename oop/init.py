class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive the {self.color} {self.model}.")
    def stop(self):
        print(f"You stop the {self.color} {self.model}.")
    def describe(self):
        print(f"This is a {self.year} {self.color} {self.model}.")
        
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Charger", 2025, "black", True)
car3 = Car("G-Wagon", 2026, "white", True)

car2.stop()
car2.drive()
car2.describe()