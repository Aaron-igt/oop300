class book:
    def __init__(self, title, author, pages, genre, volume):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.volume = volume
        
    def __str__(self):
        return f"{self.title} by {self.author}."
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        return f"{self.title} has been deleted."
    
    def get_chapter(self, chapter):
        return f"{self.title} - chapter{chapter}."
    
    def get_author(self):
        return f"{self.title} is written by {self.author}."
    
    def show_info(self):
        return f"{self.title} is written by {self.author}."
    
book1 = book ("The moon also sets", "John Doe", 565, "Fiction", 1)
book2 = book ("The Art of racing in the rain", "Garth Stein", 200, "Fiction", 2)
book3 = book ("First Blood", "David Morrell", 400, "Action", 1)

print(book1.get_author())
print(book2.get_author())
print(book3.show_info())