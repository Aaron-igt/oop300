class car:
    def __init__(self, brand, year, for_sale):
        self.brand = brand
        self.year = year
        self.for_sale = for_sale
    def drive(self):
        print(f"I drive a {car1.year} {car1.brand}.")    
car1 = car ("Jeep Grand Cherokee", 2024, False)
car1.drive()