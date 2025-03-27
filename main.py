class Book:
  def __init__(self,title,author,isbn,available=True):
    self.__title = title
    self.__author = author
    self.__isbn = isbn
    self.__available = available
  @property
  def title(self):
      return self.__title
  @property
  def author(self):
      return self.__author
  @property
  def isbn(self):
      return self.__isbn
  @property
  def available(self):
      return self.__available

  def __str__(self) -> str:
    status = "Available" if self.__available else "Not Available"
    return f"Title: {self.__title}, Author: {self.__author}, Status: {status}, ISBN: {self.__isbn}"
  def borrow(self):
    """marks book as unavailabe if it is available"""
    if self.__available:
      self.__available = False
      print(f"{self.__title} has been borrowed.")
    else:
      print(f"{self.__title} is alredy borrowed.")

  def return_book(self):
    """marks book as available again"""
    if not self.__available:
      self.__available = True
      print(f"{self.__title} has been returned.")
      return True
    else:
      print(f"{self.__title} was not borrowed.")
      return False


class Member:
  def __init__(self,name,member_id):
    self.__name = name
    self.__member_id = member_id
    self.__borrowed_books = []
  @property
  def name(self):
    return self.__name
  @property
  def member_id(self):
    return self.__member_id

  def borrow_book(self,book:Book):
    """adds book to borrowed_books list and marks it as unavailable"""
    if book.available:
      book.borrow()
      self.__borrowed_books.append(book)
      print(f"{self.__name} Borrowed '{book.title}'")
    else:
      print(f"Sorry, '{book.title}' is already borrowed.")

  def return_book(self, book:Book):
    """removes book from borrowed_books list and marks it as available"""
    if book in self.__borrowed_books:
      if book.return_book():
        self.__borrowed_books.remove(book)
        print(f"{self.__name} returned '{book.title}' ")
    else:
      print(f"{self.__name} has not borrowed '{book.title}'")

  def view_borrowed_books(self):
    """prints the list of borrowd books"""
    if self.__borrowed_books:
      print(f"{self.__name} has borrowd:")
      for book in self.__borrowed_books:
        print(f"- {book.title}")
    else:
      print(f"{self.__name} has not borrowed any bookks.")



class Library:
  def __init__(self):
    self.__books = []
    self.__members = []

  def add_books(self, book:Book):
    """adds a book to the library collection"""
    self.__books.append(book)
    print(f"'{book.title}' has been added to the library.")

  def remove_book(self,book:Book):
    """removes a book from the collection"""
    if book in self.__books:
      self.__books.remove(book)
      print(f"'{book.title}' has been removed from the library.")
    else:
      print(f"'{book.title}' is not in the library collection.")

  def register_member(self, member:Member):
    """adds a new member"""
    self.__members.append(member)
    print(f"Member: '{member.name}' (ID: {member.member_id}) has been registered.")

  def display_books(self):
    """shows all books with their avaiability"""
    if self.__books:
      print("\n--- Library Collection ---")
      for book in self.__books:
        print(book)
    else:
      print("No books availablel in the library.")

  def find_book_by_title(self, title:str):
    """searches for a book by title"""
    for book in self.__books:
      if book.title.lower().strip() == title.lower().strip():
        print(f"Book Found: {book}")
        return book
    print(f"No book found with title '{title}'.")
    return None


book1 = Book("The Wait of Hope","Hassaan",5678)
book2 = Book("Nothing to wait","Shani",1234)

member1 = Member("Aasia",123)
member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book1)
member1.view_borrowed_books()
member1.return_book(book1)
member1.view_borrowed_books()

library = Library()
library.add_books(book1)
library.add_books(book2)
library.register_member(member1)
library.remove_book(book2)
print("\n--- Finding a Book ---")
library.find_book_by_title("The Wait of Hope")
print("\n--- Library Books ---")
library.display_books()

