import datetime as dt
#Sintax to declare a python class
#The method have at least the self argument

class Person:
  # if we wanted class variables we would have to declare them outside of the constructor
  
  # Constructor method. 
  def __init__(self,name,email,telephone):
    self.name = name
    self.email = email 
    self.telephone= telephone 
    
    #To string method 
  def __str__(self):
    return f'Name : {self.name} -- Email : {self.email} -- Telephone : {self.telephone}'
  
class Product:
  def __init__(self,name,description,price,image):
    self.name = name
    self.description = description
    self.price = price
    self.image = image
    
  def __str__(self):
    return f'Product name : {self.name} -- Description : {self.description} -- Price : {self.price} -- Image : {self.image}'
  
class Order:
  
  #In this case, both client and list of products will be instatiation of the classes above, but will be when we initiate Order with that data
  def __init__(self,date,list_of_products,client):
    self.date = date
    self.list_of_products = list_of_products
    self.client = client
    
  def __str__(self):
    text = "Date :"+ str(self.date) + "\n" +"List of products :" + "\n"
    for product in self.list_of_products:
      text += "\t{" + str(product) + "}\n"
    text += "Client: {" + str(self.client) + "}"
    return text 
  
  #Itera sobre a lista executando en cada elemento o indicado, neste caso pasar a str cada elemento
  #solución de Jose : return map(str, self.list_of_products)
  
  #Auxiliar method that iterates by every item in the list of products and access individually every price atribute of said product in the list in order to sum them to a final total price
  
  def get_total(self):
    total = 0
    for product in self.list_of_products:
      total += float(product.price)
    return total
  
  #Solución de Gabriel : return sum(product.price for product in self.list_of_products)
  
  #
  
  
person1 = Person('Alberto','albgogar@gmail.com',698123456)
product1 = Product('Tennis Racket', 'An item to play tennis with', 99, 'image.jpg')
product2 = Product('Tennis ball', 'An item to play tennis with', 9.99, 'image.jpg')
product3 = Product('Tennis Net', 'An item to play tennis with', 999.99, 'image.jpg')

list_of_products = [product1, product2, product3]

order = Order(dt.datetime(1999,2,22),list_of_products,person1)
print(order)
print(f'The total is {str(order.get_total())} €')