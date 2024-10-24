"""Write a function called "potencia".
It receives two integer numbers. Check that the numbers are integer. If they are not, raise an exception.
It calculates the power using a loop and returns the result.
Write a program that invokes the previous function. Use exceptions.
"""

def potencia(base, exponente):
    if  not type(base) is int or not type(exponente) is int:
        raise TypeError("Some of the inputs are not integers")
    
    produto = 1
    for element in range(exponente):
        produto *= base
            
    return produto

try:
    print(potencia(5,4))
except TypeError as error:
    print(error)

try:
    print(potencia("a",3))
except TypeError as error:
    print(error)

try:
    print(potencia(1,"patata"))
except TypeError as error:
    print(error)
    
print("patata")