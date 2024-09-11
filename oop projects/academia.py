class student:
    def __init__(self, name, university, year, gpa):
        self.name = name
        self.university = university
        self.year = year
        self.gpa = gpa
    def passed(self):
        print(f"{student1.name} graduated from {student1.university} in {student1.year} with a {student1.gpa} CGPA.")

student1 = student ("Marcus", "UCU", 2024, 4.3)
student1.passed()