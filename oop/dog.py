class Dog:
    
    birthday = "10/03/17"
    
    def __init__ (self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender
    
    def guard(self):
        return f"{Max.name}, a {Max.breed} is guarding."
    def play(self):
        return f"{Atom.name}, a {Atom.breed} is playing."
    def show(self):
        print(f"Name: {self.name}")
        print(f"Name: {self.breed}")
        print(f"Gender: {self.gender}")
        print(f"birthday: {Dog.birthday}")
    
Max = Dog("Max", "Rottweiler", "Male")
Atom = Dog("Atom", "Chihuahua", "Male")
print(Max.guard())
print(Atom.play())