class Person:
  def __init__(self,name,email,telephone):
    self.name = name
    self.email = email 
    self.telephone= telephone 
  def __str__(self):
    return f'Name : {self.name} -- Email : {self.email} -- Telephone : {self.telephone}'
  
class Product:
  def __init__(self,name,description,price,image):
    self.name = name
    self.description = description
    self.price = price
    self.image = image
    
  def __str__(self):
    return f'Name : {self.name} -- Description : {self.description} -- Price : {self.price} -- Image : {self.image}'
  
class Order:
  def __init__(self,date,list_of_products,client):
    self.date = date
    self.list_of_products = list_of_products
    self.client = client
    
  def __str__(self):
    text = "Date :"+ self.date + "\n" +"List of products :"
    for product in self.list_of_products:
      text += "\t" + str(product) + "\n"
    text += "Client: {" + str(self.client) + "}"
    return text 
  
  def get_total(self):
    total = 0
    for product in self.list_of_products:
      total += product.price
    return total
  
  
person1 = Person('Alberto','albgogar@gmail.com',698123456)
product1 = Product('Tennis Racket', 'An item to play tennis with', 99, 'image.jpg')
product2 = Product('Tennis ball', 'An item to play tennis with', 9.99, 'image.jpg')
product3 = Product('Tennis Net', 'An item to play tennis with', 999.99, 'image.jpg')

list_of_products = [product1, product2, product3]

order = Order('1999-2-22',list_of_products,person1)
print(order)
print('The total is ' + str(order.get_total()))