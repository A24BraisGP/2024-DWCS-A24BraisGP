class Calculator:
    numberOfObjects = 0
    def __init__(self, num1 = 0, num2 = 0):
        if not type(num1) is int or not type(num2) is int:
            raise TypeError("They are not integers")
        else:
            self.num1 = num1
            self.num2 = num2
            Calculator.numberOfObjects += 1
            
    def __str__(self):
        return f"The numbers are {self.num1} and {self.num2}. The total of objects is {Calculator.numberOfObjects}"
    
    def suma(self):
        return self.num1 + self.num2
try:
    firstCalcule = Calculator()
    firstCalcule.num1 = 1
    firstCalcule.num2 = 3
    print(f"{firstCalcule.num1} and {firstCalcule.num2}")
except TypeError as error:
    print(error)
    


try:
    secondCalcule = Calculator(8,300)
    print(secondCalcule)
    print(f"sum of secondCalcule values: {secondCalcule.suma()}")
except TypeError as error:
    print(error)
    
try:
    thirdCalcule = Calculator(8,-55)
    print(thirdCalcule)
    print(f"sum of secondCalcule values: {thirdCalcule.suma()}")
except TypeError as error:
    print(error)
    