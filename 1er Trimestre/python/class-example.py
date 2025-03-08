class Car:
    
    model = "Volvo"
    
    
    def __init__(self, color, power ):
        self.color = color
        self.power = power
        
    def __str__(self):
        return f"The {self.color} {self.model} has {self.power} many horsepower"
    
    def getColor(self):
        return self.color
    
    def getModel():
        return Car.model
    
## If we create an attribute with the same name as the class atribute it will register it from the object att
myCar = Car("red", 100)
print(myCar)
myCar.model = "BMW"

Car.model = "Submarine"
print(myCar)
del myCar.model
print(myCar)

myCar2 = Car("yellow", 3000)

print(myCar2)

print(myCar2.getColor())
print(Car.getModel())