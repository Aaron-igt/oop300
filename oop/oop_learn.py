class employee:
    def __init__(self, name, job, salary, address):
        self.name = name
        self.job = job
        self.salary = salary
        self.address = address
    def work (self):
        return f"{self.name} is the {self.job} at this establishment."
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")

emp_1 = employee("Ryan", "Manager", 500000, "Kampala")
emp_2 = employee("Aaron", "CEO", 1500000, "Jinja")

print(emp_1.work())
print(emp_2.work())
print(emp_1.show_info())
print(emp_2.show_info())