class BookNotAvaliableException(Exception):
  
  def __init__(self, text):
    self.text = text
    super().__init__(self.text)

class BookNotFoundException(Exception):
  
  def __init__(self, text):
    self.text = 'Book was not found'
    super().__init__(self.text)


class Book:
  def __init__(self,title:str, author:str,avaliable:bool):
    self.title = title
    self.author = author
    self.avaliable = avaliable
    
  def __str__(self):
    text = f'Title : {self.title} -- Author: {self.author} -- '
    text += 'Is avaliable' if self.avaliable else 'Is not avaliable'
    return text
  
class Library:
  def __init__(self, list_of_books):
    self.list_of_books = list_of_books
  
  def __str__(self):
    return '\n'.join(map(str, self.list_of_books))
  
  def avaliable_books(self):
    for book in self.list_of_books:
      if book.avaliable:
        print(book)
        
  def borrow_book(self,title):
    try: 
      for book in self.list_of_books:
        if book.title == title:
          if not book.avaliable:
            raise BookNotAvaliableException('Book is not avaliable')
          else: 
            book.avaliable = False
    except BookNotAvaliableException as err:
      print(f'\n EXCEPTION: {err} \n')
          
  def return_book(self,title):
    for book in self.list_of_books:
      try: 
        if title == book.title:
          
         book.avaliable = True         
      except BookNotFoundException as err:        
          print(f'{err}')

book1 = Book('Hamlet','Shakespeare',True)
book2 = Book('Romeo and Juliet','Shakespeare',True)
book3 = Book('Poeta en Nueva York','Federico García Lorca',False)
book4 = Book('La Regenta','Leopoldo Clarín',True)
book5 = Book('Niebla','Miguel de Unamuno',False)
list_of_books = [book1,book2,book3,book4,book5]
library1 = Library(list_of_books)

print(library1)


library1.borrow_book('Niebla')
print(library1)
library1.return_book('Hamlet')
print(library1)
