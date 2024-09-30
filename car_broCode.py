class Student:
    
    # class variables
    year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
    def show_info(self):
       print (f"Name: {self.name}") 
       print (f"Age: {self.age}")
       print (f"Year: {Student.year}")
student1 = Student("Ryan", 25)
student2 = Student("Aaron", 22)
student3 = Student("Samartha", 20)
student4 = Student("Ricky", 23)
student5 = Student("Josh", 24)

print(student1.show_info())
print(student2.show_info())
print(student3.show_info())
print(student4.show_info())
print(Student.num_students)