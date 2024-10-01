class Maths:
    
    grades = 0
    
    def __init__(self ,name ,age ,value):
        self.name = name
        self.age = age
        self.value = value
        Maths.grades += 10     
        
    def get_grades(cls):
        return Maths.grades
    
Student1 = Maths("Aaron", 20, 70)
Student1.get_increment_grades()
print(Student1.get_grades())
    