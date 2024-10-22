class Shape:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides
        
    def area(self):
        print(f"{type}'s Calculating Area")
        
class Square(Shape):
    def __init__(self ,type ,sides, len):
        super().__init__(type, sides)
        self.len = len
        
    def area(self):
        Area = self.len ** 2
        print(f"{self.type}'s Area = {Area}")
        
sq = Square("square", 4, 4)

# sq.area()

class Rectangle(Shape):
    def __init__(self, type, sides, width, height):
        super().__init__(type, sides)
        self.width = width
        self.height = height
        
    def area(self):
        Area = self.height * self.width
        print(f"{self.type} area is {Area}")
    
rect = Rectangle("Rectangle", 4, 8, 4)

rect.area()