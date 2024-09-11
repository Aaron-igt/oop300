class country:
    def __init__(self ,name, continent, population):
        self.name = name
        self.continent = continent
        self.population = population
    def strong(self):
        print(f"{country1.name} is the strongest country in the world and in found in {country1.continent}")
        
country1 = country ("United states of America", "North America", 333300000)
country1.strong()
