class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def display_info(self):
        super().display_info()
        print(f"team size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        super().display_info()
        print(f"Main programming language: {self.programming_language}")
        
class TeamLead(Manager, Developer):
    def __init__(self, name, salary, team_size, programming_language):
        Employee.__init__(self, name, salary)  # Call Employee.__init__() directly
        self.team_size = team_size
        self.programming_language = programming_language
        
    def display_info(self):
         Employee.display_info(self)
         print(f"Team size: {self.team_size}")
         print(f"Main programming language: {self.programming_language}")
         
mgr = Manager("Alice", 90000, 5)
mgr.display_info()

dev = Developer("Bob", 80000, "Python")
dev.display_info()

lead = TeamLead("Charlie", 100000, 3, "JavaScript")
lead.display_info()