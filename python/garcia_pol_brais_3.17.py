# In order to stablish a custom exception we create a class that inherits the Exception class
class DivisionByZeroError(Exception):
  
  
  def __init__(self,text):
    self.text = text
    super().__init__(self.text)
    
  
#In the fuction we check if the denominator is 0, if it is we raise the exception with the message and print it 


def divide_numbers(numerator, denominator):
  try:
    if denominator == 0:
      raise DivisionByZeroError("Cannot divide by 0")
    return numerator / denominator

  except DivisionByZeroError as error:
    print(f'EXCEPTION: {error}')
    
  
 
   
result = divide_numbers(3,4)

print(result)
   
 
result = divide_numbers(3,0)


print(result)

result = divide_numbers(0,5)

print(result)
 
    
  
    
    