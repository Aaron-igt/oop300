class University:
    
    num_of_unis = 0
    
    def __init__(self, name, location, motto, num_intakes = 3):
        self.name = name
        self.location = location
        self.motto = motto
        self.num_intakes = num_intakes
        University.num_of_unis += 1
        
    def showInfo(self):
        print (f"Name: {self.name}")
        print (f"Location: {self.location}")
        print (f"Motto: {self.motto}")
        print (f"number of Intakes: {self.num_intakes}")


university1 = University("UCU", "Mukono", "Centre of excellence")
university2 = University("makerere University", "Banda", "We build for the future")
university3 = University("Kampala internation uni", "Kansanga", "We move")
university4 = University("Kyambogo University", "Banda", "Bolingo")

university1.showInfo()
university2.showInfo()
university3.showInfo()
university4.showInfo()
print (University.num_of_unis)