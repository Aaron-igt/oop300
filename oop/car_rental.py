class CarRental:
    
    total_rented_cars = 0
    
    def __init__(self, model, rental_price):
        self.model = model
        self.rental_price = rental_price
    
    def rent_car(self, no_of_days):
        total_cost = self.rental_price * no_of_days
        print(f"The {self.model} will cost you ${total_cost} for {no_of_days} days.")
        
        CarRental.total_rented_cars += 1
    
    def display(self):
        print(f"Car Model: {self.model}")
        print(f"Price per day: ${self.rental_price}")
    
    @classmethod    
    def get_total_rented(cls):
        return cls.total_rented_cars
        
Car1 = CarRental("Jeep Grand cherokee", 3000)
Car2 = CarRental("Lamborghini Aventador", 10000)
 
Car1.rent_car(3)
Car2.rent_car(2)
Car2.display()
print(f"The total number of cars rented is {CarRental.get_total_rented()}.")       