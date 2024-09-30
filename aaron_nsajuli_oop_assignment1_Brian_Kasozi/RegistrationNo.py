class RegNo:
    def __init__(self, name, age, registration_number):
        self.name = name
        self.age = age
        self.registration_number = registration_number
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Registration Number: {self.registration_number}")
        
    
Student1 = RegNo("Aaron" ,22 ,"S23B13/047")
Student1.show_info()