# We begin by declaring both exceptions. Like before, they inherit the Exception class and are raised whenever we need them to pop up 
class BookNotAvaliableException(Exception):
  
  def __init__(self, text):
    self.text = text
    super().__init__(self.text)

class BookNotFoundException(Exception):
  
  def __init__(self, text):
    self.text = text
    super().__init__(self.text)


#We now declare both classes, considering each argument SHOULD be of the declared type, or that the constructor is going to expect those specific data types
class Book:
  def __init__(self,title:str, author:str,avaliable:bool):
    self.title = title
    self.author = author
    self.avaliable = avaliable
    
# We print the book, changing the text of the avaliability considering the value of the bool avaliable 
  def __str__(self):
    text = f'Title : {self.title} -- Author: {self.author} -- '
    text += 'Is avaliable' if self.avaliable else 'Is not avaliable'
    return text
  
class Library:
  def __init__(self, list_of_books):
    self.list_of_books = list_of_books
  
# To string method Jose introduced in earlier exercises. Map in python iterates and acts recursively in every item of a colection
  def __str__(self):
    return '\n'.join(map(str, self.list_of_books))
  
  def avaliable_books(self):
    for book in self.list_of_books:
      if book.avaliable:
        print(book)
        
#Exceptions should be attached to an specific block of code !! you can capture multiple exceptions but not raise them consecuentially in the same block/indent

#We try to check every item of the list. If the title of the book coincide with the one we iterate over it checks if its avaliable, if not, the exception raises and it exits the loop. If no book in the list coincided with the check, the book no found exception raises
  def borrow_book(self,title):
    book_found = False
    try: 
      for book in self.list_of_books:
        if book.title == title:
          if not book.avaliable:
            book_found = True
            raise BookNotAvaliableException(book.title + ' is not avaliable')
          else: 
            book.avaliable = False
            
      if not book_found:
        raise BookNotFoundException(title + ' was not found in the library')
    except BookNotAvaliableException as err:
      print(f'\n EXCEPTION: {err} \n')
    except BookNotFoundException as err:
      print(f'\n EXCEPTION: {err} \n')
          
  def return_book(self,title):
    book_found = False
    try: 
    
      for book in self.list_of_books:
        if title == book.title:
          book.avaliable = True 
          book_found = True
          
      if not book_found:
        raise BookNotFoundException(title + ' was not found in the library')
    except BookNotFoundException as err:        
      print(f'\n EXCEPTION: {err} \n')

book1 = Book('Hamlet','Shakespeare',True)
book2 = Book('Romeo and Juliet','Shakespeare',True)
book3 = Book('Poeta en Nueva York','Federico García Lorca',False)
book4 = Book('La Regenta','Leopoldo Clarín',True)
book5 = Book('Niebla','Miguel de Unamuno',False)
list_of_books = [book1,book2,book3,book4,book5]
library1 = Library(list_of_books)


library1.borrow_book('Niebla')
print(library1)
library1.return_book('Niebla')
print(library1)

#A book that doesn't exist
library1.return_book('AAAAAAA')
library1.borrow_book('AAAAAAAAA')