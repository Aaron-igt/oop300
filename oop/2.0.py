class Music:
    def __init__(self ,title, artist):
        self.title = title
        self.artist = artist
        
    def show_song(self):
        print (f"{self.title} by {self.artist}")
    
    def play_song(self):
        print(f"Playing{self.title}")
        
playlist = [Music("You and I", "John Legend"), Music("All of me", "John Legend")]

print(playlist)