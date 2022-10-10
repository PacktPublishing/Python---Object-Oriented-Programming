
class Book:
    def __init__(self,title,category):
        self.title = title
        self.category = category
    
    def __str__(self):
        return f'Book, {self.title}, {self.category}'
    
class Library:
    def __init__(self):
        self.books = []
        
    def add(self, book):
        assert isinstance(book,Book), 'you can only add book'
        self.books.append(book)
        
    def __getitem__(self,idx):
        return self.books[idx]
    
if __name__ == '__main__':
    b1 =Book("Python",'Textbook')
    b2 = Book("A man on the moon", "Novel")
    b3 = Book("C++","Textbook")
    b4 = Book("My love", "Novel")

    lib = Library()
    lib.add(b1)
    lib.add(b2)
    lib.add(b3)
    lib.add(b4)

    for book in lib:
        print(book)

