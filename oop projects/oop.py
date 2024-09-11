class food:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
    def eat(self):
        print(f"You eat {food1.name}")
        

food1 = food ("Rice", "Carbohydrates", 2500)
print(food1.name)
print(food1.type)
print(food1.price)

food1.eat()


