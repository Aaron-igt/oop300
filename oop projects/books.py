class book:
    def __init__(self, name, author, publisher, year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
    def read(self):
        print(f"My Grandfather always read {book1.name} by {book1.author} to me before I went to bed back in 2005.")

book1 = book ("Oliver twist", "Cherles Dickens", "Serial: Bentley's Miscellany Book: Richard Bentley", 1838)
book1.read()