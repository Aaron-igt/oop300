class Library:
    
    total_books_issued = 0
    
    def __init__(self ,title ,author):
        self.title = title
        self.author = author
        self.issued = False
    def issue_book(self):
        if not self.issued:
            self.issued = True
            Library.total_books_issued += 1
            print(f"{self.title} has been issued.")
        else:
            print(f"{self.title} has already been issued.")
    def display(self):
        print(f"Book title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Issued: { 'yes' if self.issued else 'No'}")
    
    @classmethod
    def get_total_books_issued(cls):
        return cls.total_books_issued
    
Book1 = Library("Jane Eyre" ,"Charlotte Bronte")
Book2 = Library("1984", "George Orwell")

Book1.issue_book()
Book2.issue_book()

Book1.display()
Book2.display()

print(Library.get_total_books_issued())