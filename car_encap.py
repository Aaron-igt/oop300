class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self._model = model # protected (single underscore)
        self.__year = year # private (double underscore)
        
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year
    
car1 = Car("Ferrari", "Purosangue", 2023)
car2 = Car("Lamborghini", "Revuelto", 2023)

car1.brand = "Honda"
car1._model = "Civic"
car1.set_year(2018)

print(car1.brand)

print(car1._model)

print(car1.get_year())

