# system managing different employees in a company
class Employee:
    
    company_name = "IGT inc."
    
    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.__salary = salary
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.__salary}")
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
    
    @classmethod    
    def set_company_name(cls, name):
        cls.company_name = name
    
    def welcome_message(self):
        print(f"Welcome {self.name}")
    
class FullTimeEmployee(Employee):
    def __init__(self, name, age, employee_id, salary, annual_bonus):
        super().__init__(name, age, employee_id, salary)
        self.annual_bonus = annual_bonus
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Annual Bonus: {self.annual_bonus}")
        
class PartTimeEmployee(Employee):
    def __init__(self, name, age, employee_id, hourly_rate):
        super().__init__(name, age, employee_id)
        self.hourly_rate = hourly_rate
        
    def calculate_monthly_salary(self, hours_worked):
        monthly_salary = hours_worked * self.hourly_rate
        print(f"{self.name}'s monthly salary is {monthly_salary}.")
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Hourly Rate: {self.hourly_rate}")
        
        
