class team:
    position = 1
    def __init__(self, name, slogan):
        self.name = name
        self.slogan = slogan
    
    def show_info(self):
        print(f"Team {self.name} - {self.slogan}")
        
team1 = team ("Arsenal" , "Gunners")
team2 = team ("ManU" , "It will never run.")

print(team1.show_info())
print(team2.show_info())